import re

def validate_gstin(gstin):

    pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][A-Z0-9]Z[A-Z0-9]$'

    return bool(re.match(pattern,gstin))
