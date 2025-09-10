import json


def tr(content, key, count):
    if count == 0:  # for normal string
        return content[key]
    if count == 1:  # for string with as singular
        return content[key]["one"]
    if count == 2:
        return content[key]["other"]


def translate(key, lang="", count: int = 0):
    if lang == "":
        lang = "en"
    try:
        with open(f"localisations/{lang}.json", mode="r") as f:
            content = json.load(f)
        return tr(key=key, content=content, count=count)
    except:
        lang = "en"
        with open(f"localisations/{lang}.json", mode="r") as f:
            content = json.load(f)
        return tr(key=key, content=content, count=count)
