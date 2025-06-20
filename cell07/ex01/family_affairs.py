def find_the_readheads(family_dict):
    readhead = filter(lambda name: family_dict[name] == "red", family_dict)
    return list(redheads)

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginine": "brunette",
        "david": "red",
        "franck": "red"
    }

    print(find_the_readheads(dupont_family))