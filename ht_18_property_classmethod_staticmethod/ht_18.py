# # Task 1
# import re
#
# class IsValidEmail:
#
#     def __init__(self, email):
#         self.email = email
#         self.validate(self.email)
#
#     @classmethod
#     def validate(cls, email):
#         check = None
#         pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#         if re.match(pattern, email) and email[email.index('@')-1] not in '.-_':
#             for _ in email:
#                 if _ in '.-_' and (email[email.index(_)-1] in '.-_' or email[email.index(_)+1] in '.-_'):
#                     check = False
#
#             if check is False:
#                 print("Invalid Email")
#             else:
#                 print("Valid Email")
#         else:
#             print("Invalid Email")
#
#
# is_valid = IsValidEmail('ja..ngo@gmail.com')
# # Task 2
#
# class Boss:
#
#     def __init__(self, id_: int, name: str, company: str):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.workers = []
#
#     def add_worker(self, worker):
#         self.workers.append(worker)
#
#
# class Worker:
#
#     def __init__(self, id_: int, name: str, company: str, boss: Boss):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self._boss = boss
#
#     @property
#     def boss(self):
#         return self._boss
#
#     @boss.setter
#     def boss(self, boss):
#         if isinstance(boss, Boss):
#             self._boss = boss
#             self._boss.add_worker(self)
#
#
#
# boss1 = Boss(0, 'name_boss1', 'company1')
# boss2 = Boss(1, 'name_boss2', 'company2')
#
# worker1 = Worker(2, 'name_w1', 'company1', boss1)
# worker2 = Worker(3, 'name_w2', 'company1', boss1)
# worker3 = Worker(4, 'name_w3', 'company2', boss2)
# worker4 = Worker(5, 'name_w4', 'company2', boss2)
#
#
# worker1.boss = boss1
# worker2.boss = boss1
#
# worker3.boss = boss2
# worker4.boss = boss2
#
# print(worker1.boss)
# print(boss1.workers)
# print(boss2.workers)
#
# # Task 3
# from functools import wraps
#
#
# class TypeDecorators:
#     @staticmethod
#     def to_int(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return int(func(*args, **kwargs))
#             except (TypeError, ValueError):
#                 return None
#
#         return wrapper
#
#     @staticmethod
#     def to_str(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return str(func(*args, **kwargs))
#             except (TypeError, ValueError):
#                 return None
#
#         return wrapper
#
#     @staticmethod
#     def to_bool(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return bool(func(*args, **kwargs))
#             except (TypeError, ValueError):
#                 return None
#
#         return wrapper
#
#     @staticmethod
#     def to_float(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return float(func(*args, **kwargs))
#             except (TypeError, ValueError):
#                 return None
#
#         return wrapper
#
#
# if __name__ == '__main__':
#     @TypeDecorators.to_int
#     def do_nothing(string: str):
#         return string
#
#     @TypeDecorators.to_bool
#     def do_something(string: str):
#         return string
#
#
#
#     assert do_nothing('25') == 25
#
#     assert do_something('True') is True


