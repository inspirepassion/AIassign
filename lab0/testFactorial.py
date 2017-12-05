def factorial(x):
    value_factorial = 1
    if x<0: print("input should not be less than 0")
    elif x==0:  return value_factorial
    else:
        for i in range(1, x+1):
            value_factorial *= i
        return value_factorial

input_factorial = int(raw_input("plese input a number"))
print factorial(input_factorial)