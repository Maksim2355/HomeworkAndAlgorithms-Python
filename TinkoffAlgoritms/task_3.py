N, K, A, B = map(int, input().split())

# Проверка на возможность покупки
k = A // B
if k != 0:
    res = min(K-1, N)
    print(k + k // res)
else:
    print(0)