# # Task 1
#
# class Person:
#     def __init__(self, firstname, lastname, age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#
#
#     def talk(self):
#         print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old.")
#
#
# new_person = Person('Carl', 'Johnson', 26)
# new_person.talk()
#
# Task 2
#
# class Dog:
#     age_factor = 7
#
#     def __init__(self, age):
#         self.age = age
#
#
#     def human_age(self):
#         return self.age * self.age_factor
#
# my_dog = Dog(10)
# print(my_dog.human_age())
#
# # Task 3
#
# CHANNELS = ["BBC", "Discovery", "TV1000"]
#
#
# class TVController:
#
#     def __init__(self, list_of_channels):
#         self.list_of_channels = list_of_channels
#         self.num_of_cur_channel = 0
#
#     def first_channel(self):
#         self.num_of_cur_channel = 0
#         return self.list_of_channels[self.num_of_cur_channel]
#
#
#     def last_channel(self):
#         self.num_of_cur_channel = len(self.list_of_channels) - 1
#         return self.list_of_channels[self.num_of_cur_channel]
#
#
#     def turn_channel(self, n):
#         self.num_of_cur_channel = n - 1
#         return self.list_of_channels[self.num_of_cur_channel]
#
#
#     def next_channel(self):
#         if self.num_of_cur_channel == len(self.list_of_channels)-1:
#             self.num_of_cur_channel = 0
#             return self.list_of_channels[self.num_of_cur_channel]
#         else:
#             self.num_of_cur_channel += 1
#             return self.list_of_channels[self.num_of_cur_channel]
#
#
#     def previous_channel(self):
#         if self.num_of_cur_channel == 0:
#             self.num_of_cur_channel = len(self.list_of_channels) - 1
#             return self.list_of_channels[self.num_of_cur_channel]
#         else:
#             self.num_of_cur_channel -= 1
#             return self.list_of_channels[self.num_of_cur_channel]
#
#
#     def show_current_channel(self):
#         return self.list_of_channels[self.num_of_cur_channel]
#
#
#     def is_exist(self, n_or_name):
#         if type(n_or_name) == int:
#             if n_or_name <= len(self.list_of_channels) and n_or_name >= 1:
#                 return 'Yes'
#             else:
#                 return 'No'
#         elif type(n_or_name) == str:
#             if n_or_name in self.list_of_channels:
#                 return 'Yes'
#             else:
#                 return 'No'
#
#
# controller = TVController(CHANNELS)
# # print(controller.turn_channel(3))
# # controller.show_current_channel()
#
# # print(controller.next_channel())
# # controller.previous_channel()
# # print(controller.show_current_channel())
# # print(controller.is_exist(4))
# # print(controller.is_exist('BBC'))
# # # ---------------------------------------
# print(controller.turn_channel(2))
# print(controller.first_channel())
# print(controller.last_channel())
# print(controller.next_channel())





