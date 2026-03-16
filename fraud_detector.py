def calculate_fraud_score(gst_valid,duplicate,price_anomaly):

    score = 0

    if not gst_valid:
        score += 0.4

    if duplicate:
        score += 0.3

    if price_anomaly:
        score += 0.3

    return score
