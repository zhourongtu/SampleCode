#!usr/bin/env python

# 算法：取某个值或者某个值的集合为输入，产生某个值或者某个值的集合为输出，将输入转换为输出的计算步骤的一个序列，称作算法

# 1.定义存储顺序，a1为最低位，an为最高位。
# 输入: A<a1, a2, a3, ..., an>, B<b1, b2, b3, ..., bn>
# 输出: C<c1, c2, c3, ..., cn, c_(n+1)>

# 伪代码
# C[0] <- (A[0] + B[0]) mod 2
# C[1] <- (A[0] + B[0]) / 2

# for i <- j <- 2 -> n:
#     key_1 <- A[i]
#     key_2 <- B[j]
#     tmp_key <- (A[i] + B[j] + C[i])
#     C[i] <- tmp_key mod 2
#     C[i + 1] <- tmp_key / 2

# 证明如下
# 初始化：对i = 2的初始值，有子问题输入A<a1>， B<b1>，等于C<c1, c2>。
# 保持：
#     对i = j = k值，有子问题输入A<a1, a2, ..., a_(k-1)>，B<b1, b2, ..., b_(k-1)>, C<c1, c2, ..., k>成立
#     tmp_key <- (A[i] + B[j] + C[i])
#     C[k] = tmp_key mod 2
#     C[k + 1] = tmp_key / 2

#     此时有C[1->(k-1)], C[k], C[k+1] 满足 A[1->(k-1)] + B[1->(k-1)]的C[1->(k-1)], (前结果C[k] + A[k] + B[k]) mod 2, (前结果C[k] + A[k] + B[k]) / 2 满足条件。
# 终止：对i = n+1的初始值，有子问题输入A<a1, ..., an>, B<b1, ..., bn>,等于C<c1, ..., c_(n+1)。

def add_binary_in_array(l_array, r_array, length):
    result = [0] * (length + 1)
    result[0] = (l_array[0] + r_array[0]) % 2
    result[1] = (l_array[0] + r_array[0]) // 2
    for idx in range(1, length):
        i = j = idx
        key_1 = l_array[i]
        key_2 = r_array[j]
        tmp_key = key_1 + key_2 + result[idx]
        result[idx] = tmp_key % 2
        result[idx + 1] = tmp_key // 2
    return result


# 改造了一下，支持字符串的二进制加法，通过了leetcode。
def add_binary_with_str(l_str, r_str):
    l_array = [*reversed([int(a) for a in list(l_str)])]
    r_array = [*reversed([int(a) for a in list(r_str)])]
    result_array = none_equal_add_binary_in_array(l_array, r_array)
    result_int_list = reversed(result_array)
    result_str_list = [str(a) for a in result_int_list]
    result = ''.join(result_str_list)
    result = result.lstrip('0')
    if not result:
        return '0'
    return result


def none_equal_add_binary_in_array(l_array, r_array):
    min_length = min(len(l_array), len(r_array))
    max_length = max(len(l_array), len(r_array))
    result = [0] * (max_length + 1)
    result[0] = (l_array[0] + r_array[0]) % 2
    result[1] = (l_array[0] + r_array[0]) // 2
    # 破循环min_length
    for idx in range(1, min_length):
        i = j = idx
        key_1 = l_array[i]
        key_2 = r_array[j]
        tmp_key = key_1 + key_2 + result[idx]
        result[idx] = tmp_key % 2
        result[idx + 1] = tmp_key // 2
    
    p_array = r_array if len(l_array) == min_length else l_array
    for idx in range(min_length, max_length):
        tmp_key = p_array[idx] + result[idx]
        result[idx] = tmp_key % 2
        result[idx + 1] = tmp_key // 2
    return result

if __name__ == "__main__":
    import unittest
    class TestInsertSort(unittest.TestCase):
        def test_case(self):
            self.assertEqual(add_binary_in_array([1], [1], 1), [0, 1])
        
        def test_case_2(self):
            self.assertEqual(add_binary_in_array([0], [1], 1), [1, 0])
        
        def test_case_3(self):
            self.assertEqual(add_binary_in_array([1, 0], [1, 0], 2), [0, 1, 0])
 
        def test_case_4(self):
            self.assertEqual(add_binary_in_array([1, 0], [1, 1], 2), [0, 0, 1])
    unittest.main()