
def count_lines(name):
    # with open(name) as file:
    #     number_of_lines = len(file.readlines())
    #     return number_of_lines
    number_of_lines = len(name.readlines())
    return number_of_lines



def count_chars(name):
    # with open(name) as file:
    #     number_of_chars = len(file.read())
    #     return number_of_chars
    number_of_chars = len(name.read())
    return number_of_chars



def test(name):
    # print(f"There are {count_lines(name)} lines in {name}")
    # print(f"There are {count_chars(name)} chars in {name}")
    with open(name) as file:
        print(f"There are {count_lines(file)} lines in {name}")
        file.seek(0)
        print(f"There are {count_chars(file)} chars in {name}")






