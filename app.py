import streamlit as st

from ocr_utils import extract_text
from bill_parser import parse_bill
from gst_validator import validate_gstin
from fraud_detector import fraud_analysis

st.title("🧾 BillGuard AI")

uploaded_file = st.file_uploader(
    "Upload Bill",
    type=["png","jpg","jpeg"]
)

if uploaded_file:

    st.image(uploaded_file)

    text = extract_text(uploaded_file)

    st.subheader("Extracted Bill Text")
    st.text(text)

    data = parse_bill(text)

    st.subheader("Bill Information")

    st.write("Invoice Number:",data["invoice"])
    st.write("Date:",data["date"])
    st.write("GST:",data["gst"])

    gst_valid = validate_gstin(data["gst"])

    if gst_valid:
        st.success("GST Valid")

    else:
        st.error("GST Invalid")

    fraud_score = fraud_analysis(gst_valid,False)

    st.subheader("Fraud Risk Score")

    st.write(fraud_score)

    if fraud_score > 0.5:

        st.error("⚠ Possible Fraud")

    else:

        st.success("Bill looks normal")
