graph = {}
graph["0"] = ["1", "6"]
graph["2"] = ["3", "8"]
graph["3"] = ["4", "5"]
graph["4"] = []
graph["5"] = []
graph["6"] = ["7"]
graph["8"] = ["9"]
graph["9"] = ["0"]

def cond_check(usl):
    if usl == "Отравление":
        return 1
    return 0


