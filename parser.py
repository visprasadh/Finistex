# Finite State Expression Parser Function
# Authored by Vishnuprasadh

def parser(fa, fa_dict):

    fa_dict.update({"start": ""})
    fa_dict.update({"final": []})
    fa_dict.update({"transitions": {}})

    start = final = False # Keeps track of start and final states

    init_tracker = -1 # Keeps track of the beginning of an element string
    end_tracker = -1 # Keeps track of the end of an element string

    state = ""
    key = ""

    for i, x in enumerate(fa):

        if x == "<": continue
        elif x == ">": break

        elif x == "#": 
            start = True
            init_tracker = i+1
        elif x == "*":
            final = True

        elif x == "(":
            end_tracker = i
            state = fa[init_tracker:end_tracker]
            end_tracker = -1
            init_tracker = i+1
            if start:
                fa_dict["start"] = state
                start = False
            if final:
                state = state.replace("*","")
                fa_dict["final"].append(state)
                final = False
            fa_dict["transitions"].update({state: {}})
        elif x == ")":
            state = ""
            init_tracker = i+1

        elif x == "[":
            end_tracker = i
            key = fa[init_tracker:end_tracker]
            init_tracker = i + 1
            end_tracker = -1
            fa_dict["transitions"][state].update({key: []})
        elif x == "]": 
            end_tracker = i
            temp = fa[init_tracker:end_tracker]
            end_tracker = -1
            fa_dict["transitions"][state][key].append(temp)
            init_tracker = i+1

        elif x == ",":
            end_tracker = i
            temp = fa[init_tracker:end_tracker]
            end_tracker = -1
            fa_dict["transitions"][state][key].append(temp)
            init_tracker = i+1

        else:
            continue  

    return fa_dict