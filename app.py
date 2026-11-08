
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cafe Sales Dashboard",
    page_icon="☕",
    layout="wide"
)

st.title("Cafe Sales Dashboard")
st.write("Coffee Shop Sales Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv("cafe_sales.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

branches = sorted(df["branch"].unique())

selected_branch = st.selectbox(
    "Select a Branch",
    branches
)

branch_data = df[df["branch"] == selected_branch]

total_revenue = branch_data["total_sar"].sum()

st.metric(
    "Total Revenue",
    f"{total_revenue:,.0f} SAR"
)

product_revenue = (
    branch_data.groupby("product")["total_sar"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("Revenue by Product")

st.bar_chart(product_revenue)
