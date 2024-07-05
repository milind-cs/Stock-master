import streamlit as st
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Stock Master: Your ML-Powered Stock Predictor",
    page_icon="📈",
    layout="wide"
)

# Title and subtitle
st.title("Stock Master: Your ML-Powered Stock Predictor")
st.markdown("#### Transforming Stock Predictions with Machine Learning")

# Introduction
st.header("Welcome to Stock Master! 📈")
st.markdown("""
Discover the power of machine learning in stock price prediction with **Stock Master**. This app leverages cutting-edge ML models to forecast stock prices, providing you with the insights needed to make informed investment decisions.
""")

# How It's Built section
st.header("Under the Hood of Stock Master 🏗️")
st.markdown("""
Stock Master is engineered with a robust stack of tools and technologies:

- **Streamlit**: Crafts a seamless and interactive user interface.
- **YFinance**: Fetches comprehensive financial data from the Yahoo Finance API.
- **StatsModels**: Builds and fine-tunes the ARIMA time series forecasting model.
- **Plotly**: Generates dynamic and interactive financial charts.

### App Workflow:

1. **Select a Stock Ticker**: Choose the stock you're interested in.
2. **Data Retrieval**: Historical data is fetched from Yahoo Finance.
3. **Model Training**: The ARIMA model is trained on the historical data.
4. **Forecast Generation**: The model predicts future stock prices.
5. **Visualization**: Forecasts and historical data are plotted with Plotly for easy interpretation.
""")

# Key Features section
st.header("Key Features of Stock Master 🎯")
st.markdown("""
- **Real-Time Data**: Access up-to-the-minute stock prices and financial metrics.
- **Interactive Charts**: Explore historical trends and future forecasts with interactive visualizations.
- **Robust Predictions**: Utilize ARIMA for reliable and statistically sound forecasting.
- **Performance Evaluation**: Backtest models to evaluate prediction accuracy.
- **Mobile-Friendly Design**: Experience a responsive design that works seamlessly across all devices.
""")

# Call to Action
st.markdown("**Ready to see the future of your favorite stocks? Select a stock ticker from the sidebar and let Stock Master do the rest!**")
