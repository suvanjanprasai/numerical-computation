import math
from sympy import symbols,diff

xx = symbols('x')


func = input("Enter: ")
derivative_of_func = input("Enter f'(x): ")
x1 = int(input("Let x1: "))
iterations = int(input("Iterations: "))

if derivative_of_func == "na" or derivative_of_func == "NA" or derivative_of_func == "":
    derivative_of_func = diff(func, xx)

if "^" in str(func):
    func = str(func).replace("^", "**")

e = math.e
functions = ["sin","cos","tan","log"]
for i in functions:
    if i in str(func):
        func = str(func).replace(f"{i}(x)", f"math.{i}(x*(math.pi)/(180))")


    if i in str(derivative_of_func):
        derivative_of_func = str(derivative_of_func).replace(f"{i}(x)", f"math.{i}(x*(math.pi)/(180))")


x=x1
for i in range(1,iterations):
    x2 = x1 - eval(str(func))/eval(str(derivative_of_func))
    x1=x2
    x=x2

print(x1)