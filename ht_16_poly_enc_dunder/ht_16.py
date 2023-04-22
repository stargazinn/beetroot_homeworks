# # Task 1
# class Animal:
#
#     def talk(self):
#         print('*sound of animal!')
#
#
# class Dog(Animal):
#
#     def talk(self):
#         print('auf!')
#
#
# class Cat(Animal):
#
#     def talk(self):
#         print('meow!')
#
#
# def animal_talking(instance):
#     instance.talk()
#
#
# my_dog = Dog()
# my_cat = Cat()
# animal_talking(my_dog)
# animal_talking(my_cat)
#
# Task 2
class Author:

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'Author: {self.name}\nCountry: {self.country}\nBirthday: {self.birthday}\nBooks: {self.books}'

    def __str__(self):
        return f'Author: {self.name}\nCountry: {self.country}\nBirthday: {self.birthday}\nBooks: {self.books}'


class Book:

    num_of_books = 0
    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.num_of_books += 1


    def __repr__(self):
        return f'Book {self.name} was written by {self.author} in {self.year}'


    def __str__(self):
        return f'Book {self.name} was written by {self.author} in {self.year}'


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.authors.append(author.name)
        self.books.append(book)
        author.books.append(book.name)
        return book

    def group_by_author(self, author: Author):
        return author.books

    def group_by_year(self, year: int):
        grouped_by_year = []
        for book in self.books:
            if book.year == year:
                grouped_by_year.append(book.name)
        return grouped_by_year

    def __repr__(self):
        return f'Library {self.name} has {len(self.books)} books by {len(self.authors)} authors)'

    def __str__(self):
        return f'Library {self.name} has {len(self.books)} books by {len(self.authors)} authors'



taras_shevchenko = Author('Taras Shevchenko', 'Ukraine', '09.03.1814')
ivan_kotliarevsky = Author('Ivan Kotliarevsky', 'Ukraine', '09.09.1769')
lesya_ukrainka = Author('Lesya Ukrainka', 'Ukraine', '25.02.1871')

my_lib = Library('My Library')
my_lib.new_book('Kobzar', 1840, taras_shevchenko)
my_lib.new_book('Eneida', 1798, ivan_kotliarevsky)
my_lib.new_book('Natalka Poltavka', 1798, ivan_kotliarevsky)
# my_lib.new_book('Forest Song', 1911, lesya_ukrainka)
# my_lib.new_book('das asda', 1911, taras_shevchenko)
#
# print(my_lib.books)
# print(my_lib.authors)
print(ivan_kotliarevsky.books)
# print(ivan_kotliarevsky.books)
# print(my_lib.group_by_author(ivan_kotliarevsky))
# print(my_lib.group_by_year(1911))
#
#
# # Task 3
# from math import lcm
#
# class Fraction:
#
#     def __init__(self, a, b):
#         if b == 0:
#             raise ZeroDivisionError("Denominator cannot be 0!")
#         self.a = a
#         self.b = b
#
#     def __add__(self, other):
#         if isinstance(other, Fraction):
#             nsk = lcm(self.b, other.b)
#             return Fraction(int(self.a * nsk/self.b+other.a * nsk/other.b), int(nsk))
#
#     def __sub__(self, other):
#         if isinstance(other, Fraction):
#             nsk = lcm(self.b, other.b)
#             return Fraction(int(self.a * nsk/self.b-other.a * nsk/other.b),nsk)
#
#     def __mul__(self, other):
#         if isinstance(other, Fraction):
#             return Fraction(self.a * other.a, self.b * other.b)
#
#     def __truediv__(self, other):
#         if other.a == 0:
#             raise ZeroDivisionError("Denominator cannot be 0!")
#         if isinstance(other, Fraction):
#             return Fraction(self.a * other.b,self.b * other.a)
#
#     def __str__(self):
#         if self.a % 1 == 0:
#             self.a = int(self.a)
#         return f'{str(self.a)}/{self.b}'
#
#     def __eq__(self, other):
#         return self.a == other.a and self.b == other.b
#
#     def __lt__(self, other):
#         return self.a * other.b < other.a * self.b
#
#     def __gt__(self, other):
#         return self.a * other.b > other.a * self.b
#
#
#
#
# if __name__ == '__main__':
#     a = Fraction(1, 2)
#     b = Fraction(1, 4)
#
#     print(a + b)
#     print(Fraction(3, 4))
#     print(a+b == Fraction(3, 4))
#     print(a<b)
