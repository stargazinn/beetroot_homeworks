# import random
#
# # Task 1
# i = 1
# my_list = []
# while i <= 10:
#     my_list.append(random.randint(1, 100))
#     i += 1
# print(my_list)
# max = my_list[0]
# i = 1
# while i < len(my_list):
#     if max < my_list[i]:
#         max = my_list[i]
#     i += 1
# print(max)
#
# #Task 2
# i = 1
# my_list1 = []
# my_list2 = []
# my_list3 = []
# while i <= 10:
#     my_list1.append(random.randint(1, 10))
#     my_list2.append(random.randint(1, 10))
#     i += 1
# for i in my_list1:
#     if i in my_list2 and i not in my_list3:
#         my_list3.append(i)
# print(f"List #1: {my_list1}\nList #2: {my_list2}\nCommon integers between the 2 initial lists {my_list3}")
#
# # Task 3
# # all_integers = []
# # i = 1
# # while i <= 100:
# #     all_integers.append(i)
# #     i += 1
# # print(all_integers)
# # my_list4 = []
# # i = 0
# # while i < len(all_integers):
# #     if i % 7 == 0 and i % 5 != 0:
# #         my_list4.append(i)
# #     i += 1
# # print(my_list4)
