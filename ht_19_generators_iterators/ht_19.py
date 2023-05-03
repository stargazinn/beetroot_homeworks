# # Task 1
# def with_index(iterable, start = 0):
#     for i in iterable:
#         yield (start, i)
#         start += 1
#
#
# my_list = ['a', 'b', 'c', 'd']
# for i, j in with_index(my_list, 1):
#     print(f'{i}: {j}')
#
# # Task 2
# def in_range(start, end, step = 1):
#     while start < end:
#         yield start
#         start += step
#
# for i in in_range(0, 10):
#     print(i)
#
# # Task 3
#
# class OwnIterable:
#     def __init__(self, iterable):
#         self._iterable = iterable
#
#     def __iter__(self):
#         self._index = 0
#         return self
#
#     def __next__(self):
#         if self._index < len(self._iterable):
#             value = self._iterable[self._index]
#             self._index += 1
#             return value
#         else:
#             raise StopIteration
#
#     def __getitem__(self, index):
#         return self._iterable[index]
#
#
#
#
# iterable = OwnIterable([1, 2, 3])
#
#
# for element in iterable:
#     print(element)
#
# print()
# print(iterable[0])
# print(iterable[2])