from fetchers.fetch_last_8_years import fetch_last_8_years
from fetchers.fetch_last_12_months import fetch_last_12_months
from fetchers.fetch_last_4_quarters import fetch_last_4_quarters
from fetchers.fetch_last_12_weeks import fetch_last_12_weeks

dashboard_config = [
    # 1. Ерөнхий үзүүлэлтүүд
    {"topic": "General Indicators", "name": "GDP per Capita", "tbl_id": "DT_NSO_0500_010V1", "fetch_func": fetch_last_8_years},
    {"topic": "General Indicators", "name": "GDP by Sector", "tbl_id": "DT_NSO_0500_002V1", "fetch_func": fetch_last_8_years},
    {"topic": "General Indicators", "name": "National Income", "tbl_id": "DT_NSO_0500_009V1", "fetch_func": fetch_last_8_years},
    {"topic": "General Indicators", "name": "Exchange Rate", "tbl_id": "DT_NSO_0700_008V1", "fetch_func": fetch_last_12_months},
    {"topic": "General Indicators", "name": "Inflation Rate", "tbl_id": "DT_NSO_0600_004V1", "fetch_func": fetch_last_8_years},
    {"topic": "General Indicators", "name": "Unemployment Rate", "tbl_id": "DT_NSO_0400_049V1", "fetch_func": fetch_last_8_years},

    # 3. Гадаад худалдаа
    {"topic": "Foreign Trade", "name": "Total Trade/Import/Export", "tbl_id": "DT_NSO_1400_001V1", "fetch_func": fetch_last_8_years},
    {"topic": "Foreign Trade", "name": "Export by Product", "tbl_id": "DT_NSO_1400_006V2", "fetch_func": fetch_last_8_years},
    {"topic": "Foreign Trade", "name": "Import by Product", "tbl_id": "DT_NSO_1400_010V2", "fetch_func": fetch_last_8_years},
    {"topic": "Foreign Trade", "name": "Export by Country", "tbl_id": "DT_NSO_1400_006V3", "fetch_func": fetch_last_8_years},
    {"topic": "Foreign Trade", "name": "Import by Country", "tbl_id": "DT_NSO_1400_010V3", "fetch_func": fetch_last_8_years},

    # 4. Хэрэглээний үнэ
    {"topic": "Consumer Prices", "name": "Weekly Food & Fuel", "tbl_id": "DT_NSO_0600_001V4", "fetch_func": fetch_last_12_weeks},
    {"topic": "Consumer Prices", "name": "Avg Prices by Region", "tbl_id": "DT_NSO_0600_019V1", "fetch_func": fetch_last_12_months},
    {"topic": "Consumer Prices", "name": "Housing Price Change", "tbl_id": "DT_NSO_0300_00V1", "fetch_func": fetch_last_12_months},

    # 5. Улсын төсөв
    {"topic": "Government Budget", "name": "Balanced Budget", "tbl_id": "DT_NSO_0800_008V1", "fetch_func": fetch_last_12_months},
    {"topic": "Government Budget", "name": "Total Revenue", "tbl_id": "DT_NSO_0800_003V1", "fetch_func": fetch_last_8_years},
    {"topic": "Government Budget", "name": "Total Expenditure", "tbl_id": "DT_NSO_0800_006V1", "fetch_func": fetch_last_8_years},
    {"topic": "Government Budget", "name": "Government Debt", "tbl_id": "DT_NSO_0700_028V1", "fetch_func": fetch_last_4_quarters},
    {"topic": "Government Budget", "name": "Local Revenue", "tbl_id": "DT_NSO_0800_031V1", "fetch_func": fetch_last_8_years},
    {"topic": "Government Budget", "name": "Local Expenditure", "tbl_id": "DT_NSO_0800_029V1", "fetch_func": fetch_last_8_years},
    {"topic": "Government Budget", "name": "Local Support", "tbl_id": "DT_NSO_0800_011V1", "fetch_func": fetch_last_8_years},
    {"topic": "Government Budget", "name": "External Debt", "tbl_id": "DT_NSO_0700_028V3", "fetch_func": fetch_last_4_quarters},
    {"topic": "Government Budget", "name": "Debt Repayment", "tbl_id": "DT_NSO_0700_028V2", "fetch_func": fetch_last_4_quarters},
    {"topic": "Government Budget", "name": "Government Revenue/Expenditure/Balance", "tbl_id": "DT_NSO_0800_001V1", "fetch_func": fetch_last_8_years},

    # 6. Бүтээмж
    {"topic": "Productivity", "name": "Labor Productivity", "tbl_id": "DT_NSO_2500_001V2", "fetch_func": fetch_last_8_years},
    {"topic": "Productivity", "name": "GDP per Worker by Sector", "tbl_id": "DT_NSO_0500_010V2", "fetch_func": fetch_last_8_years},
    {"topic": "Productivity", "name": "GDP per Worker by Quarter", "tbl_id": "DT_NSO_0500_011V3", "fetch_func": fetch_last_4_quarters},

    # 7. Мөнгө, санхүү
    {"topic": "Finance", "name": "Bank Balance Sheet", "tbl_id": "DT_NSO_0700_010V1", "fetch_func": fetch_last_12_months},
    {"topic": "Finance", "name": "Exchange Rate", "tbl_id": "DT_NSO_0700_008V1", "fetch_func": fetch_last_12_months},  # reused
    {"topic": "Finance", "name": "Money Supply", "tbl_id": "DT_NSO_0700_001V2", "fetch_func": fetch_last_12_months},
    {"topic": "Finance", "name": "Main indicator of Stock Market", "tbl_id": "DT_NSO_0300_2024V01", "fetch_func": fetch_last_12_months},
    {"topic": "Finance", "name": "Loan Interest Rate", "tbl_id": "DT_NSO_0700_018V1", "fetch_func": fetch_last_12_months},
    {"topic": "Finance", "name": "Total Loan Balance", "tbl_id": "DT_NSO_0700_005V1", "fetch_func": fetch_last_8_years},
    {"topic": "Finance", "name": "NPL Balance", "tbl_id": "DT_NSO_0700_007V1", "fetch_func": fetch_last_8_years},
    {"topic": "Finance", "name": "NBFI Indicators", "tbl_id": "DT_NSO_0700_024V1", "fetch_func": fetch_last_4_quarters},

    # 8. Хөрөнгө оруулалт 
    {"topic": "Investment", "name": "Investment by Sector", "tbl_id": "DT_NSO_0901_002V1", "fetch_func": fetch_last_8_years},
    {"topic": "Investment", "name": "Investment by Source", "tbl_id": "DT_NSO_0901_001V1", "fetch_func": fetch_last_8_years},
    {"topic": "Investment", "name": "FDI Stock by Country", "tbl_id": "DT_NSO_1500_004V3", "fetch_func": fetch_last_8_years},
    {"topic": "Investment", "name": "FDI Inflow by Sector", "tbl_id": "DT_NSO_1500_005V4", "fetch_func": fetch_last_8_years},
    {"topic": "Investment", "name": "FDI Stock by Sector", "tbl_id": "DT_NSO_1500_005V3", "fetch_func": fetch_last_8_years},
    {"topic": "Investment", "name": "FDI Inflow by Country", "tbl_id": "DT_NSO_1500_004V4", "fetch_func": fetch_last_8_years},
    {"topic": "Investment", "name": "SBI by Aimag Capital", "tbl_id": "DT_NSO_0901_004V1", "fetch_func": fetch_last_8_years}
  
]
