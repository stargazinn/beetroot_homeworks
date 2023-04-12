# # Task 1
#
# class Person:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#
#     def __str__(self):
#         return f'First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}'
#
# class Student(Person):
#
#     def __init__(self, first_name, last_name, age, grade, gpa):
#         self.grade = grade
#         self.gpa = gpa
#         super().__init__(first_name, last_name, age)
#
#
#     def __str__(self):
#         return f'First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}' \
#                f'\nGrade: {self.grade}\nGrade Point Average: {self.gpa}'
#
# class Teacher(Person):
#
#     def __init__(self, first_name, last_name, age, salary, subject):
#         self.salary = salary
#         self.subject = subject
#         super().__init__(first_name, last_name, age)
#
#
#     def __str__(self):
#         return f'First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}' \
#                f'\nSalary: {self.salary}$\nSubject: {self.subject}'
#
#
# print(default_person := Person('Fabrizio', 'Romano', 40))
# print('-'*20)
# print(student := Student('Adam', 'Smith', 14, 8, 9))
# print('-'*20)
# print(teacher := Teacher('William', 'Harrison', 44, 1000, 'Math'))
#
# # Task 2
#
# class Mathematician:
#
#     def square_nums(self, list_of_ints):
#         return [i**2 for i in list_of_ints]
#
#
#     def remove_positives(self, list_of_ints):
#         return list(filter(lambda i: i < 0, list_of_ints))
#
#
#     def filter_leaps(self, list_of_ints):
#         return list(filter(lambda i: i % 4 == 0, list_of_ints))
#
#
#
# m = Mathematician()
# # print(m.square_nums([2, 3, 4]))
# # print(m.remove_positives([-1, 2, 3, -5]))
# # print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
#
# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
#
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
#
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
#
# Task 3
# class Product:
#
#     def __init__(self, product_type, name, price):
#         self.product_type = product_type
#         self.name = name
#         self.price = price
#
# class ProductStore:
#
#     def __init__(self):
#         self.products = {}
#
#
#     def add(self, product, amount):
#         self.products[product.name] = {'type' : product.product_type,
#                                        'price' : product.price * 1.3,
#                                        'amount' : amount}
#
#
#     def set_discount(self, identifier, percent, identifier_type='name'):
#         for name, info in self.products.items():
#             if identifier_type == 'name' and name == identifier:
#                 self.products[identifier]['price'] *= percent/100
#             elif identifier_type == 'type' and info['type'] == identifier:
#                 self.products[name]['price'] *= percent/100
#
#
#     def sell_product(self, product_name, amount):
#         if amount <= self.products[product_name]['amount']:
#             self.products[product_name]['amount'] -= amount
#         else:
#              raise ValueError(f"There are only "
#                               f"{self.products[product_name]['amount']} "
#                               f"{product_name}'s left")
#
#     def get_all_products(self):
#         return self.products
#
#
#     def get_product_info(self, product_name):
#         return (product_name, self.products[product_name]['amount'])
#
#
# p = Product('Sport', 'Football T-Shirt', 100)
#
# p2 = Product('Food', 'Ramen', 1.5)
#
# s = ProductStore()
#
# s.add(p, 10)
#
# s.add(p2, 300)
#
# s.sell_product('Ramen', 10)
#
# assert s.get_product_info('Ramen') == ('Ramen', 290)
#
# # Task 4
#
# class CustomException(Exception):
#
#     def __init__(self, msg):
#         super().__init__(msg)
#         with open("logs.txt", 'a') as file:
#             file.write(f"{msg}\n")
#
#
# excptn = CustomException('SUCCES')
