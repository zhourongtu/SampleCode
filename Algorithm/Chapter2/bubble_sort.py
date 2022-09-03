#!usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import random

# 冒泡排序伪代码
# for i <- 1 to Length(A) - 1
#     # 默认从小到大
#     for j <- 1 to Length(A) - i
#         exchange A[j] with A[j-1] if A[j] < A[j-1]

class CountCompute():
    def __init__(self):
        self.cnt_ori = 0
        self.cnt_opt_1 = 0
        self.cnt_opt_2 = 0
        self.cnt_opt_3 = 0

    def clear(self):
        self.cnt_ori = 0
        self.cnt_opt_1 = 0
        self.cnt_opt_2 = 0
        self.cnt_opt_3 = 0

cnt_log = CountCompute()

# 冒泡排序
def bubble_sort(input_list, reverse=False):
    def cmp_func(a, b):
        return a > b
    def r_cmp_func(a, b):
        return a < b
    _sort_cmp_func = cmp_func if not reverse else r_cmp_func
    result = copy.deepcopy(input_list)
    for i in range(len(result)-1):
        for j in range(1, len(result) - i):
            cnt_log.cnt_ori += 1
            if _sort_cmp_func(result[j-1], result[j]):
                tmp_element = result[j]
                result[j] = result[j-1]
                result[j-1] = tmp_element
    return result

# 冒泡排序优化1:标记位
def bubble_sort_opt_1(input_list, reverse=False):
    def cmp_func(a, b):
        return a > b
    def r_cmp_func(a, b):
        return a < b
    _sort_cmp_func = cmp_func if not reverse else r_cmp_func
    result = copy.deepcopy(input_list)
    for i in range(len(result)-1):
        had_exchange = False
        for j in range(1, len(result) - i):
            cnt_log.cnt_opt_1 += 1
            if _sort_cmp_func(result[j-1], result[j]):
                had_exchange = True # 优化点：标记发生过交换
                tmp_element = result[j]
                result[j] = result[j-1]
                result[j-1] = tmp_element
        if not had_exchange:
            break
    return result

# 冒泡排序优化2:交换数据的地址记录
def bubble_sort_opt_2(input_list, reverse=False):
    def cmp_func(a, b):
        return a > b
    def r_cmp_func(a, b):
        return a < b
    _sort_cmp_func = cmp_func if not reverse else r_cmp_func
    result = copy.deepcopy(input_list)
   
    changed_index = len(result)
    for i in range(len(result)-1):
        had_exchange = False
        for j in range(1, min(len(result) - i, changed_index)):
            cnt_log.cnt_opt_2 += 1
            if _sort_cmp_func(result[j-1], result[j]):
                had_exchange = True
                changed_index = j # 优化点2：标记最后一次交换后的时间，j及以后保持有序。
                tmp_element = result[j]
                result[j] = result[j-1]
                result[j-1] = tmp_element
        if not had_exchange:
            break
    return result


# 冒泡排序优化3:双向冒泡排序，减少极端情况，因为最大值在左侧就会产生在最后一次每一次发生交换。
def bubble_sort_opt_3(input_list, reverse=False):
    def cmp_func(a, b):
        return a > b
    def r_cmp_func(a, b):
        return a < b
    _sort_cmp_func = cmp_func if not reverse else r_cmp_func
    result = copy.deepcopy(input_list)
   
    changed_index_forward = len(result)
    changed_index_backward = 0 # 原因是取j, j-1覆盖0
    for i in range(len(result)-1):
        # 正向排序
        had_exchange = False
        for j in range(1, min(len(result) - i, changed_index_forward)):
            cnt_log.cnt_opt_3 += 1
            if _sort_cmp_func(result[j-1], result[j]):
                had_exchange = True
                changed_index_forward = j
                tmp_element = result[j]
                result[j] = result[j-1]
                result[j-1] = tmp_element
        if not had_exchange:
            break
        # 反向排序（此时len(result) - i 及以后有序）、changed_index_forward及以后有序。取后者
        had_exchange = False
        for j in range(max(changed_index_forward - 1, 1), changed_index_backward, -1):
            cnt_log.cnt_opt_3 += 1
            # 从changed_index_forward -> len(result) - i 有序
            if _sort_cmp_func(result[j-1], result[j]):
                had_exchange = True
                changed_index_backward = j
                tmp_element = result[j]
                result[j] = result[j-1]
                result[j-1] = tmp_element
        if not had_exchange:
            break
    return result


if __name__ == "__main__":
    for i in range(10):
        shuffle_test_case = [random.randint(0, 10000) for i in range(2000)]
        sorted_test_case = sorted(shuffle_test_case)
        bubble_sort(shuffle_test_case)
        bubble_sort_opt_1(shuffle_test_case)
        bubble_sort_opt_2(shuffle_test_case)
        bubble_sort_opt_3(shuffle_test_case)
    print("ori: \t", cnt_log.cnt_ori)
    print("opt_1: \t", cnt_log.cnt_opt_1, "\topt_percent:", cnt_log.cnt_ori / cnt_log.cnt_opt_1)
    print("opt_2: \t", cnt_log.cnt_opt_2, "\topt_percent:", cnt_log.cnt_ori / cnt_log.cnt_opt_2)
    print("opt_3: \t", cnt_log.cnt_opt_3, "\topt_percent:", cnt_log.cnt_ori / cnt_log.cnt_opt_3)

    # import unittest
    # class TestInsertSort(unittest.TestCase):
    #     def test_case(self):
    #         shuffle_test_case = [random.randint(0, 10000) for i in range(1000)]
    #         sorted_test_case = sorted(shuffle_test_case)
    #         self.assertEqual(bubble_sort(shuffle_test_case), sorted_test_case)
    #         self.assertEqual(bubble_sort_opt_1(shuffle_test_case), sorted_test_case)
    #         self.assertEqual(bubble_sort_opt_2(shuffle_test_case), sorted_test_case)
    #         self.assertEqual(bubble_sort_opt_3(shuffle_test_case), sorted_test_case)

    #     def test_case_r(self):
    #         shuffle_test_case = [random.randint(0, 10000) for i in range(1000)]
    #         sorted_test_case = sorted(shuffle_test_case, reverse=True)
    #         self.assertEqual(bubble_sort(shuffle_test_case, reverse=True), sorted_test_case)
    #         self.assertEqual(bubble_sort_opt_1(shuffle_test_case, reverse=True), sorted_test_case)
    #         self.assertEqual(bubble_sort_opt_2(shuffle_test_case, reverse=True), sorted_test_case)
    #         self.assertEqual(bubble_sort_opt_3(shuffle_test_case, reverse=True), sorted_test_case)

    # unittest.main()