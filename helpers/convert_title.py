def convert_title(title):
    if ("Software" in title):
        return "Software"
    elif ("CEO" in title):
        return "CEO"
    elif ("Accountant" in title):
        return "Accountant"
    else:
        return "Generic"
