a = []
while True:
    b = input("Enter the payment (enter 'exit' to stop): ")
    if b == "exit":
        break  
    else:
        a.append(int(b)) 
        print(f"your bill for now is {a}")

total = sum(a)

print("Sum of payments:", total)
