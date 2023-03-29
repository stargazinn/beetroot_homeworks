# import random
#
# #Task 1
# rand_number = random.randint(1, 10)
# # print(rand_number)
# while True:
#     user_guess = int(input("Guess a random number between 1 and 10: "))
#     if user_guess == rand_number:
#         print("That's right!")
#         break
#     elif user_guess < 0 or user_guess > 10:
#         print("Choose a number between 1 and 10!")
#     else:
#         print("Try again!")
#     yes_or_no = input("Do you wanna continue? Enter y/n: ")
#     if yes_or_no == "n":
#         print("See ya!")
#         break
#
# #Task 2
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}, on your next birthday you’ll be {age + 1} years")
#
# #Task 3
# string = input("Enter a string: ")
# new_string = ""
# for i in range(1, 6):
#     print(new_string.join(random.sample(string, len(string))))