import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Executive Dashboard · 360° E-Commerce",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', 'Segoe UI', sans-serif; }

    /* App background */
    .stApp { background: #06090f; }
    .main .block-container { background: #06090f; padding: 1.2rem 2rem 2rem 2rem; max-width: 100%; }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0d1117;
        border-right: 1px solid #21262d;
    }
    section[data-testid="stSidebar"] * { color: #c9d1d9 !important; }
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stMultiSelect label {
        color: #8b949e !important;
        font-size: 0.7rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.07em;
    }
    /* Sidebar select/input boxes */
    section[data-testid="stSidebar"] .stSelectbox > div > div,
    section[data-testid="stSidebar"] .stMultiSelect > div > div {
        background: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        color: #e6edf3 !important;
    }

    /* KPI Cards */
    .kpi-wrap {
        background: #0d1117;
        border: 1px solid #21262d;
        border-radius: 14px;
        padding: 22px 20px 18px 20px;
        position: relative;
        overflow: hidden;
        height: 140px;
    }
    .kpi-wrap::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        border-radius: 14px 14px 0 0;
    }
    .kpi-accent-purple::before { background: linear-gradient(90deg, #7c3aed, #a78bfa); }
    .kpi-accent-green::before  { background: linear-gradient(90deg, #059669, #34d399); }
    .kpi-accent-blue::before   { background: linear-gradient(90deg, #2563eb, #60a5fa); }
    .kpi-accent-amber::before  { background: linear-gradient(90deg, #d97706, #fbbf24); }

    .kpi-icon  { font-size: 1.4rem; margin-bottom: 6px; display: block; }
    .kpi-label { color: #8b949e; font-size: 0.68rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 4px; }
    .kpi-value { color: #f0f6fc; font-size: 2rem; font-weight: 800; line-height: 1; letter-spacing: -0.02em; }
    .kpi-sub   { color: #6e7681; font-size: 0.72rem; margin-top: 6px; }
    .kpi-sub-pos { color: #3fb950; font-size: 0.72rem; margin-top: 6px; font-weight: 600; }
    .kpi-sub-neg { color: #f85149; font-size: 0.72rem; margin-top: 6px; font-weight: 600; }

    /* Section labels */
    .sec-label {
        color: #8b949e;
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin: 22px 0 10px 2px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .sec-label::after {
        content: '';
        flex: 1;
        height: 1px;
        background: #21262d;
    }

    /* Chart wrappers */
    .chart-card {
        background: #0d1117;
        border: 1px solid #21262d;
        border-radius: 12px;
        padding: 4px 2px 2px 2px;
        height: 100%;
    }

    hr { border-color: #21262d !important; }

    /* Hide streamlit branding */
    #MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DATA LOAD & CLEAN
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("Sales_transactions_2022_2025.csv")
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    df["Order_Month"] = df["Order_Date"].dt.to_period("M").astype(str)
    df["Order_Quarter"] = df["Order_Date"].dt.to_period("Q").astype(str)
    df["Product_Category"] = df["Product_Category"].str.strip().str.title()
    df["Order_Status"] = df["Order_Status"].str.strip().str.title()
    df["Payment_Method"] = df["Payment_Method"].str.strip().str.title()
    return df

df_raw = load_data()

# ─────────────────────────────────────────────
# SIDEBAR — SLICERS
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:16px 0 10px 0; text-align:center;">
        <div style="font-size:2rem; margin-bottom:4px;">🛒</div>
        <div style="font-size:0.95rem; font-weight:700; color:#a78bfa; letter-spacing:0.03em;">360° E-Commerce</div>
        <div style="font-size:0.7rem; color:#6e7681; margin-top:2px;">Executive Dashboard</div>
    </div>
    <hr>
    <div style="font-size:0.68rem; font-weight:700; color:#8b949e; text-transform:uppercase;
                letter-spacing:0.1em; margin-bottom:12px; margin-top:4px;">🎛️ &nbsp;Filters</div>
    """, unsafe_allow_html=True)

    # Year — multiselect
    years = sorted(df_raw["Order_Year"].unique())
    sel_years = st.multiselect("📅 Year", years, default=years)

    # Country — selectbox (dropdown, single)
    countries = ["All Countries"] + sorted(df_raw["Country"].unique())
    sel_country = st.selectbox("🌍 Country", countries)

    # Product Category — selectbox (dropdown, single)
    cats = ["All Categories"] + sorted(df_raw["Product_Category"].unique())
    sel_cat = st.selectbox("📦 Product Category", cats)

    # Order Status — selectbox (dropdown, single)
    statuses = ["All Statuses"] + sorted(df_raw["Order_Status"].unique())
    sel_status = st.selectbox("📋 Order Status", statuses)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size:0.62rem; color:#484f58; text-align:center; line-height:1.6;'>"
        "Dataset: 2022–2025<br>18,045 transactions</div>",
        unsafe_allow_html=True
    )

# ─────────────────────────────────────────────
# FILTER DATA
# ─────────────────────────────────────────────
df = df_raw.copy()
if sel_years:
    df = df[df["Order_Year"].isin(sel_years)]
if sel_country != "All Countries":
    df = df[df["Country"] == sel_country]
if sel_cat != "All Categories":
    df = df[df["Product_Category"] == sel_cat]
if sel_status != "All Statuses":
    df = df[df["Order_Status"] == sel_status]

# ─────────────────────────────────────────────
# CHART THEME HELPER
# ─────────────────────────────────────────────
BG      = "#0d1117"
GRID    = "#21262d"
FONT    = "#c9d1d9"
PALETTE = ["#7c3aed", "#2563eb", "#059669", "#d97706",
           "#db2777", "#0891b2", "#65a30d", "#dc2626"]

def theme(fig, title="", height=360):
    fig.update_layout(
        title=dict(text=title, font=dict(color="#e6edf3", size=13, family="Inter"), x=0.02, y=0.97),
        plot_bgcolor=BG, paper_bgcolor=BG,
        font=dict(color=FONT, size=11, family="Inter"),
        height=height,
        margin=dict(l=14, r=14, t=44, b=14),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=FONT, size=10),
                    bordercolor=GRID, borderwidth=1),
        xaxis=dict(gridcolor=GRID, linecolor=GRID, tickfont=dict(color=FONT),
                   showgrid=True, zeroline=False),
        yaxis=dict(gridcolor=GRID, linecolor=GRID, tickfont=dict(color=FONT),
                   showgrid=True, zeroline=False),
    )
    return fig

# ─────────────────────────────────────────────
# METRICS
# ─────────────────────────────────────────────
total_sales   = df["Sales_Amount"].sum()
total_profit  = df["Profit"].sum()
total_orders  = df["Order_ID"].nunique()
avg_margin    = (total_profit / total_sales * 100) if total_sales > 0 else 0
return_rate   = (df[df["Return_Flag"] == "Yes"].shape[0] / df.shape[0] * 100) if df.shape[0] > 0 else 0

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:space-between;
            padding:8px 0 0 0; margin-bottom:6px;">
    <div>
        <div style="font-size:1.55rem; font-weight:800; color:#f0f6fc; letter-spacing:-0.02em;">
            Executive Dashboard
        </div>
        <div style="font-size:0.8rem; color:#6e7681; margin-top:3px; font-weight:500;">
            360° E-Commerce Performance &nbsp;·&nbsp; 2022–2025
        </div>
    </div>
    <div style="text-align:right;">
        <div style="font-size:0.68rem; color:#8b949e; font-weight:600; text-transform:uppercase;
                    letter-spacing:0.07em;">Records in view</div>
        <div style="font-size:1.4rem; font-weight:800; color:#a78bfa;">{len(df):,}</div>
    </div>
</div>
<hr>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# KPI CARDS  (4 cards)
# ─────────────────────────────────────────────
st.markdown('<div class="sec-label">Key Performance Indicators</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

kpi_data = [
    (c1, "kpi-accent-purple", "💰", "Total Revenue",   f"${total_sales:,.0f}",
     "↑ All channels combined", "pos"),
    (c2, "kpi-accent-green",  "📈", "Net Profit",       f"${total_profit:,.0f}",
     f"Margin: {avg_margin:.1f}%", "pos" if avg_margin >= 15 else "neg"),
    (c3, "kpi-accent-blue",   "🛍️", "Total Orders",    f"{total_orders:,}",
     "Unique order IDs", "neu"),
    (c4, "kpi-accent-amber",  "🔄", "Return Rate",      f"{return_rate:.1f}%",
     "↓ Target < 5%", "pos" if return_rate < 5 else "neg"),
]

for col, accent, icon, label, value, sub, sub_type in kpi_data:
    with col:
        sub_class = f"kpi-sub-{sub_type}" if sub_type in ("pos", "neg") else "kpi-sub"
        st.markdown(f"""
        <div class="kpi-wrap {accent}">
            <span class="kpi-icon">{icon}</span>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="{sub_class}">{sub}</div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CHART ROW 1:  Revenue trend (wide)  +  Category donut
# ─────────────────────────────────────────────
st.markdown('<div class="sec-label">Revenue & Category Breakdown</div>', unsafe_allow_html=True)

ch_left, ch_right = st.columns([3, 2])

with ch_left:
    monthly = (
        df.groupby("Order_Month")
          .agg(Revenue=("Sales_Amount", "sum"), Profit=("Profit", "sum"))
          .reset_index()
          .sort_values("Order_Month")
    )
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=monthly["Order_Month"], y=monthly["Revenue"],
        mode="lines+markers", name="Revenue",
        line=dict(color="#7c3aed", width=2.5),
        fill="tozeroy", fillcolor="rgba(124,58,237,0.10)",
        marker=dict(size=5, color="#a78bfa")
    ))
    fig_trend.add_trace(go.Scatter(
        x=monthly["Order_Month"], y=monthly["Profit"],
        mode="lines+markers", name="Profit",
        line=dict(color="#059669", width=2),
        fill="tozeroy", fillcolor="rgba(5,150,105,0.07)",
        marker=dict(size=5, color="#34d399")
    ))
    fig_trend.update_xaxes(tickangle=40, nticks=18)
    theme(fig_trend, "📈  Monthly Revenue & Profit Trend", 360)
    st.plotly_chart(fig_trend, use_container_width=True)

with ch_right:
    cat_rev = (
        df.groupby("Product_Category")["Sales_Amount"]
          .sum().reset_index()
          .sort_values("Sales_Amount", ascending=False)
    )
    fig_donut = px.pie(
        cat_rev, names="Product_Category", values="Sales_Amount",
        hole=0.58, color_discrete_sequence=PALETTE
    )
    fig_donut.update_traces(
        textfont_color="#fff", textfont_size=11,
        hovertemplate="<b>%{label}</b><br>Revenue: $%{value:,.0f}<extra></extra>"
    )
    fig_donut.update_layout(
        annotations=[dict(text="<b>Category</b>", x=0.5, y=0.5,
                          font=dict(color="#8b949e", size=11), showarrow=False)]
    )
    theme(fig_donut, "📦  Revenue by Product Category", 360)
    st.plotly_chart(fig_donut, use_container_width=True)

# ─────────────────────────────────────────────
# CHART ROW 2:  Country bar  +  Order status donut
# ─────────────────────────────────────────────
st.markdown('<div class="sec-label">Geographic & Order Status Overview</div>', unsafe_allow_html=True)

ch_left2, ch_right2 = st.columns([3, 2])

with ch_left2:
    country_agg = (
        df.groupby("Country")
          .agg(Revenue=("Sales_Amount","sum"), Profit=("Profit","sum"), Orders=("Order_ID","nunique"))
          .reset_index()
          .sort_values("Revenue", ascending=True)
    )
    fig_country = go.Figure()
    fig_country.add_trace(go.Bar(
        y=country_agg["Country"], x=country_agg["Revenue"],
        orientation="h", name="Revenue",
        marker=dict(color="#2563eb", line=dict(width=0)),
        text=country_agg["Revenue"].apply(lambda v: f"${v:,.0f}"),
        textposition="outside", textfont=dict(color=FONT, size=10),
        hovertemplate="<b>%{y}</b><br>Revenue: $%{x:,.0f}<extra></extra>"
    ))
    fig_country.add_trace(go.Bar(
        y=country_agg["Country"], x=country_agg["Profit"],
        orientation="h", name="Profit",
        marker=dict(color="#059669", line=dict(width=0)),
        hovertemplate="<b>%{y}</b><br>Profit: $%{x:,.0f}<extra></extra>"
    ))
    fig_country.update_layout(barmode="overlay", bargap=0.3)
    theme(fig_country, "🌍  Revenue & Profit by Country", 340)
    st.plotly_chart(fig_country, use_container_width=True)

with ch_right2:
    status_cnt = df["Order_Status"].value_counts().reset_index()
    status_cnt.columns = ["Status", "Count"]
    STATUS_COLORS = {
        "Completed":  "#059669",
        "Shipped":    "#2563eb",
        "Processing": "#d97706",
        "Returned":   "#f85149",
        "Cancelled":  "#6e7681",
    }
    colors = [STATUS_COLORS.get(s, "#7c3aed") for s in status_cnt["Status"]]
    fig_status = go.Figure(go.Pie(
        labels=status_cnt["Status"],
        values=status_cnt["Count"],
        hole=0.55,
        marker=dict(colors=colors, line=dict(color=BG, width=2)),
        textfont=dict(color="#fff", size=11),
        hovertemplate="<b>%{label}</b><br>Count: %{value:,}<br>Share: %{percent}<extra></extra>"
    ))
    fig_status.update_layout(
        annotations=[dict(text="<b>Orders</b>", x=0.5, y=0.5,
                          font=dict(color="#8b949e", size=11), showarrow=False)]
    )
    theme(fig_status, "📋  Order Status Distribution", 340)
    st.plotly_chart(fig_status, use_container_width=True)

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<hr>
<div style="text-align:center; color:#484f58; font-size:0.7rem; padding:10px 0 4px 0;">
    360° E-Commerce Performance &amp; Customer Insights &nbsp;·&nbsp;
    Built with <span style="color:#7c3aed; font-weight:600;">Streamlit</span> &amp;
    <span style="color:#2563eb; font-weight:600;">Plotly</span> &nbsp;·&nbsp;
    Data: 2022–2025 Sales Transactions
</div>
""", unsafe_allow_html=True)
