def generate_actions(district):
    actions = []

    traffic = district["transport"]["traffic_level"]
    avg_speed = district["transport"]["avg_speed"]
    pm25 = district["environment"]["pm25"]
    co = district["environment"]["co"]

    if traffic >= 8:
        actions.append("Adjust traffic light timing on overloaded corridors")
    if avg_speed < 20:
        actions.append("Dispatch traffic control support and optimize route flow")
    if pm25 > 35:
        actions.append("Issue air quality warning for the affected district")
    if co > 1.5:
        actions.append("Temporarily limit high-emission traffic in critical zones")
    if traffic >= 8 and pm25 > 35:
        actions.append("Increase public transport capacity to reduce private vehicle load")

    if not actions:
        actions.append("Continue monitoring and maintain current operational mode")

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

def decision_urgency(priority):
    if priority == "high":
        return "immediate"
    if priority == "medium":
        return "planned"
    return "monitoring"

def generate_ai_report(districts):
    high_priority = [d for d in districts if d["priority"] == "high"]
    medium_priority = [d for d in districts if d["priority"] == "medium"]

    if high_priority:
        top = sorted(high_priority, key=lambda x: x["risk_score"], reverse=True)[0]
        affected_districts = [d["name"] for d in high_priority]

        return {
            "what_is_happening": (
                f"Critical cross-domain stress detected in {top['name']} district. "
                f"Transport congestion and environmental indicators are simultaneously above safe operational thresholds."
            ),
            "criticality": (
                f"High criticality. Risk score is {top['risk_score']}. "
                f"Immediate intervention is recommended due to combined transport and ecological degradation."
            ),
            "recommended_actions": generate_actions(top),
            "explanation": top["anomaly_reasons"],
            "forecast": top["forecast"]["forecast_summary"],
            "affected_districts": affected_districts,
            "decision_priority": "high",
            "decision_urgency": decision_urgency(top["priority"]),
            "top_risks": extract_top_risks(top),
            "root_cause": root_cause_analysis(top),
        }

    if medium_priority:
        top = sorted(medium_priority, key=lambda x: x["risk_score"], reverse=True)[0]
        affected_districts = [d["name"] for d in medium_priority]

        return {
            "what_is_happening": (
                f"Moderate operational pressure detected in {top['name']} district. "
                f"Some transport or environmental indicators are approaching warning thresholds."
            ),
            "criticality": (
                f"Medium criticality. Risk score is {top['risk_score']}. "
                f"Preventive action is recommended to avoid escalation."
            ),
            "recommended_actions": generate_actions(top),
            "explanation": top["anomaly_reasons"],
            "forecast": top["forecast"]["forecast_summary"],
            "affected_districts": affected_districts,
            "decision_priority": "medium",
            "decision_urgency": decision_urgency(top["priority"]),
            "top_risks": extract_top_risks(top),
            "root_cause": root_cause_analysis(top),
        }

    return {
        "what_is_happening": "City conditions are stable across monitored districts.",
        "criticality": "Low criticality. No urgent intervention is required.",
        "recommended_actions": ["Continue monitoring city indicators"],
        "explanation": ["No critical anomalies detected"],
        "forecast": "Conditions are expected to remain stable in the next 1-2 hours.",
        "affected_districts": [],
        "decision_priority": "low",
        "decision_urgency": "monitoring",
        "top_risks": [],
        "root_cause": [],
    }