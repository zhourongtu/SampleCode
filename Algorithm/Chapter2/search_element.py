#!usr/bin/env python

# 查找问题
# 输入:A = <a1, a2, ..., an>, v
# 输出:下标i, 使得v=A[i], v不在A中时,为None。

# 伪代码描述:
# result = None
# for i <- 1 to Length(A)
#     do key <- A[i]
#         compare A[i] with v.
#         if v == A[i]:
#             result <- i

# 多个情况参与考虑
def search_int_in_list(int_list, v):
    result = None
    for i in range(len(int_list)):
        key = int_list[i]
        if key == v:
            if not result:
                result = []
            result.append(i)
    return result

# 证明如下
# 初始化:i = 1时,子数组为空,此时v不在子数组内,result为None,即第一轮迭代开始前成立。
# 保持:
#     i = j时,子数组为A[1->j],从具体情况看,循环开始前,result_(j-1)满足条件,
#     在v != A[j]时,result_(j) = result_(j-1)满足条件。
#     在v == A[j]时,如果result_(j-1)为None,则result_j为[j],满足条件。
#     若result_(j-1)不为None,对result_j = result(j-1).extend(j),对result_j的每一个值k满足条件v=A[k]。
# 终止:
#     i = Length(A) + 1,子数组为A,满足条件

if __name__ == "__main__":
    import unittest
    class TestInsertSort(unittest.TestCase):
        def test_case(self):
            self.assertEqual(search_int_in_list([2, 1], 1), [1])
        
        def test_case_2(self):
            self.assertEqual(search_int_in_list([2, 1, 3], 3), [2])
        
        def test_case_3(self):
            self.assertEqual(search_int_in_list([3, 2, 1], 2), [1])
 
        def test_case_4(self):
            self.assertEqual(search_int_in_list([3, 2, 1], 5), None)
    unittest.main()