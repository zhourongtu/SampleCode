#!usr/bin/env python
import copy

def insert_sort(input_list, reverse=False):
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
            result[i + 1] = result[i]
            i = i - 1
        result[i + 1] = key
    return result

if __name__ == "__main__":
    import unittest
    class TestInsertSort(unittest.TestCase):
        def test_case(self):
            self.assertEqual(insert_sort([2, 1]), [1, 2])
        
        def test_case_2(self):
            self.assertEqual(insert_sort([2, 1, 3]), [1, 2, 3])
        
        def test_case_3(self):
            self.assertEqual(insert_sort([3, 2, 1]), [1, 2, 3])
        
        def tset_case_4(self):
            self.assertEqual(insert_sort([1, 3, 2]), [1, 2, 3])

        def test_case_r(self):
            self.assertEqual(insert_sort([2, 1], True), [2, 1])
        
        def test_case_2_r(self):
            self.assertEqual(insert_sort([2, 1, 3], True), [3, 2, 1])
        
        def test_case_3_r(self):
            self.assertEqual(insert_sort([3, 2, 1], True), [3, 2, 1])
        
        def tset_case_4_r(self):
            self.assertEqual(insert_sort([1, 3, 2], True), [3, 2, 1])
    
    unittest.main()