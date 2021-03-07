from numpy import *
from data import arr_stat_b0
from variation_series import ElementVariationSeries
from ascii_table import print_pretty_table
from creater_graphics import *

# start_interval = int(input("Введите начальное значение интервала"))
# length_interval = int(input("Введите длинну интервала"))
# N = int(input("Введите размер выборки"))
eps = 0.001
os = abs(str(eps).find('.') - len(str(eps))) - 1

start_interval = 59
length_interval = 2
N = 200
sampling_values = array(arr_stat_b0, int)
end_interval = max(sampling_values)

element = start_interval
j = start_interval + (length_interval - 1)
variation_series = []
while True:
    variation_series.append(
        ElementVariationSeries(element, j, relative_frequency=0, particularity=0, accumulated_particularity=0,
                               accumulated_frequency=0)
    )
    element = j + 1
    if j > end_interval:
        break
    j += length_interval

acmltd = 0
for el in variation_series:
    for smpl in sampling_values:
        if el.min_interval <= smpl <= el.max_interval:
            el.relative_frequency += 1
    acmltd += el.relative_frequency
    el.accumulated_frequency = acmltd
    el.particularity = round(el.relative_frequency / N, os)

sum_xi = 0
accumulated = 0
for el in variation_series:
    accumulated += el.particularity
    el.accumulated_particularity = round(accumulated, os)

# Рисуем таблицу
table_data = [
    ['Xi', 'Ni', 'Частость Wi = Ni/N', "Накопленная частость"]
]
for vs in variation_series:
    table_data.append(vs.values())
print_pretty_table(table_data)

particularity = [i.particularity for i in variation_series]
smpl = [[i.min_interval, i.max_interval] for i in variation_series]

plot_histogram(smpl, particularity)

accumulated_particularity = [i.accumulated_particularity for i in variation_series]
plot_polygon(smpl, accumulated_particularity)

x_average = 0
for element in variation_series:
    x_average += ((element.min_interval + element.max_interval) / 2) * element.particularity
print(f'Среднее выборочное {x_average}')

D = 0
Me = 0
for i in variation_series:
    D += i.particularity * ((((i.min_interval + i.max_interval) / 2) - x_average) ** 2)

for i in range(len(variation_series)):
    if variation_series[i].accumulated_particularity >= 0.5:
        Me = variation_series[i].min_interval + length_interval * (
                (0.5 * N - variation_series[i - 1].accumulated_frequency) / variation_series[i].relative_frequency)
        break

max_particularity = max(particularity)
Mo = 0
for i in range(len(variation_series)):
    if variation_series[i].particularity == max_particularity:
        Mo = variation_series[i].min_interval + length_interval * (
                (variation_series[i].relative_frequency - variation_series[i - 1].relative_frequency) / (
                (2 * variation_series[i].relative_frequency) - (
                             variation_series[i - 1].relative_frequency - variation_series[i + 1].relative_frequency)))
        Mo = int(Mo)
        break

print(f'Выборочная дисперсия {D}')
print(f'Медиана {Me}')
print(f'Мода {Mo}')
