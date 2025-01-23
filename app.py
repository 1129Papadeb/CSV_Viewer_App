import streamlit as st
import pandas as pd

# Set the title of the app
st.title("CSV Viewer and Basic Stats")

# Create a file uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.write("### Uploaded Data")
    st.write(df)

    # Display basic statistics
    st.write("### Basic Statistics")
    st.write(df.describe())

    # Display the column names
    st.write("### Column Names")
    st.write(df.columns.tolist())

    # Allow the user to select a column for more detailed stats
    column = st.selectbox("Select a column for more stats", df.columns)

    if column:
        st.write(f"### Statistics for {column}")
        st.write(f"Mean: {df[column].mean()}")
        st.write(f"Median: {df[column].median()}")
        st.write(f"Standard Deviation: {df[column].std()}")

