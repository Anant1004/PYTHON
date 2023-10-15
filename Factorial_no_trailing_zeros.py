def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


if __name__ =="__main__":
    a = int(input("Enter the number"))
    b = factorial(a)
    print(f"The factorial of a number is {b}")
