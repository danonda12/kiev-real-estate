import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data: You will replace this with actual data.
data = {
    "Period": ["Pre-Invasion", "Post-Invasion"],
    "One-Bedroom City Center": [650, 350],
    "Three-Bedroom City Center": [1250, 700]
}
df = pd.DataFrame(data)

# Title and Introduction
st.title("Impact of the Russian Invasion on Kiev's Real Estate Market")
st.write("""
Before the Russian invasion, Kiev was a bustling city with a thriving real estate market. 
However, the invasion has significantly impacted the economy and real estate market in Kiev.
""")

# Data Overview
st.header("Rental Price Analysis")
st.write("Comparison of average rent prices for apartments in Kiev's city center, before and after the invasion.")

# Plotting
fig = px.bar(df, x='Period', y=['One-Bedroom City Center', 'Three-Bedroom City Center'], barmode='group')
st.plotly_chart(fig)

# Economic Impact Analysis
st.header("Economic Impact Analysis")
st.write("""
The invasion has not only resulted in a devastating loss of life and destruction but also had a significant impact on Kiev's economy and real estate market.
""")

# Recovery and Future Outlook
st.header("Recovery and Future Outlook")
st.write("""
The future of Kiev and its real estate market remains uncertain, and it will take a long time for the city to recover from the damage that has been inflicted upon it.
""")

# Conclusion
st.header("Conclusion")
st.write("""
The Russian invasion of Ukraine has had a devastating impact on the rental market in Kiev. The once thriving city has now been reduced to a shell of its former self, and the future remains uncertain.
""")

# Run this command in your terminal to start the Streamlit app
# streamlit run kiev_real_estate_app.py
