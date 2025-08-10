import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Weather Data Dashboard")
file = st.file_uploader("Upload a CSV File", type=["csv"])
if file:
    df = pd.read_csv(file)
    df = df.reset_index().rename(columns={"index": "Index"})
    
    st.subheader("Graphical Visualizations")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Temperature Line Chart"):
            fig, ax = plt.subplots()
            ax.plot(df["Index"].head(20), df["MaxTemp"].head(20), marker="o", color="blue")
            ax.set_xlabel("Day") 
            ax.set_ylabel("Max Temperature")
            ax.set_title("Max Temperature Trend")
            st.pyplot(fig)

    with col2:
        if st.button("Humidity Histogram"):
            fig, ax = plt.subplots()
            ax.hist(df["Humidity9am"], bins=10, color="skyblue", edgecolor="black")
            ax.set_xlabel("Humidity at 9am")
            ax.set_ylabel("Frequency")
            ax.set_title("Humidity Distribution")
            st.pyplot(fig)
    with col3:
        if st.button("Rainfall Bar Chart"):
            fig , ax = plt.subplots()
            ax.bar(df["Index"].head(20),df["Rainfall"].head(20), color="lightblue")
            ax.set_xlabel("Record No")
            ax.set_ylabel("Rainfall (mm)")
            ax.set_title("Rainfall Bar Chart")
            st.pyplot(fig)
    st.subheader("Data Preview")
    st.dataframe(df)
else:
    st.warning("Please upload a CSV file to visualize the weather data.")
