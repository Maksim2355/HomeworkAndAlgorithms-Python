from src.mnist_loader import load_data_wrapper
from src.utils import *
from matplotlib import pyplot as plt


def noise_img(arr, noise_coefficient):
    new_arr = []
    len_column = len(arr)
    for i in range(len_column):
        new_iter = clamp(arr[i] + noise_coefficient, 0, 1)
        new_arr.append(new_iter)
    return new_arr


tr_data, test_data, size_picture = load_data_wrapper()

weights = np.zeros(size_picture)

lr = 0.1

epochs = 500000

for e in range(epochs):
    for data, target in tr_data:
        if target == 0:
            target = 1
        else:
            target = 0
        x = np.sum(weights * data)
        y = sigmoid(x)
        E = -(target - y)
        weights -= lr * E * y * (1.0 - y) * data

noise_coefficient_arr = [(i / 30) for i in range(0, 6)]
bad_iteration = []

data_x, target_y_arr = test_data
for coefficient in noise_coefficient_arr:
    iter_sum = 1
    iter_good = 0
    iter_bad = 0
    for i in range(len(data_x)):
        new_data = noise_img(data_x[i], coefficient)
        x = np.sum(weights * new_data)
        y = sigmoid(x)
        if target_y_arr[i] == 0:
            iter_sum += 1
            if y > 0.8:
                iter_good += 1
            if y < 0.8:
                iter_bad += 1
    bad_iteration.append(iter_good / iter_sum)
    print("Хорошие итерации", iter_good)
    print("Плохие итерации", iter_bad)

fig, ax = plt.plot(noise_coefficient_arr, bad_iteration)
ax.set_xlabel("Ось X - коэффициент шума", fontsize=14)
ax.set_ylabel("Ось Y - Процент угадываемых значений", fontsize=14)
plt.show()
