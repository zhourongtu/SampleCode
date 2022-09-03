#!usr/bin/env python

# BINARY_SEARCH(data, begin, end)
# f_s <- begin
# f_e <- end
# while f_s < f_e:
#     mid <- (f_s + f_e) // 2
#     compare Element with data[mid]
#     if find and break
#     if bigger, find between f_s and mid-1
#     if lesser, find between mid+1 and f_e

#     if f_s == mid-1:
#         compare and break
#     if f_e == mid+1:
#         compare and break


def binary_search(data_list, element, cmp_func):
    start = 0
    end = len(data_list) - 1
    f_s = start
    f_e = end
    while f_s < f_e:
        mid = (f_s + f_e) // 2
        if cmp_func(data_list[mid], element) == 0:
            f_s = f_e = mid
        elif cmp_func(f_s, element) == -1:
            f_s = mid + 1
        elif cmp_func(f_s, element) == 1:
            f_e = mid - 1
    if f_s > f_e:
        return -1
    else:
        return f_s

def cmp_func(a, b):
    if a == b:
        return 0
    elif a < b:
        return -1
    elif a > b:
        return 1

if __name__ == '__main__':
    # import unittest
    # unittest.main()
    print(binary_search([1, 2, 3], 3, cmp_func))