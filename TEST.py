acro = [[] for c in range(5)]
print(acro)
cipher = "Сосать"
co = 0
for i in cipher:
    if co == len(acro):
        co = 0
    acro[co].append(i)
    co += 1

print(acro)