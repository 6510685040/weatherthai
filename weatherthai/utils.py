from collections import defaultdict


def summarize_daily_forecast(data: dict, days: int):
    """สรุป JSON จาก /forecast เป็นข้อความรายวัน"""
    grouped = defaultdict(list)

    for entry in data.get("list", []):
        dt_txt = entry.get("dt_txt", "")
        if " " not in dt_txt:
            continue

        date = dt_txt.split(" ")[0]
        main = entry.get("main", {})
        weather_list = entry.get("weather", [])

        temp = main.get("temp")
        if temp is None:
            continue

        desc = weather_list[0].get("description") if weather_list else "ไม่ทราบสภาพอากาศ"

        grouped[date].append((temp, desc))

    result_lines = []
    count = 0

    for date, items in grouped.items():
        if count >= days:
            break

        temps = [t for t, _ in items]
        descs = [d for _, d in items]

        main_desc = max(set(descs), key=descs.count) if descs else "ไม่ทราบสภาพอากาศ"

        high = max(temps) if temps else "?"
        low = min(temps) if temps else "?"

        result_lines.append(f"{date}: สูงสุด {high}°C / ต่ำสุด {low}°C - {main_desc}")
        count += 1

    return result_lines
