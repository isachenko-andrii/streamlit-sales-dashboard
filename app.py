"""
Аналітичний дашборд продажів та прибутку
Запуск локально: streamlit run app.py
"""

import pandas as pd
import plotly.express as px
import streamlit as st

# ----------------------------------------------------------------------
# UA: АВТОР
# EN: AUTHOR
# ----------------------------------------------------------------------

AUTHOR_NAME = "Andrii Isachenko"
AUTHOR_URL = "https://www.linkedin.com/in/isachenko-andrii/"

# ----------------------------------------------------------------------
# UA: НАЛАШТУВАННЯ СТОРІНКИ
# EN: PAGE SETTINGS
# ----------------------------------------------------------------------

st.set_page_config(
    page_title="Sales and Profit Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

DATA_PATH = "data/superstore.csv"

# ----------------------------------------------------------------------
# UA: ЗАВАНТАЖЕННЯ І ПІДГОТОВКА ДАНИХ (з кешуванням)
# EN: DATA LOADING AND PREPARATION (with caching)
# ----------------------------------------------------------------------

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="latin-1")

   # UA: Kaggle-версії датасета іноді відрізняються регістром/пробілами в назвах колонок
   # EN: Kaggle versions of the dataset sometimes differ in case/spaces in column names
    
    df.columns = [c.strip() for c in df.columns]

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

    return df

df_raw = load_data(DATA_PATH)


# ----------------------------------------------------------------------
# UA: СЛОВНИК ПЕРЕКЛАДІВ - Значення самих даних (Furniture, Consumer, East тощо) НЕ перекладаються — це фактичні значення з датасету.
# EN: TRANSLATION DICTIONARY - The values ​​of the data themselves (Furniture, Consumer, East, etc.) are NOT translated — these are the actual values ​​from the dataset.
# ----------------------------------------------------------------------

TRANSLATIONS = {
    "ua": {
        "sidebar_header": "Фільтри",
        "date_range_label": "Період замовлень",
        "region_label": "Регіон",
        "category_label": "Категорія",
        "segment_label": "Сегмент клієнтів",
        "filtered_rows": "Відфільтровано рядків",
        "of_word": "з",
        "dashboard_title": "📊 Аналітичний дашборд продажів",
        "dashboard_caption": (
            "Датасет: Superstore Sales (Kaggle). Використовуйте фільтри зліва, "
            "щоб змінювати період, регіон, категорію та сегмент клієнтів."
        ),
        "empty_warning": "За обраними фільтрами немає даних. Змініть умови фільтрації.",
        "tab_kpi": "🔢 KPI",
        "tab_trend": "📈 Динаміка",
        "tab_breakdown": "🗂️ Категорії та регіони",
        "tab_top": "🏆 Топ підкатегорій",
        "tab_discount": "💸 Знижки та прибуток",
        "tab_table": "📋 Дані",
        "kpi_title": "Ключові показники",
        "kpi_revenue": "Виручка",
        "kpi_profit": "Прибуток",
        "kpi_orders": "Замовлень",
        "kpi_aov": "Середній чек",
        "kpi_margin": "Маржинальність",
        "kpi_profitable_share": "Частка прибуткових замовлень",
        "trend_title": "Динаміка продажу та прибутку по місяцях",
        "trend_value_label": "Сума, $",
        "trend_month_label": "Місяць",
        "trend_legend_label": "Показник",
        "cat_title": "Продаж за категоріями",
        "cat_sales_label": "Виручка, $",
        "region_title": "Продаж за регіонами",
        "top_title": "Топ-10 підкатегорій за прибутком",
        "top_subcat_label": "Підкатегорія",
        "top_profit_label": "Прибуток, $",
        "losing_prefix": "⚠️ Підкатегорії з негативним прибутком у вибраному періоді: ",
        "losing_suffix": ". Варто перевірити рівень знижок за цими позиціями.",
        "discount_title": "Вплив знижки на прибуток",
        "discount_label": "Знижка",
        "discount_profit_label": "Прибуток, $",
        "corr_caption": "Коефіцієнт кореляції між знижкою та прибутком: ",
        "table_title": "Детальні дані",
        "download_button": "⬇️ Завантажити відфільтровані дані (CSV)",
    },
    "en": {
        "sidebar_header": "Filters",
        "date_range_label": "Order date range",
        "region_label": "Region",
        "category_label": "Category",
        "segment_label": "Customer segment",
        "filtered_rows": "Filtered rows",
        "of_word": "of",
        "dashboard_title": "📊 Sales Analytics Dashboard",
        "dashboard_caption": (
            "Dataset: Superstore Sales (Kaggle). Use the filters on the left "
            "to change the period, region, category, and customer segment."
        ),
        "empty_warning": "No data matches the selected filters. Please adjust the filter conditions.",
        "tab_kpi": "🔢 KPI",
        "tab_trend": "📈 Trend",
        "tab_breakdown": "🗂️ Categories & Regions",
        "tab_top": "🏆 Top Sub-Categories",
        "tab_discount": "💸 Discount & Profit",
        "tab_table": "📋 Data",
        "kpi_title": "Key Performance Indicators",
        "kpi_revenue": "Revenue",
        "kpi_profit": "Profit",
        "kpi_orders": "Orders",
        "kpi_aov": "Avg. Order Value",
        "kpi_margin": "Profit Margin",
        "kpi_profitable_share": "Share of Profitable Orders",
        "trend_title": "Monthly Sales & Profit Trend",
        "trend_value_label": "Amount, $",
        "trend_month_label": "Month",
        "trend_legend_label": "Metric",
        "cat_title": "Sales by Category",
        "cat_sales_label": "Revenue, $",
        "region_title": "Sales by Region",
        "top_title": "Top 10 Sub-Categories by Profit",
        "top_subcat_label": "Sub-Category",
        "top_profit_label": "Profit, $",
        "losing_prefix": "⚠️ Sub-categories with negative profit in the selected period: ",
        "losing_suffix": ". It may be worth reviewing the discount levels for these items.",
        "discount_title": "Discount Impact on Profit",
        "discount_label": "Discount",
        "discount_profit_label": "Profit, $",
        "corr_caption": "Correlation coefficient between discount and profit: ",
        "table_title": "Detailed Data",
        "download_button": "⬇️ Download filtered data (CSV)",
    },
}

# ----------------------------------------------------------------------
# UA: ПЕРЕМИКАЧ МОВИ (перший елемент бічної панелі)
# EN: LANGUAGE SWITCH (first item in the sidebar)
# ----------------------------------------------------------------------

lang_choice = st.sidebar.radio(
    "Мова / Language",
    options=["Українська", "English"],
    horizontal=True,
)
lang = "ua" if lang_choice == "Українська" else "en"
T = TRANSLATIONS[lang]
 
st.sidebar.markdown("---")

# ----------------------------------------------------------------------
# UA: БІЧНА ПАНЕЛЬ - ФІЛЬТРИ
# EN: SIDE PANEL - FILTERS
# ----------------------------------------------------------------------

st.sidebar.header(T["sidebar_header"])

min_date, max_date = df_raw["Order Date"].min(), df_raw["Order Date"].max()
date_range = st.sidebar.date_input(
    T["date_range_label"],
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

regions = st.sidebar.multiselect(
    T["region_label"], options=sorted(df_raw["Region"].unique()), default=sorted(df_raw["Region"].unique())
)

categories = st.sidebar.multiselect(
    T["category_label"], options=sorted(df_raw["Category"].unique()), default=sorted(df_raw["Category"].unique())
)

segments = st.sidebar.multiselect(
    T["segment_label"], options=sorted(df_raw["Segment"].unique()), default=sorted(df_raw["Segment"].unique())
)

# Застосовуємо фільтри
# Apply filters

if len(date_range) == 2:
    start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
else:
    start, end = min_date, max_date

df = df_raw[
    (df_raw["Order Date"] >= start)
    & (df_raw["Order Date"] <= end)
    & (df_raw["Region"].isin(regions))
    & (df_raw["Category"].isin(categories))
    & (df_raw["Segment"].isin(segments))
]

st.sidebar.markdown("---")
st.sidebar.caption(f"{T['filtered_rows']}: **{len(df):,}** {T['of_word']} {len(df_raw):,}")

# ----------------------------------------------------------------------
# UA: ЗАГОЛОВОК (sticky - прилипає до верху екрану разом зі смужкою табів)
# EN: TITLE (sticky - sticks to the top of the screen along with the tab strip)
# ----------------------------------------------------------------------

bg_color = st.get_option("theme.backgroundColor") or "#ffffff"

st.markdown(
    f"""
    <style>
    .block-container {{
        padding-top: 2.5rem;
    }}

    /* висота вбудованої панелі Streamlit (Share / ⭐ / ✏️ / GitHub) —
       заголовок повинен прилипати НИЖЧЕ неї, а не до самого верху вікна */
       
    :root {{
        --stheader-height: 2.875rem;
    }}

    /* заголовок + підпис — липнуть одразу під панеллю Streamlit */
    
    .dashboard-header {{
        position: sticky;
        top: var(--stheader-height);
        background: {bg_color};
        z-index: 999;
        padding-top: 0.3rem;
        padding-bottom: 0.3rem;
    }}
    .dashboard-header h1 {{
        margin-bottom: 0.1rem;
        font-size: 1.9rem;
    }}
    .dashboard-header p {{
        margin: 0;
        color: gray;
        font-size: 0.85rem;
    }}

    /* смуга вкладок — липне одразу під заголовком */
    
    div[data-testid="stTabs"] > div:first-child {{
        position: sticky;
        top: calc(var(--stheader-height) + 3.6rem);   /* підстрой другий доданок під фактичну висоту .dashboard-header, якщо з'явиться нахлест/зазор */
        background: {bg_color};
        z-index: 998;
        padding-top: 0.3rem;
    }}

    /* великі KPI (глобально — st.metric більше ніде на дашборді не використовується) */
    
    [data-testid="stMetricValue"] {{
        margin-top: 14px;   /* зсуває значення вниз відносно підпису */
        font-size: 2.3rem;
        color: #1a73e8;
        font-weight: 500;
    }}
    [data-testid="stMetricLabel"] {{
        font-size: 1.05rem;
    }}

    /* центруємо підпис і значення по горизонталі всередині блоку */
    [data-testid="stMetric"] {{
        text-align: center;
    }}

    /* центруємо вміст блоку по вертикалі всередині рамки (border=True) */
    div[data-testid="stVerticalBlockBorderWrapper"]:has([data-testid="stMetric"]) {{
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    </style>

    <div class="dashboard-header">
        <h1>{T['dashboard_title']}</h1>
        <p>{T['dashboard_caption']}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if df.empty:
    st.warning(T["empty_warning"])
    st.stop()


# ----------------------------------------------------------------------
# UA: KPI-РОЗРАХУНКИ (висновок - в окремому табі, див. крок нижче)
# EN: KPI CALCULATIONS (output in a separate tab, see step below)
# ----------------------------------------------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
avg_order_value = total_sales / total_orders if total_orders else 0
margin_pct = (total_profit / total_sales * 100) if total_sales else 0

# Частка прибуткових замовлень рахується на рівні замовлення (Order ID),
# оскільки одне замовлення може включати кілька товарних позицій —
# підсумовуємо прибуток по замовленню і перевіряємо, чи він додатний
order_profit = df.groupby("Order ID")["Profit"].sum()
profitable_orders_pct = (order_profit > 0).mean() * 100 if len(order_profit) else 0

# ----------------------------------------------------------------------
# UA: РОЗДІЛИ АНАЛІЗУ — В ТАБАХ (однакова висота, щоб сторінка не "стрибала")
# EN: ANALYSIS SECTIONS — IN TABS (same height so the page doesn't "jump")
# ----------------------------------------------------------------------

TAB_HEIGHT = 520  # px — зменшено, щоб шапка + таб вміщалися в один екран

tab_kpi, tab_trend, tab_breakdown, tab_top, tab_discount, tab_table = st.tabs(
    [
        T["tab_kpi"],
        T["tab_trend"],
        T["tab_breakdown"],
        T["tab_top"],
        T["tab_discount"],
        T["tab_table"],
    ]
)

# --- UA: Таб 1 KPI: великі ключові метрики --------------------------------
# --- UA: Tab 1 KPI: major key metrics -------------------------------------

KPI_BOX_HEIGHT = 150  # px — висота кожного блоку-показника, можна збільшити за бажання

with tab_kpi:
    with st.container(height=TAB_HEIGHT, border=False):
        st.subheader("Ключові показники ефективності")

        row1 = st.columns(3)
        with row1[0]:
            with st.container(border=True, height=KPI_BOX_HEIGHT):
                st.metric("Виторг", f"${total_sales:,.0f}")
        with row1[1]:
            with st.container(border=True, height=KPI_BOX_HEIGHT):
                st.metric("Прибуток", f"${total_profit:,.0f}")
        with row1[2]:
            with st.container(border=True, height=KPI_BOX_HEIGHT):
                st.metric("Замовлень", f"{total_orders:,}")

        row2 = st.columns(3)
        with row2[0]:
            with st.container(border=True, height=KPI_BOX_HEIGHT):
                st.metric("Середній чек", f"${avg_order_value:,.0f}")
        with row2[1]:
            with st.container(border=True, height=KPI_BOX_HEIGHT):
                st.metric("Маржинальність", f"{margin_pct:.1f}%")
        with row2[2]:
            with st.container(border=True, height=KPI_BOX_HEIGHT):
                st.metric("Частка прибуткових замовлень", f"{profitable_orders_pct:.1f}%")

# --- UA: Таб 2: Динаміка продажів у часі -----------------------------------
# --- EN: Tab 2: Sales dynamics over time -----------------------------------

with tab_trend:
    with st.container(height=TAB_HEIGHT, border=False):
        st.subheader("Динаміка продажу та прибутку по місяцях")

        monthly = (
            df.groupby("Month")[["Sales", "Profit"]]
            .sum()
            .reset_index()
            .sort_values("Month")
        )

        fig_trend = px.line(
            monthly,
            x="Month",
            y=["Sales", "Profit"],
            labels={"value": "Сума, $", "Month": "Місяць", "variable": "Показник"},
            markers=True,
            height=400
        )
        fig_trend.update_layout(hovermode="x unified", legend_title_text="")
        st.plotly_chart(fig_trend, use_container_width=True)

# --- UA: Таб 3: Розбивка за категоріями та регіонами-----------------------------
# --- UA: Tab 3: Breakdown by categories and regions------------------------------

with tab_breakdown:
    with st.container(height=TAB_HEIGHT, border=False):
        col_left, col_right = st.columns(2)

        with col_left:
            st.subheader("Продажі за категоріями")
            cat_data = df.groupby("Category")[["Sales", "Profit"]].sum().reset_index()
            fig_cat = px.bar(
                cat_data.sort_values("Sales", ascending=True),
                x="Sales",
                y="Category",
                orientation="h",
                text_auto=".2s",
                color="Profit",
                color_continuous_scale="RdYlGn",
                labels={"Sales": "Виторг, $", "Category": ""},
                height=400
            )
            st.plotly_chart(fig_cat, use_container_width=True)

        with col_right:
            st.subheader("Продажі по регіонах")
            region_data = df.groupby("Region")["Sales"].sum().reset_index()
            fig_region = px.pie(
                region_data,
                names="Region",
                values="Sales",
                hole=0.45,
                height=400
            )
            fig_region.update_traces(textinfo="percent+label")
            st.plotly_chart(fig_region, use_container_width=True)

# --- UA: Таб 4: Топ підкатегорій за прибутком-----------------------------------
# --- EN: Tab 4: Top subcategories by revenue-----------------------------------

with tab_top:
    with st.container(height=TAB_HEIGHT, border=False):
        st.subheader("Топ-10 підкатегорій за прибутком")

        sub_data = (
            df.groupby("Sub-Category")[["Sales", "Profit"]]
            .sum()
            .reset_index()
            .sort_values("Profit", ascending=False)
        )

        fig_sub = px.bar(
            sub_data.head(10),
            x="Sub-Category",
            y="Profit",
            color="Profit",
            color_continuous_scale="RdYlGn",
            labels={"Sub-Category": "Підкатегорія", "Profit": "Прибуток, $"},
            height=400
        )
        st.plotly_chart(fig_sub, use_container_width=True)

        if (sub_data["Profit"] < 0).any():
            losing = sub_data[sub_data["Profit"] < 0]["Sub-Category"].tolist()
            st.info(
                "⚠️ Підкатегорії з негативним прибутком у вибраному періоді: "
                + ", ".join(losing)
                + ". Варто перевірити рівень знижок за цими позиціями."
            )

# --- UA: Таб 5: Знижки vs прибуток ---------------------------------------------
# --- EN: Tab 5: Discounts vs profit --------------------------------------------

with tab_discount:
    with st.container(height=TAB_HEIGHT, border=False):
        st.subheader("Вплив знижок на прибуток")

        fig_scatter = px.scatter(
            df.sample(min(1500, len(df)), random_state=1),
            x="Discount",
            y="Profit",
            color="Category",
            size="Sales",
            opacity=0.6,
            labels={"Discount": "Знижка", "Profit": "Прибуток, $"},
            height=400
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

        corr = df["Discount"].corr(df["Profit"])
        st.caption(f"Коефіцієнт кореляції між знижкою та прибутком: **{corr:.2f}**")

# --- UA: Таб 6: Детальні дані ------------------------------------------------
# --- EN: Tab 6: Detailed data ------------------------------------------------

with tab_table:
    with st.container(height=TAB_HEIGHT, border=False):
        st.subheader("Детальні дані")

        csv_bytes = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Завантажити відфільтровані дані(CSV)",
            data=csv_bytes,
            file_name="superstore_filtered.csv",
            mime="text/csv",
        )

        # UA: Висота таблиці трохи менша за висоту таба, щоб заголовок і кнопка теж помістилися
        # EN: The table height is slightly smaller than the tab height so that the header and button also fit
        
        st.dataframe(
            df.sort_values("Order Date", ascending=False),
            use_container_width=True,
            height=TAB_HEIGHT - 140,
        )
# ----------------------------------------------------------------------
# 7. UA: ПЛАШКА З АВТОРСТВОМ (фіксована, справа знизу)
# 7. EN: AUTHORITY PLAQUE (fixed, bottom right)
# ----------------------------------------------------------------------
st.markdown(
    f"""
    <style>
    .author-badge {{
        position: fixed;
        bottom: 50px;
        right: 18px;
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        padding: 6px 14px;
        font-size: 0.8rem;
        color: #444;
        z-index: 1000;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
    }}
    .author-badge a {{
        color: #1a73e8;
        text-decoration: none;
        font-weight: 600;
    }}
    .author-badge a:hover {{
        text-decoration: underline;
    }}
    </style>

    <div class="author-badge">
        Created by <a href="{AUTHOR_URL}" target="_blank">{AUTHOR_NAME}</a>
    </div>
    """,
    unsafe_allow_html=True,
)
