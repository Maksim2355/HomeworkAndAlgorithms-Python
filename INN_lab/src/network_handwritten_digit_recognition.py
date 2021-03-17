import numpy as np
from src.utils import *


class Network:
    def __init__(self, train_data: np.ndarray, size_picture: int, epoch=100000):
        """"Иннициализурем нашу нейронную сеть. В конструкторе подаем обучающую выборку размером n
            в @train_data содержится массив с вектором значений пикселей, которые принимают значение 0 или 1
            в @result_data содержится вектор значение из 10 элементов. Это результаты соответствующего
            элемента в @train_data вектор может быть заполнен нулевыми значениями и еденицей
            еденица на позиции k в этом векторе указыает, получившийся массив из 784 значений принимает
            значение k в десятичном формате
            @size_picture говорит о размере каждого элемента массива обучающей выборки. В данном случае
            у нас размер 784
            """
        self.train_data = train_data
        self.sizes_input_layer = size_picture
        self.weight = np.random.rand(10, 784)
        self.lr = 0.01
        self.epoch = epoch

    def train(self):
        for e in range(self.epoch):
            for tr_data, res_data in self.train_data:
                print(res_data)

    def test(self, test_data):
        res_arr = []
