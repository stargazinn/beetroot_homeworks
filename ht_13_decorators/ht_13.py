# # Task 1
# from functools import wraps
# def logger(func):
#     wraps(func)
#     def wrapper(*args):
#         func(*args)
#         arguments = ', '.join(map(str, args))
#         print(f"{func.__name__} called with {arguments}")
#     return wrapper
#
#
#
# @logger
# def add(x, y):
#     return x + y
#
#
# @logger
# def square_all(*args):
#     return [arg ** 2 for arg in args]
#
#
# add(4, 5)
# square_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# # Task 2
# from functools import wraps
# def stop_words(words: list):
#     def stop_words_inner(func):
#         @wraps(func)
#         def wrapper(name):
#             text = func(name)
#             for word in words:
#                 text = text.replace(word, '*')
#             return text
#         return wrapper
#     return stop_words_inner
#
#
# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
#
#
# print(create_slogan('Volodymyr'))
#
#
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
#
# # Task 3
# from functools import wraps
# 
# def arg_rules(type_: type, max_length: int, contains: list):
#     def arg_rules_inner(func):
#         @wraps(func)
#         def wrapper(name):
#             a, b = False, False
#             if type(name) != type_:
#                 print(f"Wrong type {type(name)}, should be: {type_}!")
#                 return False
#             elif len(name) > max_length:
#                 print(f"Too many symbols ({len(name)}), should be: {max_length}!")
#                 return False
#             elif not all(sym in name for sym in contains):
#                 print(f"Name {name} should contain following symbols: {contains}!")
#                 return False
#             else:
#                 return func(name)
#         return wrapper
#     return arg_rules_inner
#
#
# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
#
#
# assert create_slogan('johndoe05@gmail.com') is False
#
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
#
# assert create_slogan(123) is False

