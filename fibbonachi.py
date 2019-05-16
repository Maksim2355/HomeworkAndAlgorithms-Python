n = int(input())

def fibbonachi(n):
    if n <= 1:
        return 1
    else:
        return fibbonachi(n-1) + fibbonachi(n-2)

print(fibbonachi(n))