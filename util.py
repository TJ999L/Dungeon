def lookup(list, id):
    for item in list:
        if item["id"] == id:
            return item
    return False

def getDisplay(obj, singular=True):
    """
    Use an object's (or array of objects') `display` property to get a display name.
    If `display` is an array, use the first item if singular, the 2nd if plural.
    If there's only one item in the array, use that word for all cases.
    If `display` is a *string*, return that for singular or automatically add an `s` at the end for plural
    """

    if type(obj) == list:
        output = []
        for item in obj:
            output.append(getDisplay(item, singular))
        return output

    field = obj["display"]
    fieldType = type(obj["display"])
    if fieldType == list:
        count = len(field)
        if count == 1:
            return field[0]
        else:
            return field[0] if singular else field[1]
    else:
        return field+("s" if not singular else "")

def inputValidateChoice(message, items, singular=True, doubleCheck=True):
    """
    Let the user select from an array of *objects* using number keys.
    Returns the users final selection (the object from the list).
    You can optionally `doubleCheck=True` to add a confimration message
    """
    options = []
    for (i, item) in enumerate(items):
        options.append(f"({ (i+1) }){getDisplay(item, singular)}")

    choice = input(f"{message} {englishJoin(options, False)} ?")
    try:
        choiceInt = int(choice)
        choiceObject = items[choiceInt-1]
        choiceName = getDisplay(choiceObject, singular)
        finalMessage = f"You chose {choiceName}."
        if doubleCheck :
            confirm = input(finalMessage + " Are you sure? (y/n)").lower()
            if confirm[0] == "y":
                print(f"You settle on {choiceName}.")
                return choiceObject
            else:
                inputValidateChoice(message, items, singular, doubleCheck)
        else:
            print(finalMessage)
        return choiceObject
    except:
        print("Please select one of the options")
        inputValidateChoice(message, items, singular, doubleCheck)


def englishJoin(parts, inclusive=True):
    """ Turn an array into normal oxford comma plain text """
    word = "and" if inclusive else "or"
    count = len(parts)
    if count < 2:
        return "".join(parts)
    if count < 3:
        return (" "+ word +" ").join(parts)
    else:
        return ", ".join(parts[:-1]) + ", " + word + " " + parts[-1]
