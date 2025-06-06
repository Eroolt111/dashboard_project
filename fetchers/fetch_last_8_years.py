import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import time

def fetch_last_8_years(tbl_id, code_list=None, code1_list=None, code2_list=None):
    url = "https://opendata.1212.mn/api/Data?type=json"
    headers = {"Content-Type": "application/json"}

    # First fetch to get all available periods
    payload = {"tbl_id": tbl_id}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"❌ Error: HTTP {response.status_code}")
        return []

    records = response.json().get("DataList", [])
    # Extract all unique years from periods that are digits and at least 4 chars
    years_available = sorted({
        item["Period"][:4]
        for item in records
        if "Period" in item and item["Period"].isdigit() and len(item["Period"]) == 4
    })

    if not years_available:
        print("⚠️ No valid years found in periods.")
        return []

    # Select last 8 years (or fewer if not enough)
    latest_year = int(years_available[-1])
    selected_years = [str(y) for y in range(latest_year - 7, latest_year + 1) if str(y) in years_available]

    # Build refined payload with just years as Period
    refined_payload = {
        "tbl_id": tbl_id,
        "Period": selected_years,
    }

    # Handle code filters if present
    if code_list:
        if not isinstance(code_list[0], list):  # convert flat list into nested list
            code_list = [code_list]

        if len(code_list) > 0:
            refined_payload["CODE"] = code_list[0]
        if len(code_list) > 1:
            refined_payload["CODE1"] = code_list[1]
        if len(code_list) > 2:
            refined_payload["CODE2"] = code_list[2]

    # Second request with filtered years
    refined_response = requests.post(url, headers=headers, json=refined_payload)
    if refined_response.status_code != 200:
        print(f"❌ Error in refined request: HTTP {refined_response.status_code}")
        return []

    filtered_records = refined_response.json().get("DataList", [])
    print(f"✅ Found {len(filtered_records)} records from {selected_years[0]}–{selected_years[-1]}")
    return filtered_records
