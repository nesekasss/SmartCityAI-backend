def forecast_district(district_data):
    traffic = district_data["traffic_level"]
    pm25 = district_data["pm25"]
    co = district_data["co"]

    predicted_traffic_level_2h = min(10, traffic + 1) if traffic >= 6 else traffic
    predicted_pm25_2h = pm25 + 5 if pm25 >= 20 else pm25 + 2
    predicted_co_2h = round(co + 0.2, 2) if co >= 1.0 else round(co + 0.05, 2)

    if traffic >= 8 or pm25 > 35 or co > 1.5:
        forecast_summary = "Conditions are likely to worsen in the next 1-2 hours."
        trend = "negative"
    elif traffic >= 5 or pm25 > 20 or co > 1.0:
        forecast_summary = "Moderate deterioration is possible in the next 1-2 hours."
        trend = "warning"
    else:
        forecast_summary = "Conditions are expected to remain stable."
        trend = "stable"

    return {
        "predicted_traffic_level_2h": predicted_traffic_level_2h,
        "predicted_pm25_2h": predicted_pm25_2h,
        "predicted_co_2h": predicted_co_2h,
        "forecast_summary": forecast_summary,
        "trend": trend,
    }