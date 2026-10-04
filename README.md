# 🍪 Kevin's Cookie Company: Order Dashboard

> *Where data meets dough, on a warm wooden bench.* 🪵

An interactive **Streamlit** dashboard that turns 200 cookie orders into a story of **Past, Present and Future**. It is wrapped in a handcrafted wood-grain design, because spreadsheets deserve a nicer table to sit at.

🎭 **Designed & built by Chioma's Art** 🦚

🔗 **Live app:** `<paste your streamlit.app link here>`

---

## 🧁 The Story

Kevin runs a cookie company. Orders fly out the door, some rushed, some relaxed, some from customers who clearly cannot stop ordering. Kevin has a CSV. Kevin needs answers:

- How much have we made, and is it going up or down **right now**?
- What did our **past** look like?
- What might the **next few weeks** bring?
- Who are our best customers, and does paying for **rush shipping** pay off?

This dashboard answers all of it, and it looks like a cosy bakery counter while doing so.

---

## 📦 The Dataset

| Detail | Value |
|---|---|
| Rows | 200 orders |
| Columns | `Order ID`, `Customer ID`, `Order Date`, `Cookies Shipped`, `Revenue`, `Rush Shipment` |
| Date range | 3 Dec 2024 → 2 Jun 2025 |
| Customers | 49 unique customers |
| Total revenue | ≈ $513,977 |
| Cookies shipped | ≈ 100,044 🍪 |
| Order size | 11 to 996 cookies |
| Order revenue | $75.05 to $4,950.77 |
| Rush orders | 111 of 200 (≈ 55%) |

### 🔍 Fun things the data whispered
- 🚚 **Rush orders are slightly bigger:** average ~$2,662 versus ~$2,455 for standard orders.
- 🍪 **Revenue barely tracks cookie count** (correlation ≈ 0.10). More cookies does not automatically mean more money, so pricing and order type matter a lot.
- 👑 **CUST-005** is the top spender (~$23.6K), followed by CUST-039 and CUST-024.
- 📅 Monthly revenue stays in a steady band, with **December** the strongest month in the data.

---

## ✨ Features

- 🪵 **Wood-textured theme** built purely with CSS: plank seams, grain, a walnut sidebar and cream cards. No image files.
- ⏪📍🔮 **Past / Present / Future strip** at the top:
  - **Past**: everything before the chosen window
  - **Present**: the last *N* days, compared with the previous *N* days
  - **Future**: a trend forecast with best-case and worst-case ranges
- 🔎 **Sidebar filters**: date range, rush or standard, customers, revenue per order, cookies per order
- ⏳ **Time controls**: present window (days), forecast horizon (weeks), growth scenario (%)
- 📊 **5 tabs**: Past, Present, Future, Customers & Rush, Interactive Data
- 🗂️ **Interactive data table** with search, sorting and CSV downloads
- 📥 **CSV is built into the code**, so the app runs with zero uploads. An optional uploader lets anyone swap in their own file with the same columns.

---

## 🔮 How the Forecast Works

Weekly revenue and cookie totals are fitted with a straight-line trend (NumPy `polyfit`) and projected forward. The incomplete final week is dropped so it doesn't skew the line. The shaded band shows an approximate **80% range**, and a **growth scenario slider** lets you play optimist or pessimist.

> ⚠️ This is a simple trend model for exploration, not a guarantee. Cookies are unpredictable. 😄

---

## 🛠️ Tech Stack

`Python` • `Streamlit` • `Pandas` • `NumPy` • `Plotly`

---

## 🚀 Run It Yourself on your device click on the App link: https://cookie-jar-company-stocks-dashboard-geuwxxnkuhukazttgrna8b.streamlit.app/

## 📁 Project Structure

```
├── app.py              # the whole dashboard (data embedded)
├── requirements.txt
└── README.md
```

---

## 🧭 The Journey

This project started with a pile of wood-grain photos and a very specific vision: *"I wanted my dashboard to look like wood."* It grew into a full Past/Present/Future analytics tool with a custom theme, a forecasting engine and a self-contained data setup. It went from VS Code, to GitHub, to Streamlit Cloud, and now lives at a link anyone can open.

---

## 🙋🏾‍♀️ About

Built with love, curiosity and a lot of coffee by **Chioma's Art** 🎭🦚
Data Science and analysis • Dashboards • Storytelling with data

⭐ If this made you smile (or hungry), drop a star on the repo! thank you.
