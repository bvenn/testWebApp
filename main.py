import os
import pandas as pd
import streamlit as st


st.write("Hello my World")

# If the user clicks the "Update" button
if st.button('Update list of stations'):
    # Save the edited DataFrame to a CSV file
    stations_df = pd.read_csv('stations.csv',dtype={'stationID':str})

    st.dataframe(stations_df)