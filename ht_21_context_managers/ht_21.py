# # Task 1
# import logging
# import unittest
# import os
#
# logging.basicConfig(level=logging.INFO)
# class OpenFile:
#     counter = 0
#     def __init__(self, file_name, method):
#         self.file_name = file_name
#         self.method = method
#         OpenFile.counter += 1
#
#     def __enter__(self):
#         self.file = open(self.file_name, self.method)
#         logging.info(f'{self.file_name} opened, counter: {OpenFile.counter}')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#         logging.info(f'{self.file_name} closed')
#
# # for i in range(1,5):
# #     with OpenFile(f'file{i}.txt', 'w') as file:
# #         for j in range(10):
# #             file.write('hola\n')
#
# # Task 2
#
# class ContextManagerTest(unittest.TestCase):
#
#     def test_if_opened(self):
#         with OpenFile('test.txt', 'w') as file:
#             self.assertTrue(os.path.exists('test.txt'))
#
#     def test_if_written(self):
#         with OpenFile('test.txt', 'w') as file:
#             file.write('test!')
#         with open('test.txt', 'r') as file:
#             text = file.read()
#             self.assertEqual(text, 'test!')
#
#     def test_if_closed(self):
#         with OpenFile('test.txt', 'w') as file:
#             pass
#         self.assertTrue(file.closed)
#
#     def test_not_exist(self):
#         with self.assertLogs(level=logging.ERROR):
#             with OpenFile('test1.txt', 'r') as file:
#                 pass
#
#
# if __name__ == "__main__":
#     unittest.main()

