import streamlit as st
import pandas as pd

st.title('Prophet Educational Tool')

st.write("""
### Upload your CSV data for forecasting
Your CSV should have at least two columns: 'ds' (datestamp) and 'y' (numeric value to forecast).
""")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.write("**Uploaded Data Preview:**")
        st.dataframe(df.head())
        
        # Store the dataframe in session state for later use by Prophet
        st.session_state['data'] = df

        if 'ds' not in df.columns or 'y' not in df.columns:
            st.error("CSV must contain 'ds' and 'y' columns. Please check your file.")
        else:
            st.write("Data seems valid. Ready for Prophet forecasting.")
            # Placeholder for Prophet integration and visualization
            if st.button("Run Prophet Forecast"):
                try:
                    from prophet import Prophet
                    m = Prophet()
                    m.fit(df)
                    future = m.make_future_dataframe(periods=365) # Forecast for 1 year
                    forecast = m.predict(future)
                    
                    st.success("Prophet forecast completed!")
                    st.write("**Forecast Data Preview:**")
                    st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
                    
                    st.write("**Forecast Visualization:**")
                    fig1 = m.plot(forecast)
                    st.pyplot(fig1)
                    
                    st.write("**Forecast Components:**")
                    fig2 = m.plot_components(forecast)
                    st.pyplot(fig2)
                    
                except Exception as e_prophet:
                    st.error(f"Error during Prophet forecasting: {e_prophet}")
        
    except Exception as e:
        st.error(f"Error reading or processing file: {e}")
else:
    st.info("Please upload a CSV file to begin.")