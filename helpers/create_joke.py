from helpers.joke_dict import joke_dict


def create_joke(name, title):
    lower_title = title.lower()
    if lower_title in joke_dict:
        return joke_dict[lower_title] + " " + name
    return joke_dict["generic"] + " " + name
