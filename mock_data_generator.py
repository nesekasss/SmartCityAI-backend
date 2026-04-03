import json
import random
from datetime import datetime, timedelta

DISTRICTS = [
    "Medeu",
    "Bostandyk",
    "Almaly",
    "Auezov",
    "Turksib",
    "Nauryzbay",
]

def generate_current_data():
    data = []

    for district in DISTRICTS:
        if district == "Medeu":
            traffic_level = random.randint(8, 10)
            avg_speed = random.randint(10, 22)
            pm25 = random.randint(38, 60)
            co = round(random.uniform(1.4, 2.3), 2)
            accidents = random.randint(2, 4)
        elif district == "Turksib":
            traffic_level = random.randint(6, 8)
            avg_speed = random.randint(14, 28)
            pm25 = random.randint(22, 40)
            co = round(random.uniform(0.9, 1.7), 2)
            accidents = random.randint(1, 3)
        else:
            traffic_level = random.randint(3, 7)
            avg_speed = random.randint(22, 55)
            pm25 = random.randint(10, 35)
            co = round(random.uniform(0.3, 1.2), 2)
            accidents = random.randint(0, 3)

        data.append({
            "district": district,
            "traffic_level": traffic_level,
            "avg_speed": avg_speed,
            "accidents": accidents,
            "pm25": pm25,
            "co": co,
            "humidity": random.randint(30, 80),
            "temperature": random.randint(10, 35),
        })

    with open("data/city_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def generate_history_data():
    history = []
    now = datetime.now()

    for district in DISTRICTS:
        if district == "Medeu":
            base_traffic = 7
            base_speed = 26
            base_pm25 = 30
            base_co = 1.1
        elif district == "Turksib":
            base_traffic = 6
            base_speed = 28
            base_pm25 = 24
            base_co = 0.9
        else:
            base_traffic = random.randint(3, 6)
            base_speed = random.randint(28, 45)
            base_pm25 = random.randint(12, 24)
            base_co = round(random.uniform(0.4, 0.9), 2)

        for i in range(6):
            timestamp = (now - timedelta(hours=5 - i)).isoformat(timespec="minutes")

            if district == "Medeu":
                traffic_level = min(10, base_traffic + i // 2 + random.randint(0, 1))
                avg_speed = max(10, base_speed - i * 2 + random.randint(-1, 1))
                pm25 = min(65, base_pm25 + i * 3 + random.randint(0, 2))
                co = round(min(2.5, base_co + i * 0.12 + random.uniform(0, 0.08)), 2)
            else:
                traffic_level = max(1, min(10, base_traffic + random.randint(-1, 2)))
                avg_speed = max(10, base_speed + random.randint(-6, 4))
                pm25 = max(5, base_pm25 + random.randint(-3, 5))
                co = round(max(0.2, base_co + random.uniform(-0.15, 0.25)), 2)

            history.append({
                "timestamp": timestamp,
                "district": district,
                "traffic_level": traffic_level,
                "avg_speed": avg_speed,
                "accidents": random.randint(0, 4),
                "pm25": pm25,
                "co": co,
                "humidity": random.randint(30, 80),
                "temperature": random.randint(10, 35),
            })

    with open("data/city_history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    generate_current_data()
    generate_history_data()