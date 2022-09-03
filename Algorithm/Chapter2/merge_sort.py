#!usr/bin/env python
import copy
GUARD_NUM_MAX = 2**21 - 1
GUARD_NUM_MIN = -2**21

def cmp_func(a, b):
    return a < b
def r_cmp_func(a, b):
    return a > b

def merge(be_sorted_list, l_start, l_end, r_end, reverse=False):
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
            be_sorted_list[l_start + k] = tmp_list_r[j]
            j += 1
    # 添加部分
    if i < len_l:
        be_sorted_list[l_start+k : r_end+1] = tmp_list_l[i : len_l]
    if j < len_r:
        be_sorted_list[l_start+k : r_end+1] = tmp_list_r[j : len_r]


def merge_sort(be_sorted_list):
    result = copy.copy(be_sorted_list)
    _merge_sort(result, 0, len(result) - 1)
    return result

def _merge_sort(be_sorted_list, start, end, reverse=False):
    if start < end:
        mid = (start + end) // 2
        _merge_sort(be_sorted_list, start, mid, reverse)
        _merge_sort(be_sorted_list, mid + 1, end, reverse)
        merge(be_sorted_list, start, mid, end)

if __name__ == '__main__':
    import unittest
    import random
    class TestInsertSort(unittest.TestCase):
        def test_case(self):
            shuffle_test_case = [random.randint(0, 10000) for i in range(1000)]
            sorted_test_case = sorted(shuffle_test_case)
            self.assertEqual(merge_sort(shuffle_test_case), sorted_test_case)
    unittest.main()