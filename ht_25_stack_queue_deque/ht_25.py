# # Task 1
#
# from string import ascii_lowercase as asu
#
# class Stack:
#     def __init__(self):
#         self._items = []
#
#     def is_empty(self):
#         return self._items == []
#
#     def push(self, item):
#         self._items.append(item)
#
#     def pop(self):
#         return self._items.pop()
#
#     def peek(self):
#         return self._items[len(self._items) - 1]
#
#     def size(self):
#         return len(self._items)
#
#     def __repr__(self):
#         representation = "<Stack>\n"
#         for ind, item in enumerate(reversed(self._items), 1):
#             representation += f"{ind}: {str(item)}\n"
#         return representation
#
#     def __str__(self):
#         return self.__repr__()
#
#
# if __name__ == "__main__":
#     s = Stack()
#     for _ in asu:
#         s.push(_)
#     print(s)
#
# #Task 2
#
# class Stack:
#     def __init__(self):
#         self._items = []
#
#     def is_empty(self):
#         return self._items == []
#
#     def push(self, item):
#         self._items.append(item)
#
#     def pop(self):
#         return self._items.pop()
#
#     def peek(self):
#         return self._items[len(self._items) - 1]
#
#     def size(self):
#         return len(self._items)
#
#     def __repr__(self):
#         representation = "<Stack>\n"
#         for ind, item in enumerate(reversed(self._items), 1):
#             representation += f"{ind}: {str(item)}\n"
#         return representation
#
#     def __str__(self):
#         return self.__repr__()
#
# def is_balanced(some_string):
#     s = Stack()
#     opening_brackets = "([{"
#     closing_brackets = ")]}"
#     for _ in some_string:
#         if _ in opening_brackets:
#             s.push(_)
#         elif _ in closing_brackets:
#             if s.is_empty() or opening_brackets.index(s.pop()) != closing_brackets.index(_):
#                 return False
#     return s.is_empty()
#
#
# print(is_balanced('(((123)))'))
# print(is_balanced('((123)'))
# print(is_balanced('[((123))]'))
# print(is_balanced('{[((123))]'))
#
# # Task 3.1
#
# class Stack:
#     def __init__(self):
#         self._items = []
#
#     def is_empty(self):
#         return self._items == []
#
#     def push(self, item):
#         self._items.append(item)
#
#     def pop(self):
#         return self._items.pop()
#
#     def peek(self):
#         return self._items[len(self._items) - 1]
#
#     def size(self):
#         return len(self._items)
#
#     def get_from_stack(self, e):
#         s1 = Stack()
#         founded = False
#         while not self.is_empty():
#             item = self.pop()
#             if item == e:
#                 founded = True
#                 continue
#             s1.push(item)
#         while not s1.is_empty():
#             self.push(s1.pop())
#         if founded:
#             return e
#         else:
#             raise ValueError(f'Element {e} is not in your stack')
#
#
#     def __repr__(self):
#         representation = "<Stack>\n"
#         for ind, item in enumerate(reversed(self._items), 1):
#             representation += f"{ind}: {str(item)}\n"
#         return representation
#
#     def __str__(self):
#         return self.__repr__()
#
#
# if __name__ == '__main__':
#     s = Stack()
#     some = 'qwerty'
#     for _ in some:
#         s.push(_)
#     print(s)
#     print(s.get_from_stack('e'))
#     # print(s.get_from_stack('u'))
#     print(s)
#
# # Task 3.2
#
# class Queue:
#     def __init__(self):
#         self._items = []
#
#     def is_empty(self):
#         return self._items == []
#
#     def enqueue(self, item):
#         self._items.insert(0, item)
#
#     def dequeue(self):
#         return self._items.pop()
#
#     def size(self):
#         return len(self._items)
#
#     def get_from_queue(self, e):
#         q1 = Queue()
#         founded = False
#         while not self.is_empty():
#             item = self.dequeue()
#             if item == e:
#                 founded = True
#                 continue
#             q1.enqueue(item)
#         while not q1.is_empty():
#             self.enqueue(q1.dequeue())
#         if founded:
#             return e
#         else:
#             raise ValueError(f'Element {e} is not in your queue')
#
#
#     def __repr__(self):
#         representation = "<Queue>\n"
#         for ind, item in enumerate(reversed(self._items), 1):
#             representation += f"{ind}: {str(item)}\n"
#         return representation
#
#     def __str__(self):
#         return self.__repr__()
#
#
# if __name__ == "__main__":
#     q = Queue()
#     q.enqueue(4)
#     q.enqueue('dog')
#     q.enqueue(True)
#     print(q)
#     q.get_from_queue('dog')
#     print(q)
