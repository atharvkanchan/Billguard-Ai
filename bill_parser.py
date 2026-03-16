import re

def parse_bill(text):

    data = {}

    gst_pattern = r'[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][A-Z0-9]Z[A-Z0-9]'
    date_pattern = r'\d{2}/\d{2}/\d{4}'

    gst = re.findall(gst_pattern,text)
    date = re.findall(date_pattern,text)

    data["gst"] = gst[0] if gst else None
    data["date"] = date[0] if date else None

    return data
