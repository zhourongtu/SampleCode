#!usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys
abs_path = os.path.dirname(os.path.realpath(__file__))
print(abs_path)
sys.path.append(abs_path)
from binary_search import binary_search, cmp_func
from merge_sort import merge_sort

# 给出一个运行时间nlogn的算法，在给定集合S和另一个正整数x，判断S内是否有两个值之和为x。

# 方法一：排序（nlogn），顺序+二分查找。(nlogn)
# 方法二：字典。O(n)
# 方法三：每一个值线性查找O(n^2)

# TODO: 未考虑相同的情况，所以错误，需要改进二分查找，返回所有的值。

def judge_sum_of_2_element_in_list(input_list, x):
    result = merge_sort(input_list)
    for i in range(len(result)):
        l_key = result[i]
        r_key = x - l_key
        if binary_search(result, r_key, cmp_func) != -1:
            return True
    return False

if __name__ == '__main__':
    import unittest
    import random
    class TestInsertSort(unittest.TestCase):
        def test_case(self):
            self.assertEqual(judge_sum_of_2_element_in_list([1, 2, 3], 4), True)
            self.assertEqual(judge_sum_of_2_element_in_list([1, 2, 3, 4], 7), True)
            self.assertEqual(judge_sum_of_2_element_in_list([1, 2, 3], 3), True)
            self.assertEqual(judge_sum_of_2_element_in_list([1, 2, 3], 5), True)
            self.assertEqual(judge_sum_of_2_element_in_list([1, 2, 3], 6), False)
    unittest.main()