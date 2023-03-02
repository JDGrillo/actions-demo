def convert_title(title):
    if "Software" in title:
        return "Software"
    if "CEO" in title:
        return "CEO"
    if "Accountant" in title:
        return "Accountant"
    return "Generic"
