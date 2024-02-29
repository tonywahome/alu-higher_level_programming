#!/usr/bin/python3
a = 10
b = 5
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
sum_result = (a, b)
difference_result = subtract(a, b)
product_result = multiply(a, b)
division_result = divide(a, b)

output = "{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}".format(
        a, b, sum_result, a, b, difference_result, a, b, product_result, a, b, division_result)
print(output)
