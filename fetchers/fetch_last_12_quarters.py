from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests
import json
import pandas as pd
from datetime import datetime, timedelta

def fetch_last_12_quarters(tbl_id, code_list=None):
    url = "https://opendata.1212.mn/api/Data?type=json"
    headers = {"Content-Type": "application/json"}
    payload = {"tbl_id": tbl_id}

    # First request to get all available periods
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"❌ Error: HTTP {response.status_code}")
        return []

    data = response.json()
    records = data.get("DataList", [])
    if not records:
        print("⚠️ No 'DataList' found in response.")
        return []

    # Extract unique quarterly periods: "YYYYQQ"
    periods = set()
    for item in records:
        period_str = item.get("Period", "")
        if len(period_str) == 6 and period_str.isdigit():
            year = int(period_str[:4])
            quarter = int(period_str[4:])
            if 1 <= quarter <= 4:
                periods.add((year, quarter))

    if not periods:
        print("⚠️ No valid quarterly periods found.")
        return []

    # Sort by most recent, get last 4
    sorted_periods = sorted(periods, reverse=True)
    last_12 = sorted_periods[:12]
    last_12_sorted = sorted(last_12)  # ascending for API call

    # Convert to string format: "YYYYQQ"
    last_12_str = [f"{y}{q:02d}" for (y, q) in last_12_sorted]

    # Build refined payload
    refined_payload = {
        "tbl_id": tbl_id,
        "Period": last_12_str
    }

    if code_list:
        if len(code_list) > 0:
            refined_payload["CODE"] = code_list[0] if isinstance(code_list[0], list) else [code_list[0]]
        if len(code_list) > 1:
            refined_payload["CODE1"] = code_list[1] if isinstance(code_list[1], list) else [code_list[1]]
        if len(code_list) > 2:
            refined_payload["CODE2"] = code_list[2] if isinstance(code_list[2], list) else [code_list[2]]

    # request
    refined_response = requests.post(url, headers=headers, json=refined_payload)
    if refined_response.status_code != 200:
        print(f"❌ Error in refined request: HTTP {refined_response.status_code}")
        return []

    refined_data = refined_response.json()
    filtered_records = refined_data.get("DataList", [])

    print(f"✅ Found {len(filtered_records)} records for quarters: {', '.join(last_12_str)}")
    return filtered_records


