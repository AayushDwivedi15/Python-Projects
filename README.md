# 🛒 360° E-Commerce Performance & Customer Insights

> An interactive executive dashboard built with **Python · Streamlit · Plotly** — transforming 18,045 sales transactions (2022–2025) into live, filterable business intelligence.

---

## 📸 Dashboard Preview

```
┌─────────────────┬──────────────────────────────────────────────────────────┐
│                 │  Executive Dashboard              Records in view: 18,045 │
│   SIDEBAR       │  360° E-Commerce Performance  ·  2022–2025               │
│   ─────────     ├──────────────────────────────────────────────────────────┤
│                 │  KEY PERFORMANCE INDICATORS                               │
│  📅 Year        │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│  [2022–2025]    │  │💰 TOTAL  │ │📈 NET    │ │🛍️ TOTAL │ │🔄 RETURN │   │
│                 │  │ REVENUE  │ │ PROFIT   │ │  ORDERS  │   RATE     │   │
│  🌍 Country     │  │ $8.25M   │ │ $1.65M   │ │  14,541  │   10.4%    │   │
│  [All  ▼]       │  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │
│                 ├──────────────────────────────────────────────────────────┤
│  📦 Category    │  ┌──────────────────────────────┐ ┌──────────────────┐  │
│  [All  ▼]       │  │ Monthly Revenue & Profit     │ │ Category Donut   │  │
│                 │  │ Trend  (area-line, 48 months) │ │ Electronics      │  │
│  📋 Status      │  │                              │ │ Office Supplies  │  │
│  [All  ▼]       │  └──────────────────────────────┘ └──────────────────┘  │
│                 ├──────────────────────────────────────────────────────────┤
│  ─────────      │  ┌──────────────────────────────┐ ┌──────────────────┐  │
│  18,045 rows    │  │ Revenue & Profit by Country  │ │ Order Status     │  │
│                 │  │ (horizontal overlay bars)    │ │ Distribution     │  │
└─────────────────┴──────────────────────────────────────────────────────────┘
```

---

## 🚀 Features

- **Single-page executive dashboard** — everything visible without scrolling
- **4 live KPI cards** — Total Revenue, Net Profit, Total Orders, Return Rate
- **4 interactive Plotly charts** — trend line, donut, horizontal bar, status donut
- **4 sidebar slicers** — Year (multi-select), Country, Product Category, Order Status (dropdowns)
- **Real-time filtering** — all charts and KPIs update instantly on every slicer change
- **Live record counter** — shows exactly how many rows match current filters
- **Dark professional UI** — custom CSS with Inter font, dark `#06090f` background
- **Zero-config** — one Python file, no database, no web server setup required

---

## 📊 Dashboard Visuals

| # | Chart | Type | Insight |
|---|-------|------|---------|
| 1 | **Monthly Revenue & Profit Trend** | Dual area-line (48 months) | Seasonality, growth, revenue-profit gap |
| 2 | **Revenue by Product Category** | Donut chart | Category revenue share |
| 3 | **Revenue & Profit by Country** | Overlaid horizontal bar | Market size vs. profitability per country |
| 4 | **Order Status Distribution** | Semantic colour donut | Fulfilment health at a glance |

| # | KPI Card | Formula | Colour Logic |
|---|----------|---------|--------------|
| 1 | 💰 Total Revenue | `Sales_Amount.sum()` | Purple accent — always shown |
| 2 | 📈 Net Profit | `Profit.sum()` | Green if margin ≥ 15%, red otherwise |
| 3 | 🛍️ Total Orders | `Order_ID.nunique()` | Blue accent — neutral |
| 4 | 🔄 Return Rate | `(Returns / Total) × 100` | Green if < 5%, red if ≥ 5% |

---

## 🗂️ Dataset

| Property | Value |
|----------|-------|
| **File** | `Sales_transactions_2022_2025.csv` |
| **Rows** | 18,045 transactions |
| **Columns** | 36 fields |
| **Date Range** | January 2022 – December 2025 |
| **Countries** | Australia, Canada, France, Germany, United Kingdom, United States |
| **Categories** | Electronics, Office Supplies, Furniture, Appliances |
| **Channels** | Online, Retail Store, B2B Portal, Phone Order |
| **Order Statuses** | Completed, Shipped, Processing, Returned, Cancelled |
| **Total Revenue** | $8,252,141 |
| **Total Profit** | $1,649,388 |
| **Profit Margin** | 20.0% |

---

## 🛠️ Tech Stack

| Library | Version | Role |
|---------|---------|------|
| [Streamlit](https://streamlit.io) | 1.64.0 | Frontend + backend framework, sidebar, layout, reactivity |
| [Plotly](https://plotly.com/python/) | 7.1.0 | All interactive charts (`plotly.express`, `plotly.graph_objects`) |
| [Pandas](https://pandas.pydata.org) | 2.3.3 | Data loading, cleaning, aggregation |
| [NumPy](https://numpy.org) | 2.2.6 | Numerical operations |

---

## 📁 Project Structure

```
📦 project-root/
 ┣ 📄 dashboard.py                      ← Main application (single file, ~280 lines)
 ┣ 📄 Sales_transactions_2022_2025.csv  ← Source dataset (18,045 rows × 36 cols)
 ┣ 📄 requirements.txt                  ← Pinned Python dependencies
 ┗ 📄 README.md                         ← This file
```

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/AayushDwivedi15/ecommerce-dashboard.git
cd ecommerce-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install streamlit==1.64.0 plotly==7.1.0 pandas==2.3.3 numpy==2.2.6
```

### 3. Run the dashboard

```bash
streamlit run dashboard.py
```

### 4. Open in your browser

Streamlit will automatically open **http://localhost:8501**

> **Note:** Make sure `Sales_transactions_2022_2025.csv` is in the **same directory** as `dashboard.py` before running.

---

## 🎛️ How to Use the Filters

All filters live in the **left sidebar** and apply instantly to every KPI and chart:

| Slicer | Type | Default | Options |
|--------|------|---------|---------|
| 📅 **Year** | Multi-select | All years selected | 2022, 2023, 2024, 2025 |
| 🌍 **Country** | Dropdown | All Countries | 6 countries |
| 📦 **Product Category** | Dropdown | All Categories | Electronics, Office Supplies, Furniture, Appliances |
| 📋 **Order Status** | Dropdown | All Statuses | Completed, Shipped, Processing, Returned, Cancelled |

Selecting a specific combination — e.g. **Year: 2024, Country: United States, Category: Electronics, Status: Completed** — instantly narrows every chart and KPI card to only those matching records.

---

## 🏗️ Architecture

```
CSV File (cached on first load)
        │
        ▼
   load_data()  ──  @st.cache_data
        │
        ▼
  Sidebar Slicers  ──  sel_years / sel_country / sel_cat / sel_status
        │
        ▼
  Filter Logic  ──  Boolean masks on df_raw.copy()
        │
        ▼
  Metric Calculation  ──  total_sales / total_profit / total_orders / return_rate
        │
     ┌──┴──┐
     │     │
     ▼     ▼
  KPI    Charts (4x Plotly figures)
 Cards    │
     │    ▼
     └──► Streamlit Render  ──  st.markdown() + st.plotly_chart()
               │
               ▼
        Browser @ localhost:8501
```

On every slicer change, Streamlit re-executes the entire script from top to bottom. The `@st.cache_data` decorator ensures the CSV is only read once — subsequent reruns skip the file I/O and go straight to filtering.

---

## 📐 Design System

```
Backgrounds:  App #06090f  │  Cards & Charts #0d1117  │  Borders #21262d
Text:         Primary #f0f6fc  │  Secondary #c9d1d9  │  Muted #8b949e
Accents:      Purple #7c3aed  │  Blue #2563eb  │  Green #059669  │  Amber #d97706
Font:         Inter (Google Fonts) → Segoe UI → system-ui → sans-serif
```

---

## 📋 Requirements

```text
streamlit==1.64.0
plotly==7.1.0
pandas==2.3.3
numpy==2.2.6
```

---

## 🔧 Troubleshooting

| Issue | Fix |
|-------|-----|
| `FileNotFoundError: Sales_transactions_2022_2025.csv` | Place the CSV in the same directory as `dashboard.py` |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| Charts appear blank after filtering | A filter combination returned 0 records — widen your selection |
| Port 8501 already in use | Run `streamlit run dashboard.py --server.port 8502` |
| Slow first load | Normal — Streamlit compiles the app on first run; subsequent loads are instant |

---

## 🚧 Possible Enhancements

- [ ] Add Year-over-Year comparison toggle
- [ ] Export filtered data as CSV download button
- [ ] Add a second page for product-level deep-dive
- [ ] Add date range picker for sub-monthly granularity
- [ ] Deploy to [Streamlit Community Cloud](https://streamlit.io/cloud) for public sharing

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Built with ❤️ using **Python · Streamlit · Plotly**

</div>
