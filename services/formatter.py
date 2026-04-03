from datetime import datetime


def build_overview(districts):
    city_health_index = 100

    for d in districts:
        if d["priority"] == "high":
            city_health_index -= 18
        elif d["priority"] == "medium":
            city_health_index -= 8

    city_health_index = max(city_health_index, 0)

    active_alerts = len([d for d in districts if d["priority"] == "high"])
    critical_districts = len([
        d for d in districts
        if d["transport"]["status"] == "critical" or d["environment"]["status"] == "critical"
    ])

    average_traffic_level = round(
        sum(d["transport"]["traffic_level"] for d in districts) / len(districts), 1
    )
    average_pm25 = round(
        sum(d["environment"]["pm25"] for d in districts) / len(districts), 1
    )
    average_risk_score = round(
        sum(d["risk_score"] for d in districts) / len(districts), 1
    )
    average_confidence = round(
        sum(d["confidence"] for d in districts) / len(districts), 2
    )
    average_decision_score = round(
        sum(d["decision_score"] for d in districts) / len(districts), 1
    )

    if city_health_index < 40:
        overall_status = "critical"
        system_mode = "critical"
    elif city_health_index < 70:
        overall_status = "warning"
        system_mode = "stress"
    else:
        overall_status = "stable"
        system_mode = "normal"

    top_problem_district = None
    if districts:
        top_problem_district = sorted(
            districts,
            key=lambda x: x["risk_score"],
            reverse=True
        )[0]["name"]

    resilience_score = max(0, round((city_health_index * 0.6) + (100 - average_risk_score) * 0.4, 1))

    if resilience_score >= 75:
        resilience_interpretation = "The city system is resilient under the current load."
    elif resilience_score >= 50:
        resilience_interpretation = "The city remains operational but is vulnerable to escalating stress."
    else:
        resilience_interpretation = "The city system shows low resilience under current conditions."

    return {
        "city_health_index": city_health_index,
        "active_alerts": active_alerts,
        "critical_districts": critical_districts,
        "average_traffic_level": average_traffic_level,
        "average_pm25": average_pm25,
        "average_risk_score": average_risk_score,
        "average_confidence": average_confidence,
        "average_decision_score": average_decision_score,
        "overall_status": overall_status,
        "system_mode": system_mode,
        "top_problem_district": top_problem_district,
        "resilience_score": resilience_score,
        "resilience_interpretation": resilience_interpretation,
        "kpi_cards": {
            "traffic": average_traffic_level,
            "air_quality": average_pm25,
            "risk": average_risk_score,
            "confidence": average_confidence,
        },
    }


def build_meta():
    return {
        "city": "Almaty",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "data_source": "simulated urban operational data",
        "ai_mode": "rule-based explainable decision engine v5",
    }


def build_summary(districts):
    high = [d["name"] for d in districts if d["priority"] == "high"]
    medium = [d["name"] for d in districts if d["priority"] == "medium"]

    if high:
        return f"Critical conditions detected in {', '.join(high)}."
    if medium:
        return f"Warning-level conditions detected in {', '.join(medium)}."
    return "City operating normally."