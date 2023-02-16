# Инструкция

---

***Задача:*** 
Написать программу, которая из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам. Первоначальный массив можно задать на старте выполнения алгоритма.

***Решение:***
* Заводим массив **test_data_array** с заданными элементами и итоговый массив **result_array**. Заводим переменную **length**, которая хранит размер массива **test_data_array**. Заводим два счетчика **n** и **m**, присваиваем им значение ноль. 
* Далее мы заводим цикл, в котором проходим по всем элементам массива **test_data_array**, и все элементы, длина которых будет меньше либо равна трем мы будем складывать в массив **result_array**.
* В конце программы мы выведем заполненный массив **result_array**.