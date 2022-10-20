#!usr/bin/env python
# -*- coding: utf-8 -*-

# 1.渐近运行时间O(n)

# 2.伪代码实现朴素多项式求值

def polynoimal_evaluation(a_list, x):
    result = 0
    for idx, a_i in enumerate(a_list):
        result += a_i * compute_poly(x, idx)
    return result

def compute_poly(x, n):
    if n == 0:
        return 1
    result = 1
    for i in range(n):
        result *= x
    return result

def poly_horner(a_list, x):
    y = 0
    i = len(a_list)
    while i >= 0:
        y = a_list[i] + x * y
        i = i - 1
    return y

# 3.循环不变式说明 见笔记




if __name__ == "__main__":
    import unittest
    import random
    class TestPolyAlgo(unittest.TestCase):
        def test_case(self):
            for i in range(200):
                shuffle_test_case = [random.randint(0, 10000) for i in range(20)]
                self.assertEqual(poly_horner(shuffle_test_case, 2), polynoimal_evaluation(shuffle_test_case, 2))
    unittest.main()

