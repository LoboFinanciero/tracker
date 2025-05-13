
import streamlit as st
import pandas as pd
import numpy as np # For dummy chart data

# --- Page Configuration ---
st.set_page_config(
    page_title="Stock Prediction Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Main Application ---
st.title("📈 AI Stock Prediction Dashboard")
st.caption("Your intelligent assistant for navigating the stock market.")

# --- Tab Creation ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Portfolio Tops & Drops",
    "💰 Investment Suggestor",
    "📊 Stock Search",
    "ℹ️ About"
])

# --- Tab 1: Portfolio Tops & Drops ---
with tab1:
    st.header("Portfolio: Predicted Tops & Drops")
    st.markdown("Based on our model's latest predictions, here are the stocks expected to see significant movement.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚀 Top Predicted Gainers")
        # Placeholder data - replace with actual model output
        gainers_data = {
            'Ticker': ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'NVDA'],
            'Current Price': [170.34, 280.50, 2500.70, 800.10, 260.25],
            'Predicted Change (%)': [5.2, 4.8, 4.5, 6.1, 3.9],
            'Target Price': [179.20, 293.96, 2613.23, 848.91, 270.39],
            'Confidence': ['High', 'High', 'Medium', 'High', 'Medium']
        }
        gainers_df = pd.DataFrame(gainers_data)
        st.dataframe(gainers_df, use_container_width=True)
        st.caption("*Disclaimer: Predictions are not financial advice.*")

    with col2:
        st.subheader("📉 Top Predicted Decliners")
        # Placeholder data - replace with actual model output
        decliners_data = {
            'Ticker': ['NFLX', 'ZM', 'PTON', 'RBLX', 'COIN'],
            'Current Price': [350.10, 100.20, 25.50, 40.75, 150.90],
            'Predicted Change (%)': [-3.5, -4.2, -5.0, -2.8, -3.1],
            'Target Price': [337.85, 95.99, 24.23, 39.61, 146.22],
            'Confidence': ['Medium', 'High', 'Medium', 'Low', 'Medium']
        }
        decliners_df = pd.DataFrame(decliners_data)
        st.dataframe(decliners_df, use_container_width=True)
        st.caption("*Model updated: 2023-10-27 08:00 AM UTC*")

# --- Tab 2: Investment Suggestor ---
with tab2:
    st.header("💡 Investment Suggestor")
    st.markdown("Enter an amount you'd like to invest, and our model will suggest a diversified portfolio based on predicted growth and risk.")

    investment_amount = st.number_input(
        "Enter amount to invest ($):",
        min_value=100.0,
        max_value=1000000.0,
        value=1000.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Suggest Investments 💸", use_container_width=True):
        if investment_amount >= 100:
            st.subheader(f"Investment Suggestions for ${investment_amount:,.2f}")
            st.info("Generating suggestions... (This is a placeholder - no actual calculation is performed yet)")

            # Placeholder for suggestion logic
            suggestions_data = {
                'Ticker': ['AAPL', 'GOOGL', 'VTI', 'BND'],
                'Asset Class': ['Growth Stock', 'Growth Stock', 'US Equity ETF', 'Bond ETF'],
                'Suggested Allocation (%)': [30, 30, 25, 15],
                'Amount ($)': [
                    investment_amount * 0.30,
                    investment_amount * 0.30,
                    investment_amount * 0.25,
                    investment_amount * 0.15
                ],
                'Rationale': [
                    'Strong growth potential',
                    'Market leader, innovation',
                    'Broad market exposure',
                    'Portfolio stability'
                ]
            }
            suggestions_df = pd.DataFrame(suggestions_data)
            st.dataframe(suggestions_df, use_container_width=True)
            st.success("Portfolio suggestion generated! Remember to do your own research.")
        else:
            st.warning("Please enter an investment amount of at least $100.")

# --- Tab 3: Stock Search ---
with tab3:
    st.header("🔎 Stock Information & Prediction")
    st.markdown("Search for a stock ticker to view its current data, historical performance, and our model's prediction.")

    # Dummy list of tickers for the selectbox
    available_tickers = ["", "AAPL", "MSFT", "GOOGL", "TSLA", "NVDA", "AMZN", "NFLX", "META"]

    search_col1, search_col2 = st.columns([3,1]) # Give more space to search input

    with search_col1:
        ticker_input = st.text_input("Enter Stock Ticker (e.g., AAPL):", placeholder="Type ticker here...").upper()

    with search_col2:
        selected_ticker_dropdown = st.selectbox("Or pick from list:", available_tickers, index=0) # Default to empty

    # Determine which input to use (prefer text input if typed)
    ticker_to_search = ticker_input if ticker_input else selected_ticker_dropdown

    if st.button("Search Stock 🔍", use_container_width=True) or (ticker_to_search and ticker_to_search != ""):
        if ticker_to_search and ticker_to_search != "":
            st.subheader(f"Showing Information for: {ticker_to_search}")

            # Placeholder for fetching stock data
            st.markdown(f"**{ticker_to_search} - Fictional Company Inc.**")

            info_col1, info_col2, info_col3 = st.columns(3)
            with info_col1:
                st.metric(label="Current Price", value="$175.50", delta="+$1.20 (0.69%)")
            with info_col2:
                st.metric(label="Model Prediction (1 Week)", value="BUY", delta="Target: $180.00")
            with info_col3:
                st.metric(label="Market Cap", value="$2.75T")

            st.markdown("---")
            st.subheader("Historical Price Chart (Dummy Data)")
            # Dummy chart data
            chart_data = pd.DataFrame(
                np.random.randn(20, 2) * [5, 1] + [170, 172], # Simulate price around 170 and prediction
                columns=['Actual Price', 'Predicted Price']
            )
            st.line_chart(chart_data)

            st.subheader("Model Insights (Placeholder)")
            st.write(f"""
            - **Trend Analysis:** Positive short-term trend observed.
            - **Key Support Level:** $168.00
            - **Key Resistance Level:** $182.50
            - **News Sentiment:** Moderately Positive (based on recent headlines - *not implemented*)
            - **Volatility:** Medium
            """)

            st.subheader("Recent News (Placeholder)")
            st.write("- Fictional Company Inc. announces new product line.")
            st.write("- Analysts upgrade Fictional Company Inc. to 'Outperform'.")
            st.write("- Market reacts positively to Fictional Company's earnings report.")

        elif not ticker_input and not selected_ticker_dropdown:
            st.warning("Please enter or select a stock ticker to search.")

# --- Tab 4: About ---
with tab4:
    st.header("ℹ️ About This Dashboard & Model")
    st.markdown("""
    This dashboard provides AI-driven stock market insights.
    Our goal is to offer a tool that aids in understanding market trends and potential stock movements.
    """)

    st.subheader("The Prediction Model")
    st.markdown("""
    - **Model Type:** (e.g., LSTM Recurrent Neural Network / Gradient Boosting Machine / Time Series Analysis - ARIMA) - *Specify your model type here*
    - **Data Sources:**
        - Historical stock prices (OHLCV) from (e.g., Yahoo Finance, Alpha Vantage, IEX Cloud).
        - Fundamental data (e.g., P/E ratio, EPS, Market Cap) from (e.g., FinancialModelingPrep).
        - (Optional) Sentiment analysis from news headlines (e.g., NewsAPI, Twitter).
        - (Optional) Macroeconomic indicators (e.g., interest rates, inflation).
    - **Features Used:** (e.g., Lagged prices, trading volume, moving averages, RSI, MACD, sentiment scores).
    - **Prediction Horizon:** (e.g., 1 day, 1 week, 1 month ahead).
    - **Training & Validation:** The model is trained on data up to [Date] and validated on [Date Range]. Performance metrics include [e.g., MAE, RMSE, Accuracy].
    """)

    st.subheader("How to Use")
    st.markdown("""
    - **Portfolio Tops & Drops:** Shows stocks our model predicts will have the largest upward or downward movements.
    - **Investment Suggestor:** Enter a dollar amount to receive a sample portfolio allocation based on risk and growth potential.
    - **Stock Search:** Look up individual stocks for detailed information, historical charts, and specific predictions.
    """)

    st.subheader("Disclaimer")
    st.warning("""
    **This is not financial advice.**
    The predictions and suggestions provided by this dashboard are for informational and educational purposes only.
    Stock market investments carry risk, and past performance is not indicative of future results.
    Always conduct your own thorough research and consult with a qualified financial advisor before making any investment decisions.
    The creators of this dashboard are not liable for any financial losses incurred based on the information presented here.
    """)

    st.markdown("---")
    st.markdown("Developed with ❤️ using Streamlit.")
    st.markdown("Version 0.1.0 (UI Demo)")

# --- Optional: Sidebar for general info or controls ---
# st.sidebar.header("Controls")
# st.sidebar.selectbox("Select Market:", ["US", "Global (Placeholder)"])
# st.sidebar.info("This is a demo application. Predictions are illustrative.")
