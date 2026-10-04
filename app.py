# ============================================================
#  🍪 KEVIN'S COOKIE COMPANY — WOODEN DASHBOARD  (app.py)
#  Run with:  streamlit run app.py
#  Needs:     pip install streamlit pandas numpy plotly
#  The CSV data is built INTO this file — nothing to upload.
#  (Optional: use the sidebar uploader to swap in another CSV
#   with the same columns.)
# ============================================================
import io
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Kevin's Cookie Company", page_icon="🍪", layout="wide")

# ---------------------- EMBEDDED CSV DATA ----------------------
RAW_CSV = """Order ID,Customer ID,Order Date,Cookies Shipped,Revenue,Rush Shipment
ORD-0001,CUST-019,2025-02-27,112,4542.45,Yes
ORD-0002,CUST-041,2025-01-21,445,1284,Yes
ORD-0003,CUST-040,2025-04-26,870,2081.4,Yes
ORD-0004,CUST-024,2025-01-19,280,3789.98,Yes
ORD-0005,CUST-037,2025-05-14,116,1182.55,No
ORD-0006,CUST-013,2025-04-04,81,431.05,Yes
ORD-0007,CUST-046,2025-01-24,710,1484.27,Yes
ORD-0008,CUST-005,2025-04-29,30,848.05,No
ORD-0009,CUST-003,2025-05-02,624,4652,No
ORD-0010,CUST-043,2025-03-13,131,4050.2,Yes
ORD-0011,CUST-015,2025-03-06,476,3185.35,Yes
ORD-0012,CUST-050,2025-04-02,224,4363.73,No
ORD-0013,CUST-019,2025-01-17,340,4028.18,Yes
ORD-0014,CUST-006,2025-01-24,468,973.52,No
ORD-0015,CUST-015,2025-02-25,97,4468.17,No
ORD-0016,CUST-007,2024-12-17,382,2719.74,Yes
ORD-0017,CUST-025,2025-04-19,109,4046.83,Yes
ORD-0018,CUST-018,2025-01-26,881,4485.65,Yes
ORD-0019,CUST-030,2025-01-16,673,1624.12,No
ORD-0020,CUST-041,2025-01-23,140,594.76,No
ORD-0021,CUST-024,2025-02-05,671,1178.28,No
ORD-0022,CUST-011,2025-02-02,318,2164.18,No
ORD-0023,CUST-024,2025-05-24,779,4099.17,No
ORD-0024,CUST-023,2025-03-16,353,4310.62,Yes
ORD-0025,CUST-014,2024-12-17,501,84.41,Yes
ORD-0026,CUST-043,2024-12-28,423,2578.2,Yes
ORD-0027,CUST-018,2024-12-31,815,2116.18,No
ORD-0028,CUST-045,2025-01-15,395,1149.43,No
ORD-0029,CUST-044,2025-02-14,201,643.33,Yes
ORD-0030,CUST-042,2025-04-15,965,1721.2,Yes
ORD-0031,CUST-005,2024-12-31,286,4717.4,Yes
ORD-0032,CUST-039,2025-04-18,170,1649.85,Yes
ORD-0033,CUST-041,2025-01-12,469,2618.01,No
ORD-0034,CUST-011,2024-12-14,323,3529.94,Yes
ORD-0035,CUST-035,2025-02-20,31,1849.97,No
ORD-0036,CUST-047,2025-02-19,262,4860.32,Yes
ORD-0037,CUST-016,2025-02-04,757,4814.11,No
ORD-0038,CUST-011,2025-03-17,866,1296.32,No
ORD-0039,CUST-030,2025-03-02,570,2511.38,Yes
ORD-0040,CUST-025,2025-02-20,484,1539.35,Yes
ORD-0041,CUST-018,2024-12-14,68,1459.96,No
ORD-0042,CUST-041,2025-01-11,520,232.59,Yes
ORD-0043,CUST-045,2025-05-12,691,3067.34,Yes
ORD-0044,CUST-036,2025-02-21,485,2538.26,Yes
ORD-0045,CUST-015,2025-02-15,709,304.82,Yes
ORD-0046,CUST-044,2025-05-26,985,1429.3,Yes
ORD-0047,CUST-021,2025-04-30,792,4545.92,Yes
ORD-0048,CUST-050,2025-03-25,199,1235.83,No
ORD-0049,CUST-050,2025-04-16,967,767.23,No
ORD-0050,CUST-004,2024-12-05,696,2472.79,No
ORD-0051,CUST-015,2025-05-17,967,4928.97,Yes
ORD-0052,CUST-003,2025-05-22,572,1248.17,No
ORD-0053,CUST-021,2025-04-29,885,3377.07,Yes
ORD-0054,CUST-026,2025-03-23,576,3820.02,Yes
ORD-0055,CUST-018,2025-02-13,253,1226.31,No
ORD-0056,CUST-005,2025-03-04,841,3654.67,Yes
ORD-0057,CUST-014,2024-12-03,514,1870.53,No
ORD-0058,CUST-037,2025-02-08,140,3179.91,No
ORD-0059,CUST-046,2025-01-28,494,3185.97,No
ORD-0060,CUST-021,2025-04-27,828,2702.08,No
ORD-0061,CUST-014,2025-02-15,656,496.93,No
ORD-0062,CUST-042,2025-05-16,30,4184.75,No
ORD-0063,CUST-032,2025-05-24,850,1637.86,Yes
ORD-0064,CUST-026,2025-05-13,176,973.27,Yes
ORD-0065,CUST-042,2025-02-21,283,251.84,No
ORD-0066,CUST-030,2025-03-16,397,2974.92,Yes
ORD-0067,CUST-010,2025-04-26,610,3403.94,Yes
ORD-0068,CUST-017,2025-04-23,325,132.11,Yes
ORD-0069,CUST-009,2025-03-18,23,2584.86,No
ORD-0070,CUST-016,2025-05-06,251,1171.15,Yes
ORD-0071,CUST-048,2025-03-29,786,3243.61,Yes
ORD-0072,CUST-036,2025-05-25,355,913.11,No
ORD-0073,CUST-035,2025-01-13,574,3470.14,Yes
ORD-0074,CUST-017,2025-03-06,907,1964.34,Yes
ORD-0075,CUST-048,2025-01-13,349,4686.81,Yes
ORD-0076,CUST-038,2025-01-23,101,730.73,Yes
ORD-0077,CUST-028,2025-02-24,376,1738.28,Yes
ORD-0078,CUST-038,2025-03-06,965,611.69,Yes
ORD-0079,CUST-026,2024-12-07,464,4627.23,Yes
ORD-0080,CUST-024,2025-02-15,437,4392.83,No
ORD-0081,CUST-015,2025-02-05,518,1326.81,Yes
ORD-0082,CUST-009,2025-04-10,785,3316.92,Yes
ORD-0083,CUST-033,2025-04-12,952,4095.25,Yes
ORD-0084,CUST-032,2025-05-05,44,2798.24,Yes
ORD-0085,CUST-006,2025-02-18,215,2671.77,No
ORD-0086,CUST-049,2025-04-21,90,1247.17,No
ORD-0087,CUST-004,2025-01-03,941,510.86,No
ORD-0088,CUST-008,2025-05-14,571,4491.22,Yes
ORD-0089,CUST-010,2025-03-02,881,4507.07,No
ORD-0090,CUST-041,2025-05-29,397,3183.85,Yes
ORD-0091,CUST-011,2024-12-26,11,1728.2,No
ORD-0092,CUST-044,2025-04-01,399,1778.59,No
ORD-0093,CUST-028,2025-03-15,575,3643.48,Yes
ORD-0094,CUST-039,2024-12-07,115,4490.7,No
ORD-0095,CUST-005,2025-05-27,781,4441.08,No
ORD-0096,CUST-025,2025-02-16,831,3910.38,No
ORD-0097,CUST-025,2025-03-26,486,3228.06,Yes
ORD-0098,CUST-039,2025-03-21,712,466.49,Yes
ORD-0099,CUST-030,2025-04-09,411,850.06,No
ORD-0100,CUST-034,2024-12-07,739,4497.84,Yes
ORD-0101,CUST-017,2024-12-18,565,3051.82,Yes
ORD-0102,CUST-036,2025-04-05,171,95.53,Yes
ORD-0103,CUST-001,2025-02-23,211,552.28,No
ORD-0104,CUST-044,2024-12-28,967,3334.33,Yes
ORD-0105,CUST-047,2025-05-19,279,75.05,No
ORD-0106,CUST-008,2025-03-01,872,846,Yes
ORD-0107,CUST-044,2025-01-06,825,2766.23,Yes
ORD-0108,CUST-035,2024-12-11,280,3474.88,No
ORD-0109,CUST-049,2025-01-21,465,3277.21,No
ORD-0110,CUST-018,2025-02-13,471,1160.13,Yes
ORD-0111,CUST-050,2025-02-03,736,3575.29,No
ORD-0112,CUST-042,2025-01-12,261,1224.38,No
ORD-0113,CUST-022,2025-02-28,711,1660.73,Yes
ORD-0114,CUST-008,2025-02-03,305,3745.13,No
ORD-0115,CUST-019,2025-02-05,734,3265.68,Yes
ORD-0116,CUST-028,2025-04-28,729,4253.66,Yes
ORD-0117,CUST-011,2025-05-21,758,3305.18,No
ORD-0118,CUST-030,2025-02-13,347,2863.13,Yes
ORD-0119,CUST-001,2025-01-25,888,513.69,Yes
ORD-0120,CUST-047,2025-04-27,62,1870.19,Yes
ORD-0121,CUST-047,2025-05-12,801,1362.75,No
ORD-0122,CUST-017,2025-02-21,931,1257.75,No
ORD-0123,CUST-033,2025-01-19,226,4866.4,Yes
ORD-0124,CUST-049,2025-05-13,773,1995.83,No
ORD-0125,CUST-012,2024-12-17,197,4465.63,Yes
ORD-0126,CUST-033,2025-03-03,389,3174.14,No
ORD-0127,CUST-007,2024-12-05,502,3984.32,No
ORD-0128,CUST-041,2025-04-26,50,2538.05,No
ORD-0129,CUST-020,2025-03-16,166,2905.67,Yes
ORD-0130,CUST-041,2024-12-12,24,2487.96,Yes
ORD-0131,CUST-033,2025-02-07,822,1016.45,No
ORD-0132,CUST-039,2025-01-14,74,3626.14,No
ORD-0133,CUST-013,2025-04-07,866,1439.82,Yes
ORD-0134,CUST-010,2024-12-15,848,170.36,Yes
ORD-0135,CUST-024,2025-05-02,530,3245.09,No
ORD-0136,CUST-049,2025-04-07,353,926.7,Yes
ORD-0137,CUST-011,2024-12-09,138,4705.27,No
ORD-0138,CUST-035,2025-04-27,657,4771.95,Yes
ORD-0139,CUST-050,2024-12-08,481,4578.58,No
ORD-0140,CUST-034,2025-01-19,72,1882.29,No
ORD-0141,CUST-001,2025-01-09,148,126.51,Yes
ORD-0142,CUST-039,2025-05-13,508,4645.18,Yes
ORD-0143,CUST-021,2024-12-05,602,2169.51,Yes
ORD-0144,CUST-032,2025-04-01,401,4834.94,Yes
ORD-0145,CUST-002,2024-12-31,684,4819.92,Yes
ORD-0146,CUST-008,2025-01-17,428,4272.4,No
ORD-0147,CUST-024,2024-12-26,298,1507.52,Yes
ORD-0148,CUST-020,2025-03-03,388,1956.23,No
ORD-0149,CUST-016,2025-04-10,782,4263.13,Yes
ORD-0150,CUST-004,2024-12-24,499,1618.76,Yes
ORD-0151,CUST-016,2025-03-21,240,888.99,No
ORD-0152,CUST-037,2025-01-13,50,2806.17,No
ORD-0153,CUST-006,2025-03-02,37,4683.97,Yes
ORD-0154,CUST-006,2025-04-16,144,3495.35,No
ORD-0155,CUST-047,2025-01-20,210,2871.8,Yes
ORD-0156,CUST-032,2025-04-29,849,531.02,Yes
ORD-0157,CUST-005,2025-02-11,789,3094.29,Yes
ORD-0158,CUST-049,2025-01-03,939,4950.77,No
ORD-0159,CUST-035,2025-03-29,42,743.42,No
ORD-0160,CUST-050,2025-03-29,57,2615.73,Yes
ORD-0161,CUST-009,2025-04-26,512,4393,Yes
ORD-0162,CUST-009,2025-04-20,416,3716.8,Yes
ORD-0163,CUST-043,2024-12-24,583,3500.23,Yes
ORD-0164,CUST-031,2025-05-02,737,3527.3,No
ORD-0165,CUST-036,2025-05-10,814,1829.48,Yes
ORD-0166,CUST-011,2025-01-02,108,1503.28,Yes
ORD-0167,CUST-017,2025-01-31,693,4056.34,No
ORD-0168,CUST-034,2024-12-22,881,4060.06,No
ORD-0169,CUST-039,2025-03-24,735,4342.01,Yes
ORD-0170,CUST-028,2024-12-06,996,4570.54,No
ORD-0171,CUST-014,2025-05-31,556,2581.14,Yes
ORD-0172,CUST-035,2025-01-31,970,2532.51,Yes
ORD-0173,CUST-049,2025-03-23,748,4001.56,No
ORD-0174,CUST-047,2025-04-12,622,3267.32,Yes
ORD-0175,CUST-045,2025-05-27,952,3524.74,No
ORD-0176,CUST-013,2025-02-12,471,3989.17,Yes
ORD-0177,CUST-046,2025-02-17,652,4455.53,Yes
ORD-0178,CUST-020,2025-06-02,778,1723.08,No
ORD-0179,CUST-026,2025-04-19,14,1909.14,No
ORD-0180,CUST-043,2025-01-09,227,515.21,No
ORD-0181,CUST-042,2024-12-16,512,2912.49,Yes
ORD-0182,CUST-024,2025-03-26,776,227.91,Yes
ORD-0183,CUST-029,2025-04-15,407,2354.71,Yes
ORD-0184,CUST-034,2025-05-12,880,2736.09,Yes
ORD-0185,CUST-029,2025-04-02,804,1468.38,No
ORD-0186,CUST-008,2025-01-18,402,2974.62,No
ORD-0187,CUST-016,2024-12-21,216,200.98,No
ORD-0188,CUST-015,2025-04-16,24,234.87,Yes
ORD-0189,CUST-005,2025-05-01,867,4121.87,No
ORD-0190,CUST-022,2025-01-29,563,1832.94,No
ORD-0191,CUST-002,2025-05-16,901,678.95,No
ORD-0192,CUST-038,2025-04-13,470,2635.1,No
ORD-0193,CUST-036,2025-03-28,700,3861.47,Yes
ORD-0194,CUST-015,2025-05-07,584,1118.31,Yes
ORD-0195,CUST-038,2024-12-25,873,3133.31,No
ORD-0196,CUST-015,2025-05-05,752,472.47,Yes
ORD-0197,CUST-001,2025-03-21,250,305.82,No
ORD-0198,CUST-005,2025-05-02,573,2680.21,Yes
ORD-0199,CUST-046,2024-12-09,105,2726.14,Yes
ORD-0200,CUST-041,2025-02-07,909,3205.28,No"""

# ---------------------- WOOD THEME (CSS) ----------------------
INK = "#3b2412"
PALETTE = ["#8B5A2B", "#C68E4E", "#5C3A1E", "#E0A458", "#A0522D", "#D2A56B", "#6F4E37"]

GRAIN = ("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='900' height='700'%3E"
         "%3Cfilter id='w'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.003 0.08' numOctaves='5' seed='11'/%3E"
         "%3CfeColorMatrix values='0 0 0 0 0.30  0 0 0 0 0.16  0 0 0 0 0.05  2.4 0 0 0 -0.75'/%3E%3C/filter%3E"
         "%3Crect width='100%25' height='100%25' filter='url(%23w)'/%3E%3C/svg%3E")

CSS = """
<style>
.stApp {
  background-color: #c68e4e;
  background-image:
    repeating-linear-gradient(90deg, rgba(0,0,0,0) 0px, rgba(0,0,0,0) 300px, rgba(50,25,8,.45) 300px, rgba(50,25,8,.45) 303px),
    url("__GRAIN__"),
    linear-gradient(180deg, #d9a566 0%, #c68e4e 50%, #b87d3f 100%);
  background-attachment: fixed;
}
header[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 1.2rem; max-width: 1400px; }

/* sidebar = dark walnut */
section[data-testid="stSidebar"] {
  background-color: #4a2c14;
  background-image:
    repeating-linear-gradient(90deg, rgba(0,0,0,0) 0px, rgba(0,0,0,0) 120px, rgba(20,8,0,.5) 120px, rgba(20,8,0,.5) 123px),
    url("__GRAIN__");
  border-right: 4px solid #2b1608;
}
section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] small { color: #f6e3c0 !important; }
section[data-testid="stSidebar"] [data-baseweb="select"] span,
section[data-testid="stSidebar"] input { color: #2b1608 !important; }

/* hero banner */
.hero {
  background-color: #3a1f0d;
  background-image: repeating-linear-gradient(0deg, rgba(255,200,120,.07) 0px, rgba(255,200,120,.07) 2px, rgba(0,0,0,0) 2px, rgba(0,0,0,0) 7px),
                    url("__GRAIN__");
  border: 3px solid #24120a; border-radius: 16px; padding: 18px 26px; margin-bottom: 16px;
  box-shadow: 0 6px 14px rgba(0,0,0,.45), inset 0 0 25px rgba(0,0,0,.5);
}
.hero h1 { color: #f8e2b8; margin: 0; font-family: Georgia, serif; font-size: 2.1rem; }
.hero p { color: #e2b97a; margin: 4px 0 0 0; font-family: Georgia, serif; }

/* time cards (past / present / future) */
.tcard { border-radius: 14px; padding: 14px 18px; color: #fdf1d8; border: 3px solid #24120a;
  box-shadow: 0 5px 12px rgba(0,0,0,.4); min-height: 138px; }
.t-past    { background: linear-gradient(135deg, #6b4423, #4a2c14); }
.t-present { background: linear-gradient(135deg, #b5651d, #8b4513); }
.t-future  { background: linear-gradient(135deg, #d9a441, #a97420); color:#2b1608; }
.tcard .tt { font-size: .85rem; letter-spacing: .12em; text-transform: uppercase; opacity: .85; }
.tcard .tv { font-size: 2rem; font-weight: 700; font-family: Georgia, serif; }
.tcard .ts { font-size: .85rem; opacity: .9; }

/* KPI cards */
.kpi { background: rgba(251,240,218,.94); border: 2px solid #5c3a1e; border-left: 8px solid #8b5a2b;
  border-radius: 12px; padding: 10px 14px; margin-bottom: 10px; box-shadow: 0 3px 8px rgba(0,0,0,.3); }
.kpi .kl { color: #6f4e37; font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; }
.kpi .kv { color: #3b2412; font-size: 1.65rem; font-weight: 700; font-family: Georgia, serif; }
.kpi .kd { font-size: .8rem; font-weight: 600; }
.kpi .up { color: #2e6b2e; } .kpi .down { color: #a32a1a; }
.kpi .ks { color: #8a6a4a; font-size: .75rem; }

/* tabs */
.stTabs [data-baseweb="tab-list"] { gap: 6px; background: rgba(40,20,8,.55); padding: 6px; border-radius: 12px; }
.stTabs [data-baseweb="tab"] { background: rgba(251,240,218,.18); border-radius: 8px; padding: 8px 18px; }
.stTabs [data-baseweb="tab"] p { color: #f6e3c0 !important; font-weight: 600; }
.stTabs [aria-selected="true"] { background: #f3d9a4 !important; }
.stTabs [aria-selected="true"] p { color: #3b2412 !important; }

/* chart + table cards */
div[data-testid="stPlotlyChart"], div[data-testid="stDataFrame"] {
  background: rgba(251,240,218,.93); border: 2px solid #5c3a1e; border-radius: 12px;
  padding: 6px; box-shadow: 0 3px 8px rgba(0,0,0,.3);
}
.sec { color: #fdf1d8; background: rgba(40,20,8,.7); display:inline-block; padding: 4px 14px;
  border-radius: 8px; font-family: Georgia, serif; font-size: 1.15rem; margin: 8px 0; }
.note { background: rgba(251,240,218,.9); color:#3b2412; border:2px dashed #5c3a1e; border-radius:10px; padding:10px 14px; }
</style>
""".replace("__GRAIN__", GRAIN)
st.markdown(CSS, unsafe_allow_html=True)

# ---------------------- HELPERS ----------------------
_counter = {"n": 0}

def show(fig):
    _counter["n"] += 1
    try:
        st.plotly_chart(fig, width="stretch", key=f"chart_{_counter['n']}")
    except Exception:
        st.plotly_chart(fig, use_container_width=True, key=f"chart_{_counter['n']}")

def show_table(d, **kw):
    try:
        st.dataframe(d, width="stretch", hide_index=True, **kw)
    except Exception:
        st.dataframe(d, use_container_width=True, hide_index=True, **kw)

def style(fig, h=360, title=None):
    fig.update_layout(
        height=h, title=dict(text=title, font=dict(size=16, color=INK)) if title else None,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=INK, family="Georgia, serif"), colorway=PALETTE,
        margin=dict(l=10, r=10, t=50 if title else 15, b=10),
        legend=dict(orientation="h", y=-0.18),
    )
    fig.update_xaxes(gridcolor="rgba(92,58,30,.18)", zeroline=False)
    fig.update_yaxes(gridcolor="rgba(92,58,30,.18)", zeroline=False)
    return fig

def money(x): return f"${x:,.0f}"
def num(x): return f"{x:,.0f}"

def pct_change(cur, prev):
    return None if (prev is None or prev == 0) else (cur - prev) / prev * 100

def kpi(label, value, delta=None, sub=""):
    d_html = ""
    if delta is not None:
        cls = "up" if delta >= 0 else "down"
        arrow = "▲" if delta >= 0 else "▼"
        d_html = f'<div class="kd {cls}">{arrow} {abs(delta):.1f}% vs prior</div>'
    return (f'<div class="kpi"><div class="kl">{label}</div><div class="kv">{value}</div>'
            f'{d_html}<div class="ks">{sub}</div></div>')

def summarize(d):
    orders = len(d)
    rev = d["Revenue"].sum()
    cookies = d["Cookies Shipped"].sum()
    return dict(
        rev=rev, cookies=cookies, orders=orders,
        aov=rev / orders if orders else 0,
        rush=(d["Rush Shipment"].eq("Yes").mean() * 100) if orders else 0,
        rpc=rev / cookies if cookies else 0,
    )

@st.cache_data
def load_df(raw_text):
    df = pd.read_csv(io.StringIO(raw_text))
    df.columns = [c.strip() for c in df.columns]
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Rush Shipment"] = df["Rush Shipment"].astype(str).str.strip().str.title()
    df["Revenue per Cookie"] = df["Revenue"] / df["Cookies Shipped"]
    return df.sort_values("Order Date").reset_index(drop=True)

def make_forecast(d, weeks, growth_pct):
    w = d.set_index("Order Date").resample("W-SUN")[["Revenue", "Cookies Shipped"]].sum().reset_index()
    if len(w) and (w["Order Date"].iloc[-1] - d["Order Date"].max()).days >= 3:
        w = w.iloc[:-1]                      # drop the incomplete last week
    if len(w) < 6:
        return None, None
    x = np.arange(len(w))
    out = pd.DataFrame({"Week Ending": pd.date_range(w["Order Date"].iloc[-1] + pd.Timedelta(weeks=1), periods=weeks, freq="W-SUN")})
    xf = np.arange(len(w), len(w) + weeks)
    for col, name in [("Revenue", "Revenue"), ("Cookies Shipped", "Cookies")]:
        slope, icpt = np.polyfit(x, w[col].values, 1)
        resid = w[col].values - (slope * x + icpt)
        sd = resid.std()
        pred = np.clip(slope * xf + icpt, 0, None) * (1 + growth_pct / 100)
        out[name] = pred
        out[name + " Low"] = np.clip(pred - 1.28 * sd, 0, None)
        out[name + " High"] = pred + 1.28 * sd
        w[name + " Trend"] = slope * x + icpt
    w = w.rename(columns={"Order Date": "Week Ending"})
    return w, out

# ---------------------- LOAD DATA ----------------------
st.sidebar.markdown("## 🪵 Control Panel")
up = st.sidebar.file_uploader("Optional: swap in another CSV", type="csv",
                              help="Leave empty to use the built-in Kevin Cookie Company data.")
try:
    raw = up.getvalue().decode("utf-8-sig") if up is not None else RAW_CSV
    df = load_df(raw)
except Exception as e:
    st.sidebar.error(f"Could not read that file ({e}). Using built-in data.")
    df = load_df(RAW_CSV)

# ---------------------- SIDEBAR FILTERS ----------------------
st.sidebar.markdown("### 🔎 Filters")
min_d, max_d = df["Order Date"].min().date(), df["Order Date"].max().date()
dr = st.sidebar.date_input("Date range", (min_d, max_d), min_value=min_d, max_value=max_d)
start, end = (dr[0], dr[1]) if isinstance(dr, (list, tuple)) and len(dr) == 2 else (min_d, max_d)

ship = st.sidebar.multiselect("Shipment type", ["Yes", "No"], default=["Yes", "No"],
                              format_func=lambda v: "🚚 Rush" if v == "Yes" else "📦 Standard")
custs = st.sidebar.multiselect("Customers (empty = all)", sorted(df["Customer ID"].unique()))
rmin, rmax = float(df["Revenue"].min()), float(df["Revenue"].max())
rev_rng = st.sidebar.slider("Revenue per order ($)", rmin, rmax, (rmin, rmax))
cmin, cmax = int(df["Cookies Shipped"].min()), int(df["Cookies Shipped"].max())
cook_rng = st.sidebar.slider("Cookies per order", cmin, cmax, (cmin, cmax))

st.sidebar.markdown("### ⏳ Time Settings")
win = st.sidebar.slider("Present window (days)", 7, 90, 30)
horizon = st.sidebar.slider("Future forecast (weeks)", 2, 26, 8)
growth = st.sidebar.slider("Growth scenario (%)", -30, 30, 0,
                           help="Adds an optimistic / pessimistic adjustment on top of the trend forecast.")

mask = (
    (df["Order Date"].dt.date >= start) & (df["Order Date"].dt.date <= end)
    & df["Rush Shipment"].isin(ship)
    & df["Revenue"].between(*rev_rng) & df["Cookies Shipped"].between(*cook_rng)
)
if custs:
    mask &= df["Customer ID"].isin(custs)
f = df[mask].copy()

st.markdown(
    '<div class="hero"><h1>🍪 Kevin\'s Cookie Company — Order Dashboard</h1>'
    '<p>Past • Present • Future  |  hand-crafted on a warm wooden bench</p></div>',
    unsafe_allow_html=True)

if f.empty:
    st.warning("No orders match these filters. Widen the filters in the sidebar.")
    st.stop()

# ---------------------- PAST / PRESENT WINDOWS ----------------------
last_day = f["Order Date"].max()
p_start = last_day - pd.Timedelta(days=win - 1)
prev_start = p_start - pd.Timedelta(days=win)
present = f[f["Order Date"] >= p_start]
prior = f[(f["Order Date"] >= prev_start) & (f["Order Date"] < p_start)]
past = f[f["Order Date"] < p_start]

S_pres, S_prior, S_past = summarize(present), summarize(prior), summarize(past)
hist, fut = make_forecast(f, horizon, growth)

# ---------------------- TOP STRIP: PAST | PRESENT | FUTURE ----------------------
c1, c2, c3 = st.columns(3)
with c1:
    rng = f"{past['Order Date'].min():%b %d, %Y} → {(p_start - pd.Timedelta(days=1)):%b %d, %Y}" if len(past) else "no earlier data"
    st.markdown(f'<div class="tcard t-past"><div class="tt">⏪ Past</div><div class="tv">{money(S_past["rev"])}</div>'
                f'<div class="ts">{num(S_past["orders"])} orders • {num(S_past["cookies"])} cookies</div>'
                f'<div class="ts">{rng}</div></div>', unsafe_allow_html=True)
with c2:
    d = pct_change(S_pres["rev"], S_prior["rev"])
    dtxt = "" if d is None else f' • {"▲" if d >= 0 else "▼"} {abs(d):.1f}% vs previous {win} days'
    st.markdown(f'<div class="tcard t-present"><div class="tt">📍 Present (last {win} days)</div><div class="tv">{money(S_pres["rev"])}</div>'
                f'<div class="ts">{num(S_pres["orders"])} orders • {num(S_pres["cookies"])} cookies</div>'
                f'<div class="ts">{p_start:%b %d} → {last_day:%b %d, %Y}{dtxt}</div></div>', unsafe_allow_html=True)
with c3:
    if fut is not None:
        proj = fut["Revenue"].sum()
        trail = hist["Revenue"].tail(horizon).sum()
        d = pct_change(proj, trail)
        dtxt = "" if d is None else f' • {"▲" if d >= 0 else "▼"} {abs(d):.1f}% vs last {horizon} wks'
        st.markdown(f'<div class="tcard t-future"><div class="tt">🔮 Future (next {horizon} weeks)</div><div class="tv">{money(proj)}</div>'
                    f'<div class="ts">≈ {num(fut["Cookies"].sum())} cookies projected</div>'
                    f'<div class="ts">{fut["Week Ending"].iloc[0]:%b %d} → {fut["Week Ending"].iloc[-1]:%b %d, %Y}{dtxt}</div></div>',
                    unsafe_allow_html=True)
    else:
        st.markdown('<div class="tcard t-future"><div class="tt">🔮 Future</div><div class="tv">—</div>'
                    '<div class="ts">Need at least 6 weeks of data to forecast.</div></div>', unsafe_allow_html=True)

st.write("")
tab_past, tab_pres, tab_fut, tab_cust, tab_data = st.tabs(
    ["⏪ Past", "📍 Present", "🔮 Future", "👥 Customers & Rush", "🗂️ Interactive Data"])

# ===================== PAST =====================
with tab_past:
    if past.empty:
        st.info("Nothing earlier than the present window with the current filters. Try a smaller 'Present window'.")
    else:
        k = st.columns(4)
        k[0].markdown(kpi("Past Revenue", money(S_past["rev"])), unsafe_allow_html=True)
        k[1].markdown(kpi("Past Cookies Shipped", num(S_past["cookies"])), unsafe_allow_html=True)
        k[2].markdown(kpi("Avg Order Value", money(S_past["aov"])), unsafe_allow_html=True)
        k[3].markdown(kpi("Rush Share", f'{S_past["rush"]:.0f}%'), unsafe_allow_html=True)

        m = past.set_index("Order Date").resample("MS").agg(
            Revenue=("Revenue", "sum"), Orders=("Order ID", "count"), Cookies=("Cookies Shipped", "sum")).reset_index()
        m["Month"] = m["Order Date"].dt.strftime("%b %Y")
        a, b = st.columns(2)
        with a:
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_bar(x=m["Month"], y=m["Revenue"], name="Revenue", marker_color="#8B5A2B", secondary_y=False)
            fig.add_scatter(x=m["Month"], y=m["Orders"], name="Orders", mode="lines+markers",
                            line=dict(color="#E0A458", width=3), secondary_y=True)
            show(style(fig, 360, "Monthly Revenue & Orders (past)"))
        with b:
            cum = past.sort_values("Order Date").copy()
            cum["Cumulative Revenue"] = cum["Revenue"].cumsum()
            fig = px.area(cum, x="Order Date", y="Cumulative Revenue", color_discrete_sequence=["#A0522D"])
            show(style(fig, 360, "Cumulative Revenue Growth"))
        a, b = st.columns(2)
        with a:
            order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            wd = past.assign(Day=past["Order Date"].dt.day_name()).groupby("Day")["Revenue"].mean().reindex(order).reset_index()
            fig = px.bar(wd, x="Day", y="Revenue", color="Revenue", color_continuous_scale=["#E3B778", "#5C3A1E"])
            fig.update_coloraxes(showscale=False)
            show(style(fig, 340, "Average Revenue by Weekday"))
        with b:
            fig = px.scatter(past, x="Cookies Shipped", y="Revenue", color="Rush Shipment",
                             color_discrete_map={"Yes": "#A0522D", "No": "#C68E4E"}, opacity=.8, hover_data=["Order ID", "Customer ID"])
            if len(past) > 2:
                s, i = np.polyfit(past["Cookies Shipped"], past["Revenue"], 1)
                xs = np.array([past["Cookies Shipped"].min(), past["Cookies Shipped"].max()])
                fig.add_scatter(x=xs, y=s * xs + i, mode="lines", name="Trend", line=dict(color="#3b2412", dash="dash"))
            show(style(fig, 340, "Cookies Shipped vs Revenue"))
        st.markdown('<div class="sec">📅 Monthly summary</div>', unsafe_allow_html=True)
        show_table(m[["Month", "Revenue", "Orders", "Cookies"]].round(2))

# ===================== PRESENT =====================
with tab_pres:
    k = st.columns(3)
    k[0].markdown(kpi("Revenue", money(S_pres["rev"]), pct_change(S_pres["rev"], S_prior["rev"]), f"last {win} days"), unsafe_allow_html=True)
    k[1].markdown(kpi("Cookies Shipped", num(S_pres["cookies"]), pct_change(S_pres["cookies"], S_prior["cookies"])), unsafe_allow_html=True)
    k[2].markdown(kpi("Orders", num(S_pres["orders"]), pct_change(S_pres["orders"], S_prior["orders"])), unsafe_allow_html=True)
    k = st.columns(3)
    k[0].markdown(kpi("Avg Order Value", money(S_pres["aov"]), pct_change(S_pres["aov"], S_prior["aov"])), unsafe_allow_html=True)
    k[1].markdown(kpi("Rush Orders", f'{S_pres["rush"]:.0f}%', pct_change(S_pres["rush"], S_prior["rush"])), unsafe_allow_html=True)
    k[2].markdown(kpi("Revenue / Cookie", f'${S_pres["rpc"]:.2f}', pct_change(S_pres["rpc"], S_prior["rpc"])), unsafe_allow_html=True)

    if present.empty:
        st.info("No orders in the present window.")
    else:
        daily = present.groupby("Order Date")["Revenue"].sum().reindex(
            pd.date_range(p_start, last_day), fill_value=0).rename_axis("Date").reset_index()
        daily["7-day avg"] = daily["Revenue"].rolling(7, min_periods=1).mean()
        a, b = st.columns([2, 1])
        with a:
            fig = go.Figure()
            fig.add_bar(x=daily["Date"], y=daily["Revenue"], name="Daily revenue", marker_color="#C68E4E")
            fig.add_scatter(x=daily["Date"], y=daily["7-day avg"], name="7-day avg", line=dict(color="#5C3A1E", width=3))
            show(style(fig, 360, f"Daily Revenue — last {win} days"))
        with b:
            rs = present["Rush Shipment"].map({"Yes": "Rush", "No": "Standard"}).value_counts().reset_index()
            rs.columns = ["Type", "Orders"]
            fig = px.pie(rs, names="Type", values="Orders", hole=.55, color="Type",
                         color_discrete_map={"Rush": "#A0522D", "Standard": "#E0A458"})
            show(style(fig, 360, "Rush vs Standard"))
        a, b = st.columns(2)
        with a:
            tc = present.groupby("Customer ID")["Revenue"].sum().nlargest(8).reset_index().sort_values("Revenue")
            fig = px.bar(tc, x="Revenue", y="Customer ID", orientation="h", color_discrete_sequence=["#8B5A2B"])
            show(style(fig, 340, "Top Customers (present)"))
        with b:
            fig = px.histogram(present, x="Revenue", nbins=12, color_discrete_sequence=["#A0522D"])
            show(style(fig, 340, "Order Size Distribution (present)"))
        st.markdown('<div class="sec">🧾 Most recent orders</div>', unsafe_allow_html=True)
        rec = present.sort_values("Order Date", ascending=False).head(15).copy()
        rec["Order Date"] = rec["Order Date"].dt.strftime("%Y-%m-%d")
        show_table(rec[["Order ID", "Customer ID", "Order Date", "Cookies Shipped", "Revenue", "Rush Shipment"]])

# ===================== FUTURE =====================
with tab_fut:
    if fut is None:
        st.info("Not enough weekly history (need 6+ complete weeks) to build a forecast with the current filters.")
    else:
        st.markdown(f'<div class="note">🔮 Forecast = straight-line trend fitted to weekly totals, extended <b>{horizon} weeks</b> '
                    f'with a <b>{growth:+d}%</b> scenario adjustment. The shaded band is an ~80% likely range. '
                    f'Change the horizon and scenario in the sidebar.</div>', unsafe_allow_html=True)
        st.write("")
        metric = st.radio("Forecast metric", ["Revenue", "Cookies"], horizontal=True)
        src = "Revenue" if metric == "Revenue" else "Cookies Shipped"
        k = st.columns(4)
        proj = fut[metric].sum()
        trail = hist[src].tail(horizon).sum()
        fmt = money if metric == "Revenue" else num
        k[0].markdown(kpi(f"Projected {metric}", fmt(proj), pct_change(proj, trail), f"next {horizon} weeks"), unsafe_allow_html=True)
        k[1].markdown(kpi("Avg per Week", fmt(proj / horizon)), unsafe_allow_html=True)
        k[2].markdown(kpi("Best Case", fmt(fut[metric + " High"].sum())), unsafe_allow_html=True)
        k[3].markdown(kpi("Worst Case", fmt(fut[metric + " Low"].sum())), unsafe_allow_html=True)

        fig = go.Figure()
        fig.add_scatter(x=hist["Week Ending"], y=hist[src], name="Actual (weekly)", mode="lines+markers",
                        line=dict(color="#5C3A1E", width=3))
        fig.add_scatter(x=hist["Week Ending"], y=hist[metric + " Trend"], name="Trend", line=dict(color="#C68E4E", dash="dot"))
        fig.add_scatter(x=fut["Week Ending"], y=fut[metric + " High"], line=dict(width=0), showlegend=False, hoverinfo="skip")
        fig.add_scatter(x=fut["Week Ending"], y=fut[metric + " Low"], fill="tonexty", fillcolor="rgba(224,164,88,.35)",
                        line=dict(width=0), name="80% range", hoverinfo="skip")
        fig.add_scatter(x=fut["Week Ending"], y=fut[metric], name="Forecast", mode="lines+markers",
                        line=dict(color="#A0522D", width=3, dash="dash"))
        show(style(fig, 420, f"Weekly {metric}: actual vs forecast"))

        fut_cum = fut[["Week Ending", metric]].copy()
        fut_cum["Cumulative"] = fut_cum[metric].cumsum()
        a, b = st.columns(2)
        with a:
            fig = px.bar(fut_cum, x="Week Ending", y=metric, color_discrete_sequence=["#D2A56B"])
            show(style(fig, 320, f"Projected weekly {metric}"))
        with b:
            fig = px.area(fut_cum, x="Week Ending", y="Cumulative", color_discrete_sequence=["#8B5A2B"])
            show(style(fig, 320, "Projected cumulative total"))
        st.markdown('<div class="sec">📋 Forecast table</div>', unsafe_allow_html=True)
        out = fut.copy()
        out["Week Ending"] = out["Week Ending"].dt.strftime("%Y-%m-%d")
        out = out.round(0)
        show_table(out)
        st.download_button("⬇️ Download forecast CSV", out.to_csv(index=False).encode("utf-8"), "cookie_forecast.csv", "text/csv")

# ===================== CUSTOMERS & RUSH =====================
with tab_cust:
    cu = f.groupby("Customer ID").agg(Orders=("Order ID", "count"), Revenue=("Revenue", "sum"),
                                       Cookies=("Cookies Shipped", "sum"),
                                       RushShare=("Rush Shipment", lambda s: (s == "Yes").mean() * 100)).reset_index()
    k = st.columns(4)
    k[0].markdown(kpi("Active Customers", num(len(cu))), unsafe_allow_html=True)
    k[1].markdown(kpi("Avg Revenue / Customer", money(cu["Revenue"].mean())), unsafe_allow_html=True)
    k[2].markdown(kpi("Top Customer", cu.loc[cu["Revenue"].idxmax(), "Customer ID"], sub=money(cu["Revenue"].max())), unsafe_allow_html=True)
    k[3].markdown(kpi("Repeat Customers", f'{(cu["Orders"] > 1).mean() * 100:.0f}%'), unsafe_allow_html=True)
    a, b = st.columns(2)
    with a:
        fig = px.scatter(cu, x="Orders", y="Revenue", size="Cookies", color="RushShare",
                         color_continuous_scale=["#E3B778", "#5C3A1E"], hover_name="Customer ID",
                         labels={"RushShare": "Rush %"})
        show(style(fig, 400, "Customer map (bubble = cookies, colour = rush %)"))
    with b:
        top = cu.nlargest(10, "Revenue").sort_values("Revenue")
        fig = px.bar(top, x="Revenue", y="Customer ID", orientation="h", color_discrete_sequence=["#8B5A2B"])
        show(style(fig, 400, "Top 10 Customers by Revenue"))
    a, b = st.columns(2)
    with a:
        rv = f.assign(Type=f["Rush Shipment"].map({"Yes": "Rush", "No": "Standard"})).groupby("Type").agg(
            Orders=("Order ID", "count"), Revenue=("Revenue", "sum"), AvgOrder=("Revenue", "mean")).reset_index()
        fig = px.bar(rv, x="Type", y="Revenue", color="Type", text_auto=".3s",
                     color_discrete_map={"Rush": "#A0522D", "Standard": "#E0A458"})
        show(style(fig, 340, "Revenue: Rush vs Standard"))
    with b:
        hm = f.assign(Day=f["Order Date"].dt.day_name(), Month=f["Order Date"].dt.strftime("%Y-%m"))
        pv = hm.pivot_table(index="Day", columns="Month", values="Revenue", aggfunc="sum", fill_value=0).reindex(
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        fig = px.imshow(pv, aspect="auto", color_continuous_scale=["#F6E3C0", "#C68E4E", "#4A2C14"])
        show(style(fig, 340, "Revenue Heatmap: Weekday × Month"))

# ===================== INTERACTIVE DATA =====================
with tab_data:
    st.markdown('<div class="sec">🗂️ Explore & download the (filtered) orders</div>', unsafe_allow_html=True)
    q = st.text_input("Search Order ID or Customer ID", "")
    t = f.copy()
    if q:
        t = t[t["Order ID"].str.contains(q, case=False) | t["Customer ID"].str.contains(q, case=False)]
    t["Order Date"] = t["Order Date"].dt.strftime("%Y-%m-%d")
    st.caption(f"{len(t):,} orders shown — click any column header to sort.")
    show_table(t[["Order ID", "Customer ID", "Order Date", "Cookies Shipped", "Revenue", "Rush Shipment", "Revenue per Cookie"]].round(2))
    st.download_button("⬇️ Download filtered CSV", t.to_csv(index=False).encode("utf-8"), "filtered_orders.csv", "text/csv")