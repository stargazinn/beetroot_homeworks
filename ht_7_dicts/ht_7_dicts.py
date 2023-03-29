# # Task 1
# sentence = input("Write some sentence: ")
# keys = sentence.split()
# values = []
# for key in keys:
#     values.append(keys.count(key))
# my_dict = dict(zip(keys, values))
# print(my_dict)
#
# Task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
product = [key for key in stock.keys()]
quantity = [value for value in stock.values()]
sum = [value for value in prices.values()]
total = 0
for i in range(len(product)):
    total += quantity[i]*sum[i]

print(f"Total price of the stock: {total}")


# #Task 3
# l = [(i, j := i**2) for i in range(1, 11)]
# print(l)
#
# # Task 4
# import calendar
#
# # 1.
# days_of_week = [day for day in calendar.day_name]
# print(days_of_week)
# # 2.
# task4_dict1 = {(key := days_of_week.index(value) + 1) : value for value in days_of_week}
# print(task4_dict1)
# # 3.
# task4_dict2 = {value : key for key, value in task4_dict1.items()}
# print(task4_dict2)

