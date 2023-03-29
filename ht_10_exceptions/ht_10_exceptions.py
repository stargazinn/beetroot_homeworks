# Task 1

def oops():
    #raise IndexError('index error', 'index error 2')
    raise KeyError('key error', 'key error 2')

def try_except_block(*args):
    try:
        oops()
    except Exception as i:
        print(i.args)


try_except_block(1, 2, 3, 4, 5)


# Task 2

def func_task_2(a, b):
    try:
        print(float(a)**2/float(b))
    except ValueError:
        print("Enter only numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")


a = input("a: ")
b = input("b: ")
func_task_2(a, b)