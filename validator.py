# Input String validation function
# Authored by Vishnuprasadh

def validator(input_string, fa_dict):

    current_state = [fa_dict["start"]]
    is_valid = False

    for x in input_string:
        print(current_state, end = "->")
        temp = []
        copycat = current_state.copy()
        for y in current_state:
            if x in fa_dict['transitions'][y]:
                temp += fa_dict['transitions'][y][x]
            copycat.pop(0)
        current_state = copycat.copy()
        current_state += temp

    print(current_state)

    for z in current_state:
        if z in fa_dict["final"]:
            is_valid = True
            break

    if is_valid:
        print("String accepted")
    else:
        print("String rejected")