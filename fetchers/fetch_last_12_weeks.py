from datetime import datetime
import requests
from dateutil.relativedelta import relativedelta

def fetch_last_12_weeks(tbl_id, code_list=None):
    url = "https://opendata.1212.mn/api/Data?type=json"
    headers = {"Content-Type": "application/json"}
    payload = {"tbl_id": tbl_id}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"❌ Error: HTTP {response.status_code}")
        return []

    data = response.json()
    records = data.get("DataList", [])
    if not records:
        print("⚠️ No 'DataList' found in response.")
        return []

    # Extract weekly periods in format "YYYYMMDD"
    week_dates = []
    for item in records:
        period_str = item.get("Period", "")
        try:
            period_dt = datetime.strptime(period_str, "%Y%m%d")
            week_dates.append(period_dt)
        except ValueError:
            continue

    if not week_dates:
        print("⚠️ No valid weekly date periods found.")
        return []

    sorted_weeks = sorted(set(week_dates), reverse=True)
    last_12_weeks = sorted(sorted_weeks[:12])  # ascending for API

    last_12_periods = [dt.strftime("%Y%m%d") for dt in last_12_weeks]

    refined_payload = {
        "tbl_id": tbl_id,
        "Period": last_12_periods
    }

    if code_list:
        if len(code_list) > 0:
            refined_payload["CODE"] = code_list[0] if isinstance(code_list[0], list) else [code_list[0]]
        if len(code_list) > 1:
            refined_payload["CODE1"] = code_list[1] if isinstance(code_list[1], list) else [code_list[1]]
        if len(code_list) > 2:
            refined_payload["CODE2"] = code_list[2] if isinstance(code_list[2], list) else [code_list[2]]

    # Request
    refined_response = requests.post(url, headers=headers, json=refined_payload)
    if refined_response.status_code != 200:
        print(f"❌ Error in refined request: HTTP {refined_response.status_code}")
        return []

    refined_data = refined_response.json()
    filtered_records = refined_data.get("DataList", [])

    print(f"✅ Found {len(filtered_records)} records for weeks: {', '.join(last_12_periods)}")
    return filtered_records
