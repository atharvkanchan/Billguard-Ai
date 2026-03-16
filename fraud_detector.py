def fraud_analysis(gst_valid,duplicate_items):

    score = 0

    if not gst_valid:
        score += 0.5

    if duplicate_items:
        score += 0.5

    return score
