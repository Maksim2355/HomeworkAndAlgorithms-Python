from collections import deque

graph = {}
graph["food"] = ["fruits", "vegetables"]
graph["fruits"] = ["mango"]
graph["vegetables"] = ["tomato", "cucumber", "apple"]
graph["apple"] = []
graph["mango"] = []
graph["tomato"] = []
graph["cucumber"] = []


def condition_check(fruits_apple):
    if fruits_apple == "apple":
        return 1
    return 0


def search_wide():
    seacrh = deque()
    seacrh += graph["food"]
    while seacrh:
        target = seacrh.popleft() #Извлечение
        if condition_check(target) == 1:
            return print("Удачно нашлось")
        else:
            print(target)
            seacrh += graph[target]
    return print("Ничего не нашлось")

search_wide()
