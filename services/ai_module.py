def generate_actions(district):
    actions = []

    traffic = district["transport"]["traffic_level"]
    avg_speed = district["transport"]["avg_speed"]
    pm25 = district["environment"]["pm25"]
    co = district["environment"]["co"]

    if traffic >= 8:
        actions.append("Adjust traffic light timing on overloaded corridors")

    if avg_speed < 20:
        actions.append("Deploy traffic control units to improve mobility")

    if pm25 > 35:
        actions.append("Issue air quality warning")

    if co > 1.5:
        actions.append("Restrict high-emission vehicles in critical zones")

    if traffic >= 8 and pm25 > 35:
        actions.append("Increase public transport capacity to reduce load")

    if not actions:
        actions.append("Continue monitoring conditions")

    return actions


def build_structured_actions(district):
    actions = []

    if district["transport"]["traffic_level"] >= 8:
        actions.append({
            "action": "Adjust traffic light timing on overloaded corridors",
            "priority": "high",
            "time_horizon": "immediate",
            "expected_benefit": "Reduces congestion within 30-60 minutes",
            "justification": "High traffic load detected"
        })

    if district["transport"]["avg_speed"] < 20:
        actions.append({
            "action": "Deploy traffic control units",
            "priority": "high",
            "time_horizon": "immediate",
            "expected_benefit": "Improves traffic flow and reduces delays",
            "justification": "Critically low average speed"
        })

    if district["environment"]["pm25"] > 35:
        actions.append({
            "action": "Issue air quality warning",
            "priority": "medium",
            "time_horizon": "short-term",
            "expected_benefit": "Reduces public exposure to air pollution",
            "justification": "PM2.5 exceeds safe threshold"
        })

    if district["environment"]["co"] > 1.5:
        actions.append({
            "action": "Restrict high-emission vehicles in critical zones",
            "priority": "high",
            "time_horizon": "immediate",
            "expected_benefit": "Improves air quality within 1-2 hours",
            "justification": "CO concentration exceeds alert threshold"
        })

    if district["transport"]["traffic_level"] >= 8 and district["environment"]["pm25"] > 35:
        actions.append({
            "action": "Increase public transport capacity to reduce private vehicle load",
            "priority": "high",
            "time_horizon": "short-term",
            "expected_benefit": "Lowers congestion and pollution simultaneously",
            "justification": "Cross-domain stress detected between transport and environment"
        })

    if not actions:
        actions.append({
            "action": "Maintain monitoring",
            "priority": "low",
            "time_horizon": "monitoring",
            "expected_benefit": "No immediate intervention required",
            "justification": "System conditions are stable"
        })

    return actions


def extract_top_risks(district):
    risks = []

    if district["transport"]["traffic_level"] >= 8:
        risks.append("traffic overload")

    if district["transport"]["avg_speed"] < 20:
        risks.append("low urban mobility")

    if district["environment"]["pm25"] > 35:
        risks.append("air pollution spike")

    if district["environment"]["co"] > 1.5:
        risks.append("toxic gas concentration")

    if district["transport"]["accidents"] >= 3:
        risks.append("incident-driven disruption")

    return risks


def root_cause_analysis(district):
    causes = []

    if district["transport"]["traffic_level"] >= 8:
        causes.append("road network overload")

    if district["transport"]["accidents"] >= 3:
        causes.append("incident-driven congestion")

    if district["environment"]["pm25"] > 35:
        causes.append("vehicle emissions concentration")

    if district["environment"]["co"] > 1.5:
        causes.append("poor air dispersion and concentrated emissions")

    return causes


def scenario_analysis(district):
    traffic = district["transport"]["traffic_level"]
    pm25 = district["environment"]["pm25"]
    co = district["environment"]["co"]

    if traffic >= 8 and (pm25 > 35 or co > 1.5):
        return {
            "without_action": "Traffic congestion and pollution levels may increase further within the next 2 hours, creating a high probability of service disruption and environmental stress.",
            "with_action": "Applying the recommended actions may reduce traffic pressure, stabilize mobility, and slow environmental degradation within 1-2 hours."
        }

    if traffic >= 5 or pm25 > 20:
        return {
            "without_action": "Warning-level conditions may escalate into a critical event during peak load.",
            "with_action": "Preventive intervention can stabilize conditions and avoid escalation."
        }

    return {
        "without_action": "No significant deterioration is expected.",
        "with_action": "Monitoring is sufficient; no immediate intervention is required."
    }


def secondary_risks(district):
    risks = []

    if district["transport"]["traffic_level"] >= 8:
        risks.append("Public transport delays may increase")
        risks.append("Emergency response time may be affected")

    if district["environment"]["pm25"] > 35:
        risks.append("Public health risk may increase")

    if district["transport"]["accidents"] >= 3:
        risks.append("Urban mobility disruption may spread to adjacent corridors")

    if district["environment"]["co"] > 1.5:
        risks.append("Air quality deterioration may intensify in nearby areas")

    return risks


def expected_impact(district):
    traffic = district["transport"]["traffic_level"]
    pm25 = district["environment"]["pm25"]
    co = district["environment"]["co"]

    if traffic >= 8 and pm25 > 35:
        return "Expected reduction of congestion pressure and stabilization of air quality within the next 1-2 hours after intervention."

    if traffic >= 8:
        return "Expected improvement in traffic flow within the next hour after intervention."

    if pm25 > 35 or co > 1.5:
        return "Expected environmental stabilization within the next 1-2 hours after intervention."

    return "Moderate impact expected; continued monitoring recommended."


def decision_urgency(priority):
    if priority == "high":
        return "immediate"
    if priority == "medium":
        return "short-term"
    return "monitoring"


def decision_window(priority):
    if priority == "high":
        return "Action required within 30 minutes"
    if priority == "medium":
        return "Action recommended within 2 hours"
    return "Safe to monitor for the next 2-4 hours"


def system_impact(district):
    if district["priority"] == "high":
        return "district-level"
    if district["priority"] == "medium":
        return "localized"
    return "localized"


def severity_breakdown(district):
    return {
        "transport": district["transport"]["status"],
        "environment": district["environment"]["status"]
    }


def build_decision_trace(district):
    trace = []

    if district["transport"]["traffic_level"] >= 8:
        trace.append("High traffic congestion detected")

    if district["transport"]["avg_speed"] < 20:
        trace.append("Average speed below critical threshold")

    if district["transport"]["accidents"] >= 3:
        trace.append("Incident density contributes to operational stress")

    if district["environment"]["pm25"] > 35:
        trace.append("PM2.5 exceeds safe threshold")

    if district["environment"]["co"] > 1.5:
        trace.append("CO concentration exceeds alert threshold")

    if district.get("cross_domain_correlation"):
        trace.append("Cross-domain impact between transport and environment confirmed")

    trace.append(f"Risk score calculated: {district['risk_score']}")
    trace.append(f"Decision score calculated: {district['decision_score']}")
    trace.append(f"Confidence level estimated: {district['confidence']}")

    return trace


def generate_alerts(districts):
    alerts = []

    for d in districts:
        if d["priority"] == "high":
            alerts.append({
                "district": d["name"],
                "severity": "high",
                "type": "critical cross-domain event",
                "message": "Multiple transport and/or environmental thresholds exceeded",
                "risk_score": d["risk_score"],
                "decision_score": d["decision_score"]
            })
        elif d["priority"] == "medium" and d["anomaly_detected"]:
            alerts.append({
                "district": d["name"],
                "severity": "medium",
                "type": "warning anomaly",
                "message": "Warning-level anomaly detected",
                "risk_score": d["risk_score"],
                "decision_score": d["decision_score"]
            })

    return alerts


def district_ranking(districts):
    sorted_districts = sorted(districts, key=lambda x: x["risk_score"], reverse=True)

    return [
        {
            "name": d["name"],
            "risk_score": d["risk_score"],
            "priority": d["priority"]
        }
        for d in sorted_districts
    ]


def summarize_critical_districts(districts):
    high_priority = sorted(
        [x for x in districts if x["priority"] == "high"],
        key=lambda x: x["risk_score"],
        reverse=True
    )
    return [d["name"] for d in high_priority]


def executive_summary(district):
    if district["priority"] == "high":
        return (
            f"Critical congestion and environmental stress detected in {district['name']}. "
            f"Immediate intervention is required."
        )

    if district["priority"] == "medium":
        return (
            f"Warning-level instability detected in {district['name']}. "
            f"Preventive intervention is advisable."
        )

    return (
        f"Conditions in {district['name']} are stable. Continued monitoring is sufficient."
    )


def intervention_effectiveness_score(district):
    score = 60

    if district["priority"] == "high":
        score += 20

    if district["transport"]["traffic_level"] >= 8:
        score += 8

    if district["environment"]["pm25"] > 35:
        score += 7

    if district["environment"]["co"] > 1.5:
        score += 5

    return min(score, 95)


def generate_ai_report(districts):
    high_priority = [d for d in districts if d["priority"] == "high"]
    medium_priority = [d for d in districts if d["priority"] == "medium"]

    alerts = generate_alerts(districts)
    ranking = district_ranking(districts)
    top_critical = summarize_critical_districts(districts)

    if high_priority:
        top = sorted(high_priority, key=lambda x: x["risk_score"], reverse=True)[0]

        return {
            "executive_summary": executive_summary(top),
            "what_is_happening": (
                f"Critical multi-domain stress detected in {top['name']} district. "
                f"Transport congestion and environmental indicators are simultaneously above safe operational thresholds."
            ),
            "criticality": (
                f"High criticality. Risk score is {top['risk_score']}, "
                f"decision score is {top['decision_score']}, and confidence is {top['confidence']}."
            ),
            "recommended_actions": generate_actions(top),
            "structured_actions": build_structured_actions(top),
            "top_risks": extract_top_risks(top),
            "root_cause": root_cause_analysis(top),
            "forecast": top["forecast"]["forecast_summary"],
            "affected_districts": [d["name"] for d in high_priority],
            "top_critical_districts": top_critical,
            "decision_priority": "high",
            "decision_urgency": decision_urgency(top["priority"]),
            "decision_window": decision_window(top["priority"]),
            "expected_impact": expected_impact(top),
            "correlation": top["correlation"],
            "confidence": top["confidence"],
            "decision_score": top["decision_score"],
            "scenario_analysis": scenario_analysis(top),
            "secondary_risks": secondary_risks(top),
            "alerts": alerts,
            "district_ranking": ranking,
            "decision_trace": build_decision_trace(top),
            "system_impact": system_impact(top),
            "severity_breakdown": severity_breakdown(top),
            "intervention_effectiveness_score": intervention_effectiveness_score(top),
            "cascade_effects": secondary_risks(top),
        }

    if medium_priority:
        top = sorted(medium_priority, key=lambda x: x["risk_score"], reverse=True)[0]

        return {
            "executive_summary": executive_summary(top),
            "what_is_happening": (
                f"Moderate stress detected in {top['name']} district. "
                f"Some transport or environmental indicators are approaching warning thresholds."
            ),
            "criticality": (
                f"Medium criticality. Risk score is {top['risk_score']}, "
                f"decision score is {top['decision_score']}, and confidence is {top['confidence']}."
            ),
            "recommended_actions": generate_actions(top),
            "structured_actions": build_structured_actions(top),
            "top_risks": extract_top_risks(top),
            "root_cause": root_cause_analysis(top),
            "forecast": top["forecast"]["forecast_summary"],
            "affected_districts": [d["name"] for d in medium_priority],
            "top_critical_districts": top_critical,
            "decision_priority": "medium",
            "decision_urgency": decision_urgency(top["priority"]),
            "decision_window": decision_window(top["priority"]),
            "expected_impact": expected_impact(top),
            "correlation": top["correlation"],
            "confidence": top["confidence"],
            "decision_score": top["decision_score"],
            "scenario_analysis": scenario_analysis(top),
            "secondary_risks": secondary_risks(top),
            "alerts": alerts,
            "district_ranking": ranking,
            "decision_trace": build_decision_trace(top),
            "system_impact": system_impact(top),
            "severity_breakdown": severity_breakdown(top),
            "intervention_effectiveness_score": intervention_effectiveness_score(top),
            "cascade_effects": secondary_risks(top),
        }

    return {
        "executive_summary": "City conditions are stable across monitored districts.",
        "what_is_happening": "City conditions are stable.",
        "criticality": "Low criticality. No urgent intervention is required.",
        "recommended_actions": ["Continue monitoring"],
        "structured_actions": [],
        "top_risks": [],
        "root_cause": [],
        "forecast": "Conditions are expected to remain stable in the next 1-2 hours.",
        "affected_districts": [],
        "top_critical_districts": [],
        "decision_priority": "low",
        "decision_urgency": "monitoring",
        "decision_window": "Safe to monitor for the next 2-4 hours",
        "expected_impact": "No immediate intervention required",
        "correlation": "No significant cross-domain stress detected.",
        "confidence": 0.95,
        "decision_score": 20.0,
        "scenario_analysis": {
            "without_action": "No significant deterioration is expected.",
            "with_action": "No immediate action is required."
        },
        "secondary_risks": [],
        "alerts": alerts,
        "district_ranking": ranking,
        "decision_trace": ["No critical anomalies detected", "System status classified as stable"],
        "system_impact": "localized",
        "severity_breakdown": {
            "transport": "stable",
            "environment": "stable"
        },
        "intervention_effectiveness_score": 0,
        "cascade_effects": [],
    }