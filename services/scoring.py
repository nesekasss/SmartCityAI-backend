def calculate_transport_score(traffic_level, avg_speed, accidents):
    score = 0

    score += traffic_level * 6

    if avg_speed < 20:
        score += 25
    elif avg_speed < 30:
        score += 15
    elif avg_speed < 40:
        score += 8

    score += accidents * 5

    return min(score, 100)

def calculate_environment_score(pm25, co):
    score = 0

    if pm25 > 35:
        score += 40
    elif pm25 > 20:
        score += 25
    elif pm25 > 12:
        score += 10

    if co > 1.5:
        score += 35
    elif co > 1.0:
        score += 20
    elif co > 0.6:
        score += 10

    return min(score, 100)

def calculate_total_risk(transport_score, environment_score):
    total = 0.55 * transport_score + 0.45 * environment_score
    return round(min(total, 100), 1)

def risk_to_priority(risk_score):
    if risk_score >= 70:
        return "high", "red"
    if risk_score >= 40:
        return "medium", "yellow"
    return "low", "green"