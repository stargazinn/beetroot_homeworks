from string import Template

#Task 1
name = "Volodymyr"
day = "Friday"
print(f"Good day {name}! {day} is a perfect day to learn some python.")
print("Good day {}! {} is a perfect day to learn some python.".format(name, day))
print("Good day %s! %s is a perfect day to learn some python." % (name, day))
print(Template("Good day $name! $day is a perfect day to learn some python." ).substitute(name=name, day = day))
print("-" * 70)

#Task 2
first_name = "Volodymyr"
last_name = "Levchenko"
full_name = first_name + " " + last_name
print(f"Hello, {full_name}!")
print("-" * 70)

#Task 3
a = 3
b = 5
print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Division: ", a / b)
print("Multiplication: ", a * b)
print("Exponent (Power): ", a ** b)
print("Modulus: ", a % b)
print("Floor division : ", a // b)
