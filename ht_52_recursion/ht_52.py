# # Task 1
#
# from typing import Union
# def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
#     if exp < 0:
#         raise ValueError("This function works only with exp > 0.")
#     elif exp == 0:
#         return 1
#     elif exp == 1:
#         return x
#     else:
#         return x * to_power(x, exp - 1)
#
#
# print(to_power(2, 3) == 8)
# print(to_power(3.5, 2) == 12.25)
# # print(to_power(2, -1))
# #
# # Task 2
#
# def is_palindrome(looking_str: str, index: int = 0) -> bool:
#     if index >= (len(looking_str) - 1) / 2:
#         return True
#     elif looking_str[index] != looking_str[len(looking_str) - 1 - index]:
#         return False
#     else:
#         return is_palindrome(looking_str, index + 1)
#
#
#
# print(is_palindrome('mooom'))
# print(is_palindrome('saswsas'))
# print(is_palindrome('o223o'))
# # Task 3
# #
# def mult(a: int, n: int) -> int:
#     if a < 0 or n < 0:
#         raise ValueError("This function works only with positive integers")
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return a
#     else:
#         return a + mult(a, n - 1)
#
#
# print(mult(2, 8))
# print(mult(-15,3))
#
# # Task 4
# def reverse(input_str: str) -> str:
#     if len(input_str) == 1:
#         return input_str
#     else:
#         return reverse(input_str[1:]) + input_str[0]
#
#
# print(reverse('hola'))
#
# # Task 5
# def sum_of_digits(digit_string: str) -> int:
#     if not digit_string.isdigit():
#         raise ValueError("input string must be digit string")
#     if len(digit_string) == 1:
#         return int(digit_string)
#     else:
#         return int(digit_string[0]) + sum_of_digits(digit_string[1:])
#
#
# print(sum_of_digits('31'))
# print(sum_of_digits('3131'))
# print(sum_of_digits('123456789'))