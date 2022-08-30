#!usr/bin/env python
import copy

def insert_sort(input_list):
    result = copy.deepcopy(input_list)
    for j in range(1, len(result)):
        key = result[j]
        # insert key to result[0~j-1]
        i = j-1
        while i >= 0 and result[i] > key:
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
    
    unittest.main()