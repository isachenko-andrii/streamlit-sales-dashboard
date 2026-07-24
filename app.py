"""
Аналітичний дашборд продажів (Superstore Dataset).
Запуск локально: streamlit run app.py
"""

import pandas as pd
import plotly.express as px
import streamlit as st

# ----------------------------------------------------------------------
# 1. НАЛАШТУВАННЯ СТОРІНКИ
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Аналітика продажів Superstore",
    page_icon="📊",
    layout="wide",
)

DATA_PATH = "data/superstore.csv"


# ----------------------------------------------------------------------
# 2. ЗАВАНТАЖЕННЯ І ПІДГОТОВКА ДАНИХ (з кешуванням)
# ----------------------------------------------------------------------
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="latin-1")

   # Kaggle-версії датасета іноді відрізняються регістром/пробілами в назвах колонок
    df.columns = [c.strip() for c in df.columns]

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

    return df


df_raw = load_data(DATA_PATH)

# ----------------------------------------------------------------------
# 3. БІЧНА ПАНЕЛЬ - ФІЛЬТРИ
# ----------------------------------------------------------------------
st.sidebar.header("Фильтри")

min_date, max_date = df_raw["Order Date"].min(), df_raw["Order Date"].max()
date_range = st.sidebar.date_input(
    "Період замовлень",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

regions = st.sidebar.multiselect(
    "Регіон", options=sorted(df_raw["Region"].unique()), default=sorted(df_raw["Region"].unique())
)

categories = st.sidebar.multiselect(
    "Категорія", options=sorted(df_raw["Category"].unique()), default=sorted(df_raw["Category"].unique())
)

segments = st.sidebar.multiselect(
    "Сегмент клієнтів", options=sorted(df_raw["Segment"].unique()), default=sorted(df_raw["Segment"].unique())
)

# Застосовуємо фільтри
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
st.sidebar.caption(f"Відфільтровано рядків: **{len(df):,}** з {len(df_raw):,}")

# ----------------------------------------------------------------------
# 4. ЗАГОЛОВОК (sticky — прилипает к верху экрана вместе с полоской табов)
# ----------------------------------------------------------------------
bg_color = st.get_option("theme.backgroundColor") or "#ffffff"

st.markdown(
    f"""
    <style>
    .block-container {{
        padding-top: 2.5rem;
    }}

    /* высота встроенной панели Streamlit (Share / ⭐ / ✏️ / GitHub) —
       заголовок должен прилипать НИЖЕ неё, а не к самому верху окна */
    :root {{
        --stheader-height: 2.875rem;
    }}

    /* заголовок + подпись — липнут сразу под панелью Streamlit */
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

    /* полоска вкладок — липнет сразу под заголовком */
    div[data-testid="stTabs"] > div:first-child {{
        position: sticky;
        top: calc(var(--stheader-height) + 3.6rem);   /* подстрой второе слагаемое под фактическую высоту .dashboard-header, если появится нахлёст/зазор */
        background: {bg_color};
        z-index: 998;
        padding-top: 0.3rem;
    }}

     /* крупные KPI (глобально — st.metric больше нигде на дашборде не используется) */
    [data-testid="stMetricValue"] {{
        font-size: 2.3rem;
        color: #1a73e8;
        font-weight: 700;
    }}
    [data-testid="stMetricLabel"] {{
        font-size: 1.05rem;
    }}
    </style>

    <div class="dashboard-header">
        <h1>📊 Аналитический дашборд продаж</h1>
        <p>Датасет: Superstore Sales (Kaggle). Используй фильтры слева, чтобы менять период, регион, категорию и сегмент клиентов.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if df.empty:
    st.warning("По выбранным фильтрам нет данных. Измени условия фильтрации.")
    st.stop()

# ----------------------------------------------------------------------
# 5. KPI-РАСЧЁТЫ (вывод — в отдельном табе, см. шаг ниже)
# ----------------------------------------------------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
avg_order_value = total_sales / total_orders if total_orders else 0
margin_pct = (total_profit / total_sales * 100) if total_sales else 0
# Доля прибыльных заказов считается на уровне заказа (Order ID),
# т.к. один заказ может включать несколько товарных позиций —
# суммируем прибыль по заказу и проверяем, положительная ли она
order_profit = df.groupby("Order ID")["Profit"].sum()
profitable_orders_pct = (order_profit > 0).mean() * 100 if len(order_profit) else 0

# ----------------------------------------------------------------------
# 6. ДИНАМІКА ПРОДАЖІВ У ЧАСІ
# ----------------------------------------------------------------------
TAB_HEIGHT = 520  # px — уменьшено, чтобы шапка + таб помещались в один экран

tab_kpi, tab_trend, tab_breakdown, tab_top, tab_discount, tab_table = st.tabs(
    [
        "🔢 KPI",
        "📈 Динамика",
        "🗂️ Категории и регионы",
        "🏆 Топ подкатегорий",
        "💸 Скидки и прибыль",
        "📋 Данные",
    ]
)

# --- Таб KPI: крупные ключевые метрики --------------------------------
KPI_BOX_HEIGHT = 180  # px — высота каждого блока-показателя; увеличь при желании

with tab_kpi:
    with st.container(height=TAB_HEIGHT, border=False):
        st.markdown('<div class="kpi-tab">', unsafe_allow_html=True)

        st.subheader("Ключевые показатели")

        row1 = st.columns(3)
        with row1[0]:
            with st.container(border=True):
                st.metric("Выручка", f"${total_sales:,.0f}")
        with row1[1]:
            with st.container(border=True):
                st.metric("Прибыль", f"${total_profit:,.0f}")
        with row1[2]:
            with st.container(border=True):
                st.metric("Заказов", f"{total_orders:,}")

        row2 = st.columns(3)
        with row2[0]:
            with st.container(border=True):
                st.metric("Средний чек", f"${avg_order_value:,.0f}")
        with row2[1]:
            with st.container(border=True):
                st.metric("Маржинальность", f"{margin_pct:.1f}%")
        with row2[2]:
            with st.container(border=True):
                st.metric("Доля прибыльных заказов", f"{profitable_orders_pct:.1f}%")

        st.markdown('</div>', unsafe_allow_html=True)

# --- Таб 1: Динаміка продажів у часі -----------------------------------
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

# --- Таб 2: Розбивка за категоріями та регіонами-----------------------------
with tab_breakdown:
    with st.container(height=TAB_HEIGHT, border=False):
        col_left, col_right = st.columns(2)

        with col_left:
            st.subheader("Продаж за категоріями")
            cat_data = df.groupby("Category")[["Sales", "Profit"]].sum().reset_index()
            fig_cat = px.bar(
                cat_data.sort_values("Sales", ascending=True),
                x="Sales",
                y="Category",
                orientation="h",
                text_auto=".2s",
                color="Profit",
                color_continuous_scale="RdYlGn",
                labels={"Sales": "Выручка, $", "Category": ""},
                height=400
            )
            st.plotly_chart(fig_cat, use_container_width=True)

        with col_right:
            st.subheader("Продаж по регіонах")
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

# --- Таб 3: Топ підкатегорій за прибутком-----------------------------------
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

# --- Таб 4: Знижки vs прибуток ---------------------------------------------
with tab_discount:
    with st.container(height=TAB_HEIGHT, border=False):
        st.subheader("Вплив знижки на прибуток")

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

# --- Таб 5: Детальні дані ------------------------------------------------
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

        # Висота таблиці трохи менша за висоту таба, щоб заголовок і кнопка теж помістилися
        st.dataframe(
            df.sort_values("Order Date", ascending=False),
            use_container_width=True,
            height=TAB_HEIGHT - 140,
        )
