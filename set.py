# Set , frozenset


set1 = {12,14,11,'hello'} 
set2 = {14,3,141,'world'}
set3 = {11,3,145,'Mery'}
list1 = [221, 21, 34,67,12,21,34]


# FROZENSET
# fr_set = {12,34,54,22}
# print(fr_set)


# LIST
# c = set(list1)
# print(c)
# list1 = list(c)
# print(list1)


# FOR
# new_set = {i ** 2 for i in range(10)}
# print(new_set)


# ADD
# set1.add(123)
# print(set1)


# CLEAR
# set2.clear()
# print(set2)


# COPY
# new_set = set1.copy()
# print(new_set)


# DIFFERENCE Возвращает набор, содержащий разницу между двумя или более наборами
# print(set1.difference(set2,set3))


# DIFERENCE_UPDATE Удаляет элементы в этом наборе, которые также включены в другой, указанный набор
# set1.difference_update(set2)
# print(set1)


# DISCARD Удалить указанный элемент
# set1.discard(14)
# print(set1)


# INTERSECTION Возвращает набор, то есть пересечение двух других наборов
# print(set1.intersection(set2))


# ISDISJOINT Возвращает, если два набора имеют пересечение или нет
# print(set1.isdisjoint(set2))


# ISSUBSET возвращает True, если все элементы в наборе существуют в указанном наборе, в противном случае он возвращает False.
# print(set1.issubset(set2))


# POP
# x = set1.pop()
# print(x)


# REMOVE
# set1.remove('hello')
# print(set1)


# SYMETRIC_DIFFERENCE возвращает набор, содержащий все элементы из обоих наборов, но не элементы, присутствующие в обоих наборах
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y) 
# print(z)


# UNION Вернуть набор, содержащий все элементы из обоих наборов, дубликаты исключены:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.union(y) 
# print(z)


# UPDATE Обновите набор с объединением этого набора и других
# set1.update(set2)
# print(set1)