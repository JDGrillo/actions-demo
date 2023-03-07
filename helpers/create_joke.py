from helpers.convert_title import convert_title
from helpers.joke_dict import joke_dict


def create_joke(name, title):
    convTitle = ""
    converted_title = convert_title(title)
    return joke_dict[converted_title] + " " + name
