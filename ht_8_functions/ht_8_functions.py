# #Task 1
# def favorite_movie(name):
#     print(f"My My favorite movie is named {name}")
#
#
# favorite_movie("There Will Be Blood")
#
# #Task 2
# def make_country(name, capital):
#     country_dict = {name : capital}
#     print(country_dict)
#
#
# make_country("Ukraine", "Kyiv")
#
# #Task 3
# def make_operation(operator, *args):
#     answer = 0
#     if operator == '+':
#         for i in args:
#             answer += i
#     elif operator == '-':
#         answer = args[0] * 2
#         for i in args:
#             answer -= i
#     elif operator == '*':
#         answer = 1
#         for i in args:
#             answer *= i
#     else:
#         print("There are only 3 operation this function can make: '+', '-' or '*'")
#     return answer
#
#
# a = make_operation('+', 7, 7, 2)
# b = make_operation('-', 5, 5, -10, -20)
# c = make_operation('*', 7, 6)
# print(a, b, c, sep="\n")
#
