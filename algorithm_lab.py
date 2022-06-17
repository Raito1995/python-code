import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dict1 = ['DS', 80, 'DM', 76, 'LA', 63]
dict2 = ['DS', 53, 'DM', 79, 'LA', 98]
dict3 = ['DS', 83, 'DM', 49, 'LA', 78]
total_dict = {'97501': dict1, '97502': dict2, '97503': dict3}


def code_select(code_mun):
    if code_mun == '1':
        return code_mun
    elif code_mun == '2':
        return code_mun
    elif code_mun == '3':
        return code_mun
    elif code_mun == '4':
        return code_mun
    elif code_mun == '5':
        select_mode = input('請輸入科目名稱:')
        mode_select(select_mode)
        return code_mun
    elif code_mun == '6':
        return code_mun


def mode_select(mode_num):
    if mode_num == 'DS':
        select_algorithm = input('請選擇排序方法：1.Insertion Sort 2.Merge Sort 3.Radix Sort\n')
        algorithm_select(select_algorithm)
    elif mode_num == 'DM':
        return mode_num
    elif mode_num == 'LA':
        return mode_num


def algorithm_select(algorithm_num):
    if algorithm_num == '1':
        return algorithm_num
    elif algorithm_num == '2':
        return algorithm_num
    elif algorithm_num == '3':
        radix_sort()
        return algorithm_num


def insertion_sort(code, mode, algorithm, score):
    return


def merge_sort(code, mode, algorithm, score):
    return


def radix_sort():
    global total_dict
    number = [total_dict['97501'][1], total_dict['97502'][1], total_dict['97502'][1]]
    length = len(number)
    k = 0
    n = 1
    temp = []
    for i in range(length):
        temp.append([0] * length)
    order = [0] * length
    while n <= 100:
        for i in range(length):
            lsd = (number[i] // n) % 10
            temp[lsd][order[lsd]] = number[i]
            order[lsd] += 1
        for i in range(length):
            if order[i] != 0:
                for j in range(order[i]):
                    number[k] = temp[i][j]
                    k += 1
            order[i] = 0
        n *= 10
        k = 0
    return


code = '功能代號如下：\n1.查詢學生單科成績\n2.查詢學生所有成績\n3.新增學生成績\n4.刪除學生成績\n5.排序學生成績\n6.離開系統\n請輸入代號：'
select_code = input(code)
code_select(select_code)





