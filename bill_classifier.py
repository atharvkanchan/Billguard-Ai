def classify_bill(text):

    text = text.lower()

    if "pharmacy" in text or "medicine" in text:
        return "Medical"

    if "restaurant" in text or "food" in text:
        return "Restaurant"

    if "tax invoice" in text:
        return "GST Invoice"

    return "General"
