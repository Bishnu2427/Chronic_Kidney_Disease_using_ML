import streamlit as st
from CKD_Main import pred_main

selection = st.sidebar.selectbox("Who are you?", ("Normal Person", "CKD Patient"))
kft = st.sidebar.selectbox("Do you have your latest report?", ("Yes", "No"))

if selection == "CKD Patient":
    if kft == "Yes":
        pred_main()
    else:
        st.error("Kindly provide your latest KFT report for accurate prediction.")
else:
    st.write("Take proper water is highly adviced for future.........")