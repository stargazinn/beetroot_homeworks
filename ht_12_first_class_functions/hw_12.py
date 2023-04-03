# # Task 1
# def test_func():
#     local_var_1 = 1
#     local_var_2 = 2
#     local_var_3 = 3
#     local_var_4 = 4
#     print('hi')
#
#
# print(f"Number of local variables declared in {test_func.__name__} is {test_func.__code__.co_nlocals}.")

# Task 2
def first_fun(var1):
    print(f"This is first_fun and variable is equal to {var1}")
    def second_fun():
        nonlocal var1
        var1 = 1
        print(f"This is second_fun and variable is equal to {var1}")
        return 'tu-tu-ru'
    return second_fun


a = first_fun(2030)
print(a())

# # Task 3
# def choose_func(nums, func1, func2):
#     if all([i > 0 for i in nums]):
#         return func1(nums)
#     else:
#         return func2(nums)
#
#
# # Assertions
#
# nums1 = [1, 2, 3, 4, 5]
#
# nums2 = [1, -2, 3, -4, 5]
#
#
# def square_nums(nums):
#     return [num ** 2 for num in nums]
#
#
# def remove_negatives(nums):
#     return [num for num in nums if num > 0]
#
#
# # print(choose_func(nums2, square_nums, remove_negatives))
#
# assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25], "not working right"
#
# assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5], "not working right"
# # assert (choose_func(nums2, square_nums, remove_negatives) == [1, 3, 4]), "not working right"
#
