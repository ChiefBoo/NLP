# -*- coding: utf-8 -*-
"""softgrader_tasks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dnlt76CNMZUonG88qtQk8ZeqN0gL39cu

#Задание 1
Условие
Для решения задачи необходимо найти все стандартные типы в Python.

Требования
Решение должно реализовывать единственную функцию 
get_objects()
, которая должна возвращать список (list) из объектов, каждый из которых уникального типа.

Формат входа
Входных данных нет

Формат выхода
Список из объектов, каждый из которых уникального типа. Объекты должны быть упорядочены в лексикографическом порядке названий их типов.
"""

import math
def get_objects():
  data = [[], dict(), 1, 'hi', 2.1, True, tuple(), set(), type, None, bytearray(), bytes(), 3 + 4j,
          frozenset(), range(4,5), reversed('hi'), object(), property(), GeneratorExit(), FutureWarning(), 
          FloatingPointError(), filter(None,'hi'), FileNotFoundError(), FileExistsError(), Exception(),
          EOFError(), EnvironmentError(),DeprecationWarning(), slice('hi'), staticmethod(None), zip(), 
          classmethod(None), map('hi', 'it'), memoryview(b'abc'), enumerate(b'abc'), iter('abc'), get_objects,
          ValueError(), NameError(), TypeError(), (x for x in range(1,2)), math, str.title, iter([]), iter({}),
          iter(set()), dir]
  
  data_types = sorted(data, key=lambda x: str(type(x)))
  return data_types

"""#Задание 2


Условие
Для сортировки в методе 
sorted
 есть параметр 
key
. Он принимает объект, который с помощью call получает для сортируемого объекта ключ, задающий порядок сортировки. Но иногда так бывает, что требуется компаратор, принимающий 2 объекта для сравнения. В данной задаче предлагается реализовать функцию, которая позволяет “преобразовать” произвольный бинарный компаратор в унарный объект 
key
.

Требования
Ваш код должен реализовывать единственную функцию 
cmp_to_key(comparator)
, аргументом которой является бинарная функция 
comparator
. В результате работы 
cmp_to_key
 возвращает объект, который можно передать как параметр 
key
 в встроенную функцию 
sorted
.

Формат входа
На входе 
comparator(x, y)
 — бинарная функция, сравнивающая 2 объекта и возвращающая 
−
1
 (если 
x < y
), 0 (если x == y), + 1 (если x > y)

Формат выхода
На выходе ожидается объект, у которого есть оператор (), позволяющий отобразить аргумент оператора в key.


"""

def cmp_to_key(comparator):
  class Compare(object):
    def __init__(self, obj):
      self.obj = obj
    def __lt__(self, other):
      return comparator(self.obj, other.obj) < 0
    def __gt__(self, other):
      return comparator(self.obj, other.obj) > 0
    def __eq__(self, other):
      return comparator(self.obj, other.obj) == 0
  return Compare

"""#Задание 3

Условие
В данной задаче нужно написать наследника класса 
list
 и реализовать оператор деления на число. Как работает оператор деления списка на число? Так как существует много определений, выберем одно из них.

Определим операцию деления списка из 
n
 элементов на натуральное число 
k
, как список состоящий из 
k
 списков таких, что выполняются 3 условия:
1. максимальная разница между длинами списков минимальна;
2. последовательная конкатенация списков даёт исходный список;
3. списки упорядочены по невозрастанию их длин.

Требования
Код должен реализовывать 
class list_divider
, являющийся насследником класса 
list
 и имплементирующим оператор деления на число (
/
). Оператор деления на число должен возвращать список, состоящий из списков, состоящих из элементов исходного списка в соответствии с условием задачи. В случае неверных типов операндов программа должна генерировать исключение 
TypeError
, а в случае невозможности проведения операции 
−
 
ValueError
"""

class list_divider(list):

    def __init__(self, list_):
        self.list_ = list_
        
    def __truediv__(self, other):
        if not isinstance(self.list_, list) or not isinstance(other, int):
          raise TypeError
        if other < 1:
          raise ValueError
        split_list = self.split(self.list_, other)     
        return split_list
            
    def split(self, list_, spl):
        div, mod = divmod(len(list_), spl)
        return [list_[i * div + min(i, mod):(i + 1) * div + min(i + 1, mod)] for i in range(spl)]

"""#Задание 4

Условие
В одном из научных проектов в области биофинорматики возникла задача фильтрации данных из таблицы по некоторой системе критериев. Таблица состоит из нескольких колонок, среди которых интересными для пользователя являются 7. Исходно названия колонок имеют сложный замысловатый вид, поэтому для каждой колонки дано новое название (после символа двоеточие):


ID_REF: cpgs
CHR: chr
UCSC_REFGENE_NAME: gene
RELATION_TO_UCSC_CPG_ISLAND: geotype
CROSS_R: crossr
Class: class
UCSC_REFGENE_GROUP: genepart


Пример таблицы можно скачать по ссылке.
Требования
Ваш код должен реализовывать класс 
cpgs_annotation
 с конструктором, принимающим на вход 2 аргумента:
1) таблицу, представляющую собой список списков по строкам элементов таблицы;
2) список исходных имён столбцов.

Класс должен реализовывать метод 
get_cpgs
, принимающий на вход один аргумент - словарь из критериев и возвращающий 2 списка:
1) список имён из колонки cpgs для отфильтрованных строк таблицы;
2) список индексов (в 0-индексации) для отфильтрованных строк таблицы.

Метод должен осуществить фильтрацию таблицы по критериям, при чём все критерии объединены операцией логического И. Таким образом, найденные CpG сайты должны удовлетворять каждому из критериев. Рассмотрим 2 вида критериев 
in и out
. Критерий типа 
in
 позволяет выбрать строки, в которых есть хотя бы одно из значений критерия. Критерий типа 
out
 выбирает те строки, в которых не содержится ни одного из значений критерия. Если элемент оказался в обоих типах критерия, то 
out
 имеет больший приоритет.

Класс не должен содержать других публичных методов или аттрибутов. Некорректно составленные критерии программа должна игнорировать без ошибок.

Формат входа
Элементы исходной таблицы могут быть трёх типов: 
str
, 
int
, 
float
. Некоторые элементы исходной таблицы представлены строкой с разделителем 
;
, что означает принадлежность строки таблицы к каждому из классов. Например строка ‘
AMDHD2;ATP6V0C;AMDHD2
’ означает принадлежность двум классам: 
AMDHD2
 и 
ATP6V0C


Критерии для фильтрации представляют собой словарь с ключами имен столбцов, по которым осуществляется фильтрация, плюс один из типов фильтров ‘
_in
’, ‘
_out
’.
Пример: ‘
cpgs_in
’, ‘
chr_out
’.

В качестве значения в словаре хранится либо элемент, либо список элементов. Элемент может быть типов 
int
 или 
str
. Так же возможно единственное значение типа 
float - NaN
.

Значения NaN в списке критериев необходимо игнорировать.

Примеры входных данных
Примеры критериев:


1. {‘gene_in’: ‘TMEM49’}
2. {‘gene_in’: [‘TMEM49’, ‘HAGH’, ‘POLE3’, ‘PKD1L3’, ‘PNPLA6’]}
3. {‘gene_out’: [‘TMEM49’], ‘gene_in’: [‘PNPLA6’], ‘cpgs_in’: [‘cg00000029’, ‘cg00031443’]}
4. {‘gene_out’: float(‘nan’), ‘chr_in’: ‘7’}

Примеры тестовых данных
Примеры критериев:


#	Критерий	Отфильтрованные CpG
1	{‘gene_in’: ‘TMEM49’}	[‘cg00002749’, ‘cg00040016’]
[64, 988]
2	{‘gene_in’: [‘TMEM49’, ‘HAGH’, ‘POLE3’, ‘PKD1L3’, ‘PNPLA6’]}	[‘cg00002749’, ‘cg00031443’, ‘cg00032036’, ‘cg00038167’, ‘cg00040016’, ‘cg00046913’, ‘cg00047469’, ‘cg00047683’, ‘cg00070052’, ‘cg00098239’, ‘cg00340921’, ‘cg00401032’, ‘cg00435006’, ‘cg00452393’]
[64, 782, 795, 947, 988, 1150, 1160, 1164, 1647, 2313, 7202, 8483, 9191, 9535]
3	{‘gene_out’: [‘TMEM49’], ‘gene_in’: [‘PNPLA6’], ‘cpgs_in’: [‘cg00000029’, ‘cg00031443’]}	[‘cg00031443’]
[782]
4	{‘gene_out’: float(‘nan’), ‘chr_in’: ‘7’}	[‘cg00002531’, ‘cg00003994’, ‘cg00006414’, ‘cg00006884’, ‘cg00009293’, …, ‘cg00470154’, ‘cg00470277’, ‘cg00471159’, ‘cg00471857’]
[57, 92, 154, 160, 222, …, 9955, 9978, 9991]

Формат выхода
В результате функция должна вернуть 2 списка:
1) список имён из колонки 
cpgs
 для отфильтрованных строк таблицы;
2) список индексов (в 0-индексации) для отфильтрованных строк таблицы.

Элементы в списках должны быть упорядочены по возрастанию индекса строк в таблице.

Ограничения на размер задачи
Это первая версия задачи. Количество строк в таблице не более 
10
4
. Критериев в одном фильтре не более 
10
. Количество элементов в одном критерии не более 
100
. Один тест может состоять из не более чем 
30
 запусков 
get_cpgs
 и одного вызова конструктора.


"""

import pandas as pd
import math

class cpgs_annotation:

  def __init__(self, table_, column_names_):
    self.table = pd.DataFrame(data=table_, columns= column_names_)
    self.new_names = {
        'cpgs': 'ID_REF',
        'chr': 'CHR',
        'gene': 'UCSC_REFGENE_NAME',
        'geotype': 'RELATION_TO_UCSC_CPG_ISLAND',
        'crossr': 'CROSS_R',
        'class': 'Class',
        'genepart': 'UCSC_REFGENE_GROUP'
    }
  
  def get_cpgs(self, criteria):
    table_set = self.table.applymap(lambda x: set(x.split(';')) if type(x) is str else {x})    
    filtered_index_cpgs = None

    for crit_key, crit_values in criteria.items():
      if type(crit_values) is str or type(crit_values) is float or type(crit_values) is int:
        crit_values = {crit_values}
      else:
        crit_values = set(crit_values)
      if '_' in crit_key:
        crit_name, crit_type = (crit_key).split('_')
      else: continue
      
      if crit_name in self.new_names:      
        if crit_type == 'in':      
          if any(type(x) is float and math.isnan(x) for x in crit_values):
             filtered_indexes = table_set[self.new_names[crit_name]].map(lambda x: bool(x.intersection(crit_values)))
             filtered_indexes_float = table_set[self.new_names[crit_name]].map(lambda x: (type(x) is float and math.isnan(x)))
             filtered_indexes = filtered_indexes | filtered_indexes_float
          else:
            filtered_indexes = table_set[self.new_names[crit_name]].map(lambda x: bool(x.intersection(crit_values)))

        elif crit_type == 'out':
          if any(type(x) is float and math.isnan(x) for x in crit_values):
            filtered_indexes = table_set[self.new_names[crit_name]].map(lambda x: not bool(x.intersection(crit_values)))
            filtered_indexes_float = table_set[self.new_names[crit_name]].map(lambda x: not (type(x) is float and math.isnan(x)))
            filtered_indexes = filtered_indexes & filtered_indexes_float
          else:
            filtered_indexes = table_set[self.new_names[crit_name]].map(lambda x: not bool(x.intersection(crit_values)))
        else:
          continue
        if filtered_index_cpgs is None:
          filtered_index_cpgs = filtered_indexes
        else:
          filtered_index_cpgs =  filtered_index_cpgs & filtered_indexes
      else:
        continue
    if filtered_index_cpgs is None:
      filtered_index_cpgs = np.ones((len(table_set),), dtype = np.bool)
    filtered_rows_cpgs = self.table[self.new_names['cpgs']][filtered_index_cpgs]
    return list(filtered_rows_cpgs.values), list(filtered_rows_cpgs.index.values)

"""#Задание 5

Условие
При разработке алгоритма построения графа по набору семплов возникла задача быстрого и удобного перебора пар вершин. Есть неориентированный граф из 
n
 вершин. Необходимо перебрать все возможные пары вершин в графе по одному разу. Задача усложняется тем, что перебор необходимо осуществлять параллельно на 
p
 процессах. Из-за этого необходимо уметь разбивать перебор на 
p
 примерно равных частей. Воспользуемся тем же принципом разбиения, как это было рассмотренно в задаче List divider с линейным порядком на парах 
(x, y)
.

Требования
Программа должна реализовывать класс 
graph_partition
 с конструктором, принимающим 2 аргумента: номер процесса и количество процессов. Также класс должен иметь метод 
fit
, принимающий на вход количество вершин в графе. Класс должен быть итератором с известной длиной.

В результате работы итератора должен быть получен набор всех пар элементов, перебираемых на процессе с заданным номером в порядке возрастания. Одна пара представляет собой объект типа 
tuple
.

Ограничения на размер задачи
Количество вершин 
n
 в графе может достигать 
100000
. Такие графы возникают например при обработке данных метилирования ДНК.
Количество процессов 
n
2
−
10
≤
p
≤
3
n
2
+
10
.

Примеры тестовых данных

#	Количество вершин	Номер процесса	Количество процессов	Пары
1	3	0	2	(0, 1)
(0, 2)
2	10	2	4	(2, 9)
(3, 4)
(3, 5)
(3, 6)
(3, 7)
(3, 8)
(3, 9)
(4, 5)
(4, 6)
(4, 7)
(4, 8)

"""

class graph_partition:
  def __init__(self, number_process, amount_processes):
    self.number = number_process
    self.amount = amount_processes
    self.cur = -1
  
  def fit(self, amount_vertices):
    self.amount_vertices = amount_vertices
    div, mod = divmod(sum([i for i in range(amount_vertices)]), self.amount )
    self.processes = [div for i in range(self.amount)]
    for i in range(mod):
      self.processes[i] += 1    

    number = sum(self.processes[:self.number])
    num = amount_vertices - 2   
    for j in range(0,amount_vertices-1):
      if number - 1 <= num:
        self.a, self.b = j, amount_vertices - 1 - num + number - 1
        break
      else:
        num += (amount_vertices - 2 - j)
    return self

  def __iter__(self):
    return self

  def __len__(self):
    return self.processes[self.number]


  def __next__(self):
    self.cur += 1
    if self.cur < self.processes[self.number]:
      cur = self.b + 1
      if cur < self.amount_vertices:
        self.b = cur
      else:
        self.a, self.b = self.a + 1, self.a + 2 
      return tuple((self.a, self.b))
    else:
      raise StopIteration

"""#Задание 6

Условие
Анализ метилирования ДНК требует высокопроизводительных ресурсов. Иногда даже их не хватает, если ваш код не оптимален. В данной задаче предложен упрощённый вариант проблемы, возникшей в научно-исследовательской работе.

Рассмотрим два вектора 
x
,
y
 и матрицу 
a
i
j
=
x
i
⋅
y
j
,
i
=
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
0
,
n
−
1
,
j
=
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
0
,
m
−
1
. При частичном переборе элементов этой матрицы необходимо фильтровать неподходящие пары 
(
i
,
j
)
. Пара 
(
i
,
j
)
 считается неподходящей, если не выполнено условие:
min_score
<
∑
i
k
=
0
∑
j
l
=
0
a
k
l
∑
n
−
1
k
=
0
∑
m
−
1
l
=
0
a
k
l
<
max_score
Требования
Программа должна реализовывать класс с конструктором с двумя аргументами: 
min_score
, 
max_score
.
 Также метод 
fit
 с тремя аргументами: списки 
x
,
y
 и 
iterable
 объект, перебирающий некоторые пары 
(
i
,
j
)
.
Класс должен реализовывать генератор внутри метода 
__iter__
.
При использовании экземпляра класса 
score_filter
 как iterable, объект должен возвращать в том же порядке только те элементы из исходного 
iterable
, которые удовлетворяют критерию из условия задачи.
q
=
len(iterable)
Ограничения на размер задачи
3 группы тестов:
1. 
n
≤
100
,
m
≤
100
,
q
≤
50

2. 
n
≤
100
,
m
≤
100
,
q
≤
10
4

3. 
n
≤
10
5
,
m
≤
10
5
,
q
≤
10
4

"""

from itertools import accumulate
class score_filter:

  def __init__(self, min_score_, max_score_):
    self.min_score = min_score_
    self.max_score = max_score_
  
  def fit(self, x, y, iterable_obj):
    x = list(accumulate(x))
    y = list(accumulate(y))
    self.answer = [(i,j) for i,j in iterable_obj 
                   if self.min_score < (x[i]*y[j])/(x[len(x)-1]*y[len(y)-1]) < self.max_score ]
    return self

  def __iter__(self):
    return (i for i in self.answer)

"""#Задание 7
*Неправильно работает*

Легенда
В процессе исследования мозга на клеточном уровне было обнаружено, что глиальные клетки составляют около 50% головного мозга и оказывают влияние на передачу информации между нейронами. Дальнейший анализ молекулярных механизмов влияния на нейрональную активность выявил важную роль кальциевой активности астроцитов (один из видов глаильных клеток). Высвобождая кальций из сомы клетки, астроциты могут кодировать информацию и обмениваться ей по отросткам внутри астроцитарной сети. Через молекулярный каскад астроцит в месте присоединения к синапсу может модулировать передачу информации между нейронами. Нарушение механизма такой модуляции может приводить к появления нейродегенеративных заболеваний.

В связи с этим возникает задача анализа кальциевой активности астроцитов. И одна из задач, которая встает при анализе изображений это построение базовой линии кальциевой активности для определения наличия или отсутствия кальциевых событий.

Задача
Дана 3-ёх мерная матрица 
V
 размера 
N
×
M
×
T
, представляющая собой набор из 
T
 изображений размера 
N
×
M
 значений концентрации кальция в данной точке (исходный сигнал) и матрица 
F
 размера 
N
×
M
 для оценки максимального разброса шумовой компоненты относительно базовой линии. Необходимо построить базовую линию кальциевого сигнала, медленно изменяющуюся во времени, относительно которой происходит увеличение кальциевой активности.

Для решения задачи был предложен эвристический итеративный алгоритм, состоящий из трех этапов. Алгоритм применяется для каждого пикселя 
(
i
,
j
)
 в отдельности:
0. Начальное значение для базовой линии для данного пикселя выбирается равным исходному сигналу: 
B
0
i
j
t
=
V
i
j
t


1. В качестве текущей оценки базовой линии 
B
s
i
j
t
 вычисляется скользящее среднее по времени с заданным окном 
W
 для нижней огибающей исходного сигнала и базовой линии.
2. Оценка величины “нижнего разброса” 
D
i
j
 для исходного сигнала относительно текущей базовой линии.
3. Остановка алгоритма при величине “нижнего разброса” 
D
i
j
 ниже заданного значения 
F
i
j
, либо при достижении заданного числа итераций 
P
, иначе 
s
=
s
+
1
 и переход на шаг 1.

Результатом алгоритма является сформированная матрица 
B
i
j
t
, получившаяся на последнем шаге алгоритма.

Уточнение терминов:
1. Нижняя огибающая для двух дискретных наборов точек 
x
i
,
y
i
 это такой набор точек 
z
i
, что каждая точка совпадает с одной из соответствующих точек 
x
i
 или 
y
i
, при чем ни одна из точек исходных наборов не находится ниже ломанной, проходящей через соседние точки 
z
i
.
2. Скользящее среднее с окном 
W
 вычисляется с учетом крайних положений окна. При вычислении используется центральное окно относительно координаты 
i
 с границами в полуинтервале 
[
i
−
⌊
W
/
2
⌋
;
i
+
⌈
W
/
2
⌉
)
. При нехватке элементов внутри окна, среднее значение вычисляется только по элементам внутри окна.
3. Для вычисления “нижнего разброса” рассмотрим нижнюю огибающую 
z
i
 двух дискретных наборов точек: исходного сигнала 
x
i
 и базовой линии 
y
i
, 
i
=
¯¯¯¯¯¯¯¯
1
,
n
. Тогда величина нижнего разброса определяется по следующей формуле:
D
=
√
1
n
−
1
∑
i
(
z
i
−
y
i
)
2


Требования
Программа должна реализовывать функцию 
compute_baseline
, принимающую на вход параметры:
movie
 — исходный сигнал 
V
i
j
t
, NumPy матрица размера 
N
×
M
×
T
, тип элементов 
float64
,
f_noise_sigma
 — матрица 
F
i
j
, NumPy матрица размера 
N
×
M
, тип элементов 
float64
,
mean_window_size
 — размер окна 
W
,
num_iterations
 — число итераций алгоритма 
P
.

Функция должна возвращать итоговую матрицу 
B
i
j
t
Первый пример
Входные параметры:
movie = np.array([[[1, 1, 3, 0, 5, 1, 2]]], dtype = np.float64)

f_noise_sigma = np.array([[1]], dtype = np.float64)

mean_window_size = 3

num_iterations = 10


Результат алгоритма:
np.array([[[1.0, 1.111111, 0.777777, 1.111111, 1.0, 1.5, 1.25]]])
Второй пример
Входные параметры

movie = np.array(
[[[ 3, -5,  1, -1, -3,  0], [ 4, 4, 1, -5, -3, -1]],
 [[-2, -4, -2,  0,  2, -3], [-2, 2, 2,  3, -2, 0]]], dtype = np.float64)

f_noise_sigma = np.array([[1, 1], [1, 0]], dtype = np.float64)
mean_window_size = 6
num_iterations = 4
Результат алгоритма

ans = np.array(
[[[   -3.62142, -3.3603358, -3.2882686, -3.0881984,  -3.093986, -2.6174827 ],
  [-0.83511114, -1.8763334, -2.1010666,  -2.217972, -2.6908998, -3.0786247 ]],
[[   -2.888889, -2.5416667, -2.3133333, -2.4277778, -2.3799999, -1.9749999 ],
  [ -1.1776251,  -1.080823, -1.2646583, -1.1717986, -1.0061584, -1.1003542 ]]], 
dtype = np.float64)
Корректность ответа
Ответ будет считаться верным, если 
max
∣
∣
B
j
u
r
y
i
j
t
−
B
s
o
l
i
j
t
∣
∣
<
10
−
3
,
где 
B
j
u
r
y
i
j
t
 — решение жюри, 
B
s
o
l
i
j
t
 — решение участника.

Ограничения на размер задачи
1
≤
N
≤
100

1
≤
M
≤
100

10
≤
T
≤
1000

3
≤
W
<
T

1
≤
P
≤
10

"""

import numpy as np
from math import ceil, floor

def moving_average(x, w):
    h = ceil(w / 2)
    l = flow // 2

    new_x = np.concatenate([[0] * w, x, [0] * w])

    lower = w - l
    higher = w + h


    value = np.sum(new_x[w:w + h])
    size = h

    result = []

    for _ in range(len(x)):
        result.append(value / size)

        value += new_x[higher]
        value -= new_x[lower]

        lower += 1
        higher += 1


        if lower > w:
            size -= 1
        
        if higher <= len(x) + w:
            size += 1

    return np.array(result)

def compute_baseline(movie, f_noise_sigma, mean_window_size, num_iterations):
    n, m, t = movie.shape

    for i in range(n):
        for j in range(m):
            bij = movie[i, j]
            fij = f_noise_sigma[i][j]

            source = movie[i, j]
            lower = np.min([source, bij], axis=0)

            for _ in range(num_iterations):
                bij = moving_average(lower, mean_window_size)
                lower = np.min([source, bij], axis=0)

                dij = np.sqrt(np.sum((bij - lower)**2) / (t - 1))

                if dij < fij:
                    break

            movie[i, j] = bij

    return movie

"""#Задание 8


Замечание
Условие данной задачи совпадает с условием Cpg filter v1.0, за отличием только увеличенных ограничений. Задача по сложности выше среднего, поэтому будьте осторожны.

Для оптимизации кода можно использовать возможности Python и NumPy при необходимости.

Условие
В одном из научных проектов в области биофинорматики возникла задача фильтрации данных из таблицы по некоторой системе критериев. Таблица состоит из нескольких колонок, среди которых интересными для пользователя являются 7. Исходно названия колонок имеют сложный замысловатый вид, поэтому для каждой колонки дано новое название (после символа двоеточие):


ID_REF: cpgs
CHR: chr
UCSC_REFGENE_NAME: gene
RELATION_TO_UCSC_CPG_ISLAND: geotype
CROSS_R: crossr
Class: class
UCSC_REFGENE_GROUP: genepart


Пример таблицы можно скачать по ссылке.
Требования
Ваш код должен реализовывать класс 
cpgs_annotation
 с конструктором, принимающим на вход 2 аргумента:
1) таблицу, представляющую собой список списков по строкам элементов таблицы;
2) список исходных имён столбцов.

Класс должен реализовывать метод 
get_cpgs
, принимающий на вход один аргумент - словарь из критериев и возвращающий 2 списка:
1) список имён из колонки cpgs для отфильтрованных строк таблицы;
2) список индексов (в 0-индексации) для отфильтрованных строк таблицы.

Метод должен осуществить фильтрацию таблицы по критериям, при чём все критерии объединены операцией логического И. Таким образом, найденные CpG сайты должны удовлетворять каждому из критериев. Рассмотрим 2 вида критериев 
in и out
. Критерий типа 
in
 позволяет выбрать строки, в которых есть хотя бы одно из значений критерия. Критерий типа 
out
 выбирает те строки, в которых не содержится ни одного из значений критерия. Если элемент оказался в обоих типах критерия, то 
out
 имеет больший приоритет.

Класс не должен содержать других публичных методов или аттрибутов. Некорректно составленные критерии программа должна игнорировать без ошибок.

Формат входа
Элементы исходной таблицы могут быть трёх типов: 
str
, 
int
, 
float
. Некоторые элементы исходной таблицы представлены строкой с разделителем 
;
, что означает принадлежность строки таблицы к каждому из классов. Например строка ‘
AMDHD2;ATP6V0C;AMDHD2
’ означает принадлежность двум классам: 
AMDHD2
 и 
ATP6V0C


Критерии для фильтрации представляют собой словарь с ключами имен столбцов, по которым осуществляется фильтрация, плюс один из типов фильтров ‘
_in
’, ‘
_out
’.
Пример: ‘
cpgs_in
’, ‘
chr_out
’.

В качестве значения в словаре хранится либо элемент, либо список элементов. Элемент может быть типов 
int
 или 
str
. Так же возможно единственное значение типа 
float - NaN
Значения NaN в списке критериев необходимо игнорировать.

Примеры входных данных
Примеры критериев:


1. {‘gene_in’: ‘TMEM49’}
2. {‘gene_in’: [‘TMEM49’, ‘HAGH’, ‘POLE3’, ‘PKD1L3’, ‘PNPLA6’]}
3. {‘gene_out’: [‘TMEM49’], ‘gene_in’: [‘PNPLA6’], ‘cpgs_in’: [‘cg00000029’, ‘cg00031443’]}
4. {‘gene_out’: float(‘nan’), ‘chr_in’: ‘7’}

Примеры тестовых данных
Примеры критериев

#	Критерий	Отфильтрованные CpG
1	{‘gene_in’: ‘TMEM49’}	[‘cg00002749’, ‘cg00040016’]
[64, 988]
2	{‘gene_in’: [‘TMEM49’, ‘HAGH’, ‘POLE3’, ‘PKD1L3’, ‘PNPLA6’]}	[‘cg00002749’, ‘cg00031443’, ‘cg00032036’, ‘cg00038167’, ‘cg00040016’, ‘cg00046913’, ‘cg00047469’, ‘cg00047683’, ‘cg00070052’, ‘cg00098239’, ‘cg00340921’, ‘cg00401032’, ‘cg00435006’, ‘cg00452393’]
[64, 782, 795, 947, 988, 1150, 1160, 1164, 1647, 2313, 7202, 8483, 9191, 9535]
3	{‘gene_out’: [‘TMEM49’], ‘gene_in’: [‘PNPLA6’], ‘cpgs_in’: [‘cg00000029’, ‘cg00031443’]}	[‘cg00031443’]
[782]
4	{‘gene_out’: float(‘nan’), ‘chr_in’: ‘7’}	[‘cg00002531’, ‘cg00003994’, ‘cg00006414’, ‘cg00006884’, ‘cg00009293’, …, ‘cg00470154’, ‘cg00470277’, ‘cg00471159’, ‘cg00471857’]
[57, 92, 154, 160, 222, …, 9955, 9978, 9991]
Формат выходных данных
В результате функция должна вернуть 2 списка:
1) список имён из колонки 
cpgs
 для отфильтрованных строк таблицы;
2) список индексов (в 0-индексации) для отфильтрованных строк таблицы.

Элементы в списках должны быть упорядочены по возрастанию индекса строк в таблице.

Ограничения на размер задачи
Это вторая версия задачи. Количество строк в таблице не более 
10
4
. Критериев в одном фильтре не более 
14
. Суммарное количество элементов в одном критерии не более 
2
⋅
10
4
. Один тест может состоять из не более чем 
5
 запусков 
get_cpgs
 и одного вызова конструктора.


"""

import pandas as pd
import math

class cpgs_annotation:

  def __init__(self, table_, column_names_):
    self.table = pd.DataFrame(data=table_, columns= column_names_)
    self.new_names = {
        'cpgs': 'ID_REF',
        'chr': 'CHR',
        'gene': 'UCSC_REFGENE_NAME',
        'geotype': 'RELATION_TO_UCSC_CPG_ISLAND',
        'crossr': 'CROSS_R',
        'class': 'Class',
        'genepart': 'UCSC_REFGENE_GROUP'
    }
  
  def get_cpgs(self, criteria):
    table_set = self.table.applymap(lambda x: set(x.split(';')) if type(x) is str else {x})    
    filtered_index_cpgs = None

    for crit_key, crit_values in criteria.items():
      if type(crit_values) is str or type(crit_values) is float or type(crit_values) is int:
        crit_values = {crit_values}
      else:
        crit_values = set(crit_values)
      crit_name, crit_type = (crit_key).split('_')
      
      if crit_name in self.new_names:      
        if crit_type == 'in':      
          if float in {type(x) for x in crit_values}:
             filtered_indexes = table_set[self.new_names[crit_name]].map(lambda x: bool(x.intersection(crit_values)))
             filtered_indexes_float = table_set[self.new_names[crit_name]].map(lambda x: (type(x) is float and math.isnan(x)))
             filtered_indexes = filtered_indexes | filtered_indexes_float
          else:
            filtered_indexes = table_set[self.new_names[crit_name]].map(lambda x: bool(x.intersection(crit_values)))

        elif crit_type == 'out':
          if float in {type(x) for x in crit_values}:
            filtered_indexes = table_set[self.new_names[crit_name]].map(lambda x: not bool(x.intersection(crit_values)))
            filtered_indexes_float = table_set[self.new_names[crit_name]].map(lambda x: not (type(x) is float and math.isnan(x)))
            filtered_indexes = filtered_indexes & filtered_indexes_float
          else:
            filtered_indexes = table_set[self.new_names[crit_name]].map(lambda x: not bool(x.intersection(crit_values)))
        else:
          continue
        if filtered_index_cpgs is None:
          filtered_index_cpgs = filtered_indexes
        else:
          filtered_index_cpgs =  filtered_index_cpgs & filtered_indexes
      else:
        continue
    if filtered_index_cpgs is None:
      filtered_index_cpgs = np.ones((len(table_set),), dtype = np.bool)
    filtered_rows_cpgs = self.table[self.new_names['cpgs']][filtered_index_cpgs]
    return list(filtered_rows_cpgs.values), list(filtered_rows_cpgs.index.values)
