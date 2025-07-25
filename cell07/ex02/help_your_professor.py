def average(scores_dict):
    if not score_dict:
        return 0
    total = sum(scorees_dict.values())
    count = len(scorees_dict)
    return total / count

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3c = {
    "queentin" : 17,
    "julie" : 15,
    "marc" : 8,
    "stephanie" : 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")