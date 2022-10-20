#!usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce
# 1. 为一个数组，写两个函数
# 函数1：修改某个元素的数值。
# 函数2：求出前n个元素的合。

# 正常思路：前缀合，此时 函数2 时间复杂度O(1)，函数1 需要维护前缀和 时间复杂度O(n)
# 树状数组：函数2 时间复杂度O(lgn)，函数1 时间复杂度 O(lgn)


class BIndexTreeList(object):
    # 1.lgn层的树状数组。
    # 2.部分数字没有价值，所有层的第偶数个数字，没有价值。
    # 3.将所有有用的数据维护起来，长度与数组相同。（树状数组）
    
    def __init__(self, data_list):
        self.data_list = data_list
        self.b_i_tree_list = [0] * len(self.data_list)
        self.len_data = len(self.data_list)
        self._build_b_i_tree()

    def _build_b_i_tree(self):
        for i in range(len(self.data_list)):
            tmp_i = i + 1
            len_range = self.lowbit(tmp_i)
            self.b_i_tree_list[i] = reduce(lambda a, b: a + b, iter(self.data_list[i + 1 - len_range: i + 1]))

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
            self.b_i_tree_list[index] += x
            index += self.lowbit(index+1)
    
    def count(self, p):
        # 1 ~ p+1的和
        result = 0
        while p >= 0:
            result += self.b_i_tree_list[p] # 以p为结尾的，长度为self.lowbit(p)的区间的值。
            p -= self.lowbit(p+1) # 减去该长度，继续。
        return result

    # 数的最低位代表哪个数字。x & -x。原理x最低位1，对应的补码x的位置为0，补码往后为1，+1，正好在该位置。
    # lowbit的值，为最低位代表的数字值。
    # 最低行的数据，lowbit为1，第二行的lowbit均为2，即lowbit可知序列长度，又知道结尾的序号。
    def lowbit(self, x):
        return x & -x



class PrefixSumList(object):
    def __init__(self, data_list):
        import copy
        self.data_list = copy.deepcopy(data_list)
        self.prefix_sum_list = [0] * len(self.data_list)
        self.len_data = len(self.data_list)
        self.build_prefix_sum_list()

    def build_prefix_sum_list(self):
        now_sum = 0
        for i in range(self.len_data):
            now_sum += self.data_list[i]
            self.prefix_sum_list[i] = now_sum
        
    def set_index_value(self, index, value):
        self.data_list[index] = value
        self.build_prefix_sum_list()

    def count(self, index):
        return self.prefix_sum_list[index]    

from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        print('\n')
        return result
    return timeit_wrapper

if __name__ == "__main__":
    # 1.功能测试
    # import unittest
    import random
    # class TestPolyAlgo(unittest.TestCase):
    #     def test_case(self):
    #         for i in range(10):
    #             shuffle_test_case = [random.randint(0, 10000) for i in range(1000)]
    #             prefix_class_list = PrefixSumList(shuffle_test_case)
    #             b_index_tree_list = BIndexTreeList(shuffle_test_case)
    #             for i in range(100):
    #                 self.assertEqual(prefix_class_list.count(i), b_index_tree_list.count(i))
    #             for i in range(100):
    #                 random_num = random.randint(0, 10000)
    #                 prefix_class_list.set_index_value(i, random_num)
    #                 b_index_tree_list.set_index_value(i, random_num)
    #                 for i in range(100):
    #                     self.assertEqual(prefix_class_list.count(i), b_index_tree_list.count(i))
    # unittest.main()

    # 2.性能测试

    # 1.构建性能测试
    import time
    # @timeit
    # def test_func_0():
    #     for i in range(10000):
    #         shuffle_test_case = [random.randint(0, 10000) for i in range(1000)]
    # print('random_num')
    # test_func_0()

    @timeit
    def test_func_1(cls_class, shuffule_test_case):
        for i in range(10000):
            the_list = cls_class(shuffle_test_case)
    shuffle_test_case = [random.randint(0, 10000) for i in range(1000)]
    print("prefix build_prefix_class 10000 times cost_time:")
    test_func_1(PrefixSumList, shuffle_test_case)
    print("b_i_tree build_prefix_class 10000 times cost_time:")
    test_func_1(BIndexTreeList, shuffle_test_case)

    # 2.设置性能测试
    @timeit
    def test_func_2(the_list_1, random_num_list):
        for random_num in random_num_list:
            # for i in range(len(the_list_1)):
            for idx in range(the_list_1.len_data):        
                the_list_1.set_index_value(idx, random_num)

    RANDOM_TIME_LIST_LEN = 100
    DATA_LEN = 100
    shuffle_test_case = [random.randint(0, 10000) for i in range(1000)]
    random_num_list = [random.randint(0, 10000) for i in range(RANDOM_TIME_LIST_LEN)]
    the_list_1 = PrefixSumList(shuffle_test_case)
    the_list_2 = BIndexTreeList(shuffle_test_case)
    print("prefix set_a_value {0} times, cost_time: ".format(RANDOM_TIME_LIST_LEN * DATA_LEN))
    test_func_2(the_list_1, random_num_list)
    print("b_i_tree set_a_value {0} times, cost_time: ".format(RANDOM_TIME_LIST_LEN * DATA_LEN))
    test_func_2(the_list_2, random_num_list)
    
    # 3.查询性能设置
    LOOP_TIMES = 1000
    @timeit
    def test_func_3(the_list_1):
        for _ in range(LOOP_TIMES):
            for idx in range(the_list_1.len_data):        
                the_list_1.count(idx)
    print("prefix count {0} times, cost_time: ".format(LOOP_TIMES * DATA_LEN))
    test_func_3(the_list_1)
    print("b_i_tree count {0} times, cost_time: ".format(LOOP_TIMES * DATA_LEN))
    test_func_3(the_list_2)

# prefix build_prefix_class 10000 times cost_time:
# Function test_func_1 Took 2.4067 seconds

# b_i_tree build_prefix_class 10000 times cost_time:
# Function test_func_1 Took 4.2519 seconds

# O(n)与O(lgn)
# prefix set_a_value 10000 times, cost_time:
# Function test_func_2 Took 4.7038 seconds

# b_i_tree set_a_value 10000 times, cost_time:
# Function test_func_2 Took 0.0863 seconds

# O(1)与O(lgn)
# prefix count 1000000 times, cost_time:
# Function test_func_3 Took 0.4642 seconds

# b_i_tree count 1000000 times, cost_time:
# Function test_func_3 Took 5.6615 seconds