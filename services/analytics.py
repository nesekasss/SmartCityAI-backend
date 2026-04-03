from services.scoring import (
    calculate_transport_score,
    calculate_environment_score,
    calculate_total_risk,
    risk_to_priority,
    calculate_confidence,
    calculate_decision_score,
)
from services.forecasting import forecast_district


def detect_anomaly(d):
    reasons = []

    if d["traffic_level"] >= 8:
        reasons.append("Traffic congestion is above critical threshold")
    if d["avg_speed"] < 20:
        reasons.append("Average speed is critically low")
    if d["pm25"] > 35:
        reasons.append("PM2.5 exceeds safe threshold")
    if d["co"] > 1.5:
        reasons.append("CO concentration exceeds alert threshold")
    if d["accidents"] >= 3:
        reasons.append("High accident count detected")

    return len(reasons) > 0, reasons


def determine_transport_status(traffic_level, avg_speed):
    if traffic_level >= 8 or avg_speed < 20:
        return "critical"
    if traffic_level >= 5 or avg_speed < 30:
        return "warning"
    return "stable"


def determine_environment_status(pm25, co):
    if pm25 > 35 or co > 1.5:
        return "critical"
    if pm25 > 20 or co > 1.0:
        return "warning"
    return "stable"


def detect_correlation(d):
    traffic_level = d["traffic_level"]
    pm25 = d["pm25"]
    co = d["co"]

    if traffic_level >= 8 and (pm25 > 35 or co > 1.5):
        return {
            "cross_domain_correlation": True,
            "correlation": "Traffic congestion is directly contributing to environmental degradation."
        }

    if traffic_level >= 5 and pm25 > 20:
        return {
            "cross_domain_correlation": True,
            "correlation": "Transport load is likely influencing air quality conditions."
        }

    return {
        "cross_domain_correlation": False,
        "correlation": "No strong cross-domain dependency detected."
    }


def analyze_city(data):
    results = []

    for d in data:
        transport_status = determine_transport_status(d["traffic_level"], d["avg_speed"])
        environment_status = determine_environment_status(d["pm25"], d["co"])

        transport_score = calculate_transport_score(
            d["traffic_level"],
            d["avg_speed"],
            d["accidents"],
        )
        environment_score = calculate_environment_score(
            d["pm25"],
            d["co"],
        )
        risk_score = calculate_total_risk(transport_score, environment_score)
        priority, color = risk_to_priority(risk_score)

        anomaly_detected, anomaly_reasons = detect_anomaly(d)
        forecast = forecast_district(d)
        correlation_info = detect_correlation(d)

        confidence = calculate_confidence(
            anomaly_detected=anomaly_detected,
            anomaly_reasons=anomaly_reasons,
            risk_score=risk_score,
        )

        decision_score = calculate_decision_score(
            risk_score=risk_score,
            anomaly_detected=anomaly_detected,
            forecast_summary=forecast["forecast_summary"],
        )

        results.append({
            "name": d["district"],
            "transport": {
                "traffic_level": int(d["traffic_level"]),
                "avg_speed": int(d["avg_speed"]),
                "accidents": int(d["accidents"]),
                "status": transport_status,
                "score": int(transport_score),
            },
            "environment": {
                "pm25": int(d["pm25"]),
                "co": float(d["co"]),
                "humidity": int(d["humidity"]),
                "temperature": int(d["temperature"]),
                "status": environment_status,
                "score": int(environment_score),
            },
            "risk_score": float(risk_score),
            "decision_score": float(decision_score),
            "confidence": float(confidence),
            "priority": priority,
            "color": color,
            "is_problem": priority == "high",
            "anomaly_detected": anomaly_detected,
            "anomaly_reasons": anomaly_reasons,
            "forecast": forecast,
            "cross_domain_correlation": correlation_info["cross_domain_correlation"],
            "correlation": correlation_info["correlation"],
        })

    return results