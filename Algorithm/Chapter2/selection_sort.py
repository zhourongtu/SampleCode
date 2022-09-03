#!usr/bin/env python
import copy

def selection_sort(input_list, reverse=False):
    def cmp_func(a, b):
        return a < b
    def r_cmp_func(a, b):
        return a > b
    _sort_cmp_func = cmp_func if not reverse else r_cmp_func
    result = copy.deepcopy(input_list)

    for i in range(len(result)):
        num = result[i]
        num_index = i
        for j in range(i+1, len(result)):
            if _sort_cmp_func(result[j], num):
                num = result[j]
                num_index = j
        if num_index == i:
            break
        tmp_num = result[num_index]
        result[num_index] = result[i]
        result[i] = tmp_num
    return result
if __name__ == "__main__":
    import unittest
    class TestInsertSort(unittest.TestCase):
        def test_case(self):
            self.assertEqual(selection_sort([2, 1]), [1, 2])
        
        def test_case_2(self):
            self.assertEqual(selection_sort([2, 1, 3]), [1, 2, 3])
        
        def test_case_3(self):
            self.assertEqual(selection_sort([3, 2, 1]), [1, 2, 3])
        
        def tset_case_4(self):
            self.assertEqual(selection_sort([1, 3, 2]), [1, 2, 3])

        def test_case_r(self):
            self.assertEqual(selection_sort([2, 1], True), [2, 1])
        
        def test_case_2_r(self):
            self.assertEqual(selection_sort([2, 1, 3], True), [3, 2, 1])
        
        def test_case_3_r(self):
            self.assertEqual(selection_sort([3, 2, 1], True), [3, 2, 1])
        
        def tset_case_4_r(self):
            self.assertEqual(selection_sort([1, 3, 2], True), [3, 2, 1])
    
    unittest.main()