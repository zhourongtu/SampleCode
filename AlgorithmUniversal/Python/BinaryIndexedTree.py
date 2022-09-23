#!usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce
# 1. 为一个数组，写两个函数
# 函数1：修改某个元素的数值。
# 函数2：求出前n个元素的合。

# 正常思路：前缀合，此时 函数2 时间复杂度O(1)，函数1 需要维护前缀和 时间复杂度O(n)
# 树状数组：函数2 时间复杂度O(lgn)，函数1 时间复杂度 O(lgn)


class BIndexTree(object):
    # 1.lgn层的树状数组。
    # 2.部分数字没有价值，所有层的第偶数个数字，没有价值。
    # 3.将所有有用的数据维护起来，长度与数组相同。（树状数组）
    
    def __init__(self):
        self.data_list = [1, 2, 3, 4]
        self.b_i_tree = [0] * len(self.data_list)
        self.len_data = len(self.data_list)
        self._build_b_i_tree()

    def _build_b_i_tree(self):
        for i in range(len(self.data_list)):
            tmp_i = i + 1
            len_range = self.lowbit(tmp_i)
            self.b_i_tree[i] = reduce(lambda a, b: a + b, iter(self.data_list[i + 1 - len_range: i + 1]))

    def set_index_value(self, index, value):
        ori_num = self.data_list[index]
        now_num = value
        delta_num = now_num - ori_num
        self.data_list[index] = value # 更新数组
        self.add(index, delta_num) # 更新树状数组

    # 序列b[i]正上方的序列b[i+lowbit(i)]
    def add(self, index, x):
        # 维护 包含self.data_list[index]值的合区间。
        while index < self.len_data:
            self.b_i_tree[index] += x
            index += self.lowbit(index+1)
    
    def count(self, p):
        # 1 ~ p+1的和
        result = 0
        while p >= 0:
            result += self.b_i_tree[p] # 以p为结尾的，长度为self.lowbit(p)的区间的值。
            p -= self.lowbit(p+1) # 减去该长度，继续。
        return result

    # 数的最低位代表哪个数字。x & -x。原理x最低位1，对应的补码x的位置为0，补码往后为1，+1，正好在该位置。
    # lowbit的值，为最低位代表的数字值。
    # 最低行的数据，lowbit为1，第二行的lowbit均为2，即lowbit可知序列长度，又知道结尾的序号。
    def lowbit(self, x):
        return x & -x


if __name__ == "__main__":
    # import unittest
    # import random
    # class TestPolyAlgo(unittest.TestCase):
    #     def test_case(self):
    #         for i in range(200):
    #             shuffle_test_case = [random.randint(0, 10000) for i in range(100)]
    #             get_data_dict = {}
    #             insert_sort(shuffle_test_case, extra_info=get_data_dict)
    #             self.assertEqual(len(get_inversion_tuple(shuffle_test_case)), get_data_dict['cnt'])
    #             get_data_dict = {}
    #             merge_sort(shuffle_test_case, extra_info=get_data_dict)
    #             self.assertEqual(len(get_inversion_tuple(shuffle_test_case)), get_data_dict['cnt'])
    # unittest.main()
    b_i_t = BIndexTree()
    print(b_i_t.b_i_tree)
    print(b_i_t.count(0))
    print(b_i_t.count(1))
    print(b_i_t.count(2))
    print(b_i_t.count(3))
    b_i_t.set_index_value(0, 5)
    print("b_i_t_data_list:", b_i_t.data_list)
    print("b_i_t_tree_list:", b_i_t.b_i_tree)
    print(b_i_t.count(0))
    print(b_i_t.count(1))
    print(b_i_t.count(2))
    print(b_i_t.count(3))