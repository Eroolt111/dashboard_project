from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import time

def fetch_last_12_months(tbl_id, code_list=None):
    url = "https://opendata.1212.mn/api/Data?type=json"
    headers = {"Content-Type": "application/json"}
    payload = {"tbl_id": tbl_id}

    # Initial fetch to get available periods
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"❌ Error: HTTP {response.status_code}")
        return []

    data = response.json()
    records = data.get("DataList", [])
    if not records:
        print("⚠️ No 'DataList' found in response.")
        return []

    # Extract all valid YYYYMM periods
    periods = set()
    for item in records:
        period_str = item.get("Period", "")
        if len(period_str) == 6 and period_str.isdigit():
            try:
                dt = datetime.strptime(period_str, "%Y%m")
                periods.add(dt)
            except:
                continue

    if not periods:
        print("⚠️ No valid 'YYYYMM' Periods found in data.")
        return []

    # Get the latest date and compute the last 12 months
    latest_period = max(periods)
    last_12_months = [
        (latest_period - relativedelta(months=i)).strftime("%Y%m")
        for i in range(12)
    ]
    last_12_months = sorted(last_12_months)  # ascending order

    # Refined payload with correct CODE filters
    refined_payload = {
        "tbl_id": tbl_id,
        "Period": last_12_months
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

    print(f"✅ Found {len(filtered_records)} records for months {last_12_months[0]} to {last_12_months[-1]}")
    return filtered_records
