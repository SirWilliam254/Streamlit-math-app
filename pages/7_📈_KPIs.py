import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Define some helper functions for calculating KPIs
def total_sales(df):
    return df['sales_price'].sum()

def avg_sales(df):
    return df['sales_price'].mean()

def avg_ratings(df):
    return df['rating'].mean()

def avg_sales_per_transaction(df):
    return df['sales_price'].sum() / df['customer_id'].nunique()

def monthly_sales(df):
    df['date'] = pd.to_datetime(df['date'])
    return df.groupby(pd.Grouper(key='date', freq='M'))['sales_price'].sum()

def yearly_profit(df):
    df['date'] = pd.to_datetime(df['date'])
    return df.groupby(pd.Grouper(key='date', freq='Y'))['profit'].sum()

def yearly_ratings(df):
    df['date'] = pd.to_datetime(df['date'])
    return df.groupby(pd.Grouper(key='date', freq='Y'))['rating'].mean()

#App
#df = pd.read_csv("sales_data.csv", index_col=False)
#sales_data = st.file_uploader("Upload CSV", type=["csv"])
url = 'https://raw.githubusercontent.com/SirWilliam254/KPI/main/sales_data.csv'
df = pd.read_csv(url, index_col=False)
if df is not None:
#    df = pd.read_csv(sales_data, index_col=False)
    st.write("Original DataFrame:")
    st.write(df.head())
    # Define some constants for the range slider
    MIN_PRICE = df['sales_price'].min()
    MAX_PRICE = df['sales_price'].max()

    # Define the sidebar
    st.sidebar.header('Filters')
    location_filter = st.sidebar.multiselect('Select location', df['origin_country'].unique(), default=df['origin_country'].unique())
    price_filter = st.sidebar.slider('Select price range', int(MIN_PRICE), int(MAX_PRICE), (int(MIN_PRICE), int(MAX_PRICE)))
    rating_filter = st.sidebar.slider('Select rating range', 0.0, 5.0, (0.0, 5.0))

    # Filter the data based on the sidebar inputs
    filtered_data = df[
        (df['origin_country'].isin(location_filter)) &
        (df['sales_price'] >= price_filter[0]) &
        (df['sales_price'] <= price_filter[1]) &
        (df['rating'] >= rating_filter[0]) &
        (df['rating'] <= rating_filter[1])
    ]

    # Calculate the KPIs
    ts = total_sales(filtered_data)
    as_ = avg_sales(filtered_data)
    ar = avg_ratings(filtered_data)
    asp = avg_sales_per_transaction(filtered_data)
    ms = monthly_sales(filtered_data)
    yp = yearly_profit(filtered_data)
    yr = yearly_ratings(filtered_data)
    star_rating = ":star:" * int(round(ar, 0))
    # Display the KPIs
    st.title(":seedling: KPIs")
    

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Average Sales:")
        st.subheader(f"US $ {as_:,}")
    with middle_column:
        st.subheader("Average Rating:")
        st.subheader(f"{ar} {star_rating}")
    with right_column:
        st.subheader("Total Sales:")
        st.subheader(f"US $ {ts:,}")
    st.write(f'Average Sales per Transaction: ${asp:.2f}')

    st.title(":chart_with_upwards_trend: Plots")
    # Display the monthly sales plot
    st.write('## Monthly Sales')
    chart = alt.Chart(ms.reset_index()).mark_line().encode(
        x='date',
        y='sales_price'
    ).properties(
        width=600,
        height=400
    )
    st.altair_chart(chart)

    # Display the yearly profit and ratings bar charts
    st.write('## Yearly Profit and Ratings')
    chart1 = alt.Chart(yp.reset_index()).mark_bar().encode(
        x='date',
        y='profit'
    ).properties(
        width=300,
        height=400
    )
    chart2 = alt.Chart(yr.reset_index()).mark_bar().encode(
        x='date',
        y='rating'
    ).properties(
        width=300,
        height=400
    )
    st.altair_chart(chart1 | chart2)