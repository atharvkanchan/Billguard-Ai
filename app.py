import streamlit as st
import re
from ocr_utils import extract_text
from gst_validator import validate_gstin
from fraud_detector import calculate_fraud_score

st.title("🧾 BillGuard AI")

uploaded_file = st.file_uploader("Upload Bill", type=["png","jpg","jpeg"])

if uploaded_file:

    text = extract_text(uploaded_file)

    st.subheader("Extracted Text")
    st.write(text)

    gst_pattern = r'[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][A-Z0-9]Z[A-Z0-9]'
    gst_found = re.findall(gst_pattern,text)

    gst_valid = False

    if gst_found:
        gst_valid = validate_gstin(gst_found[0])
        st.write("GST Found:",gst_found[0])

    fraud = calculate_fraud_score(gst_valid,False,False)

    st.write("Fraud Score:",fraud)
