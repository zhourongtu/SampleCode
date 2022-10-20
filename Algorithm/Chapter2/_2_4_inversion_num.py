#!usr/bin/env python
# -*- coding: utf-8 -*-
from audioop import add
import sys
import os
import copy
# abs_path = os.path.dirname(os.path.realpath(__file__))
# print(abs_path)
# sys.path.append(abs_path)

# 1.逆序数定义：A[1...n]，i<j情况下有A[i] > A[j]，(i, j)为逆序对
# 2.<2, 3, 8, 6, 1>逆序对的说明
# (1, 5), (2, 5), (3, 4), (3, 5), (4, 5)
# 3.逆序数和插入排序之间的关系：与交换次数相同——单次交换有序。

def insert_sort(input_list, reverse=False, extra_info={}):
    cnt = 0
    def cmp_func(a, b):
        return a > b
    def r_cmp_func(a, b):
        return a < b
    _sort_cmp_func = cmp_func if not reverse else r_cmp_func
    result = copy.deepcopy(input_list)
    for j in range(1, len(result)):
        key = result[j]
        # insert key to result[0~j-1]
        i = j - 1
        while i >= 0 and _sort_cmp_func(result[i], key):
            cnt += 1
            result[i + 1] = result[i]
            i = i - 1
        result[i + 1] = key
    extra_info['cnt'] = cnt
    return result

def get_inversion_tuple(data_list):
    result = []
    len_data = len(data_list)
    for i_index in range(len_data):
        cmp_num = data_list[i_index]
        j_g_i_index = i_index
        while j_g_i_index < len_data:
            j_num = data_list[j_g_i_index]
            if cmp_num > j_num:
                result.append((i_index, j_g_i_index))
            j_g_i_index += 1
    return result

def get_inversion_tuple_opt(data_list):

    pass


def cmp_func(a, b):
    return a <= b
def r_cmp_func(a, b):
    return a > b

def merge(be_sorted_list, l_start, l_end, r_end, reverse=False, extra_info={"cnt": 0}):
    _cmp_func = cmp_func if not reverse else r_cmp_func
    # GUARD_NUM = GUARD_NUM_MAX if not reverse else GUARD_NUM_MIN
    len_l = l_end - l_start + 1
    len_r = r_end - l_end
    tmp_list_l = [be_sorted_list[l_start + i] for i in range(len_l)]
    # tmp_list_l.append(GUARD_NUM)
    tmp_list_r = [be_sorted_list[l_end + 1 + i] for i in range(len_r)]
    # tmp_list_r.append(GUARD_NUM)
    i = 0
    j = 0
    k = 0
    for tmp_k in range(len_l + len_r):
        #添加部分
        k = tmp_k
        if i == len_l or j == len_r:
            break

        if _cmp_func(tmp_list_l[i], tmp_list_r[j]):
            be_sorted_list[l_start + k] = tmp_list_l[i]
            i += 1
        else:
            extra_info['cnt'] += len_l - i
            be_sorted_list[l_start + k] = tmp_list_r[j]
            j += 1
    # 添加部分
    if i < len_l:
        be_sorted_list[l_start+k : r_end+1] = tmp_list_l[i : len_l]
    if j < len_r:
        be_sorted_list[l_start+k : r_end+1] = tmp_list_r[j : len_r]


def merge_sort(be_sorted_list, extra_info={}):
    extra_info['cnt'] = 0
    result = copy.copy(be_sorted_list)
    _merge_sort(result, 0, len(result) - 1, extra_info=extra_info)
    return result

def _merge_sort(be_sorted_list, start, end, reverse=False, extra_info={"cnt": 0}):
    if start < end:
        mid = (start + end) // 2
        _merge_sort(be_sorted_list, start, mid, reverse, extra_info=extra_info)
        _merge_sort(be_sorted_list, mid + 1, end, reverse, extra_info=extra_info)
        merge(be_sorted_list, start, mid, end, extra_info=extra_info)

if __name__ == "__main__":
    import unittest
    import random
    class TestPolyAlgo(unittest.TestCase):
        def test_case(self):
            for i in range(200):
                shuffle_test_case = [random.randint(0, 10000) for i in range(100)]
                get_data_dict = {}
                insert_sort(shuffle_test_case, extra_info=get_data_dict)
                self.assertEqual(len(get_inversion_tuple(shuffle_test_case)), get_data_dict['cnt'])
                get_data_dict = {}
                merge_sort(shuffle_test_case, extra_info=get_data_dict)
                self.assertEqual(len(get_inversion_tuple(shuffle_test_case)), get_data_dict['cnt'])
    unittest.main()

    # shuffle_test_case = [random.randint(0, 10000) for i in range(10)]
    # print('basic_inversion, ', len(get_inversion_tuple(shuffle_test_case)))
    # get_data_dict = {}
    # insert_sort(shuffle_test_case, extra_info=get_data_dict)
    # print('insert_sort_get_inversion, ', get_data_dict['cnt'])
    # get_data_dict = {}
    # merge_sort(shuffle_test_case, extra_info=get_data_dict)
    # print('merge_sort_get_inversion, ', get_data_dict['cnt'])

