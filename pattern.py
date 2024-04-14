# for i in range(6):
#     print(" "*(6-i)+"* "*i)
# for i in range(6):
#     print(". "*i+ "*"*(5-i))

# user_input = input("Enter '1' to say hi, or anything else to say bye: ")
# if user_input == '1':
#     print("Hi!")
# else:
#     print("Bye!")


# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#     print("Even")
# else:
#     print("Odd")
    


# def check_last_digit_divisible_by_5():
#     user_input = input("Enter a number: ")
    
#     # Check if the input is a valid integer
#     if user_input.isdigit():
#         # Get the last digit of the number
#         last_digit = int(user_input[-1])
        
#         # Check if the last digit is divisible by 5
#         if last_digit % 5 == 0:
#             print("The last digit of the number is divisible by 5.")
#         else:
#             print("The last digit of the number is not divisible by 5.")
#     else:
#         print("Invalid input. Please enter a valid integer.")

# check_last_digit_divisible_by_5()

# user_input = int(input("Enter a number: "))
# if((user_input%10)%5 == 0):
#     print("yes")
# else:
#     print("not")


# entered_pin = input("Enter your PIN: ")
# ATM_PIN = "2345"
# Balance = 5000

# if entered_pin == ATM_PIN:
#     withdrawal_amount = float(input("Enter the amount to withdraw: "))
    
#     if withdrawal_amount > 0 and withdrawal_amount <= Balance:
#         Balance -= withdrawal_amount
#         print("Cash withdrawn successfully.")
#         print("Remaining balance: ", Balance)
#     elif withdrawal_amount <= 0:
#         print("Invalid amount. Please enter a positive amount to withdraw.")
#     else:
#         print("Insufficient balance.")
# else:
#     print("Incorrect PIN. Access denied.")   
# Take input for 5 subjects
# subject1 = float(input("Enter marks for subject 1: "))
# subject2 = float(input("Enter marks for subject 2: "))
# subject3 = float(input("Enter marks for subject 3: "))
# subject4 = float(input("Enter marks for subject 4: "))
# subject5 = float(input("Enter marks for subject 5: "))

# # Calculate total marks
# total_marks = subject1 + subject2 + subject3 + subject4 + subject5

# # Calculate average marks
# if total_marks > 0:
#     average_marks = total_marks / 5
#     print("Average marks:", average_marks)
#     if average_marks > 90:
#         print("Grade: A")
#     elif(average_marks > 80):
#         print("Grade: B")
#     elif(average_marks > 70):
#         print("Grade: C")
#     elif(average_marks > 60):
#         print("Better luck next time")
# else:
#     print("Invalid marks entered. Please enter positive marks for all subjects.")
# def anant (a,b):
#     return a+b


# print(anant(2,3))


# def add(a,b):
#     return a+b
# def mul(a,b):
#     return a*b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b

# print(add(2,3))
# print(mul(2,3))
# print(sub(2,3))
# print(div(27,3))

# def get_pi():
#     return 3.14

# print(get_pi())


# def fact(a):
#     if a==1:
#         return 1
#     else:
#         return a+fact(a-1)

# print(fact(5))



def lcm(a, b):
    gcd = hcf(a, b)
    return (a * b)

def hcf(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

num1 = int(input("Enter first NO: "))
num2 = int(input("Enter second NO: "))

print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))

