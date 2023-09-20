# Recursive function to generate Fibonacci series
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Input: Number of terms in the Fibonacci series
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Call the recursive function to generate the Fibonacci series
fib_series = fibonacci_recursive(n)

# Print the generated Fibonacci series
print(f"Fibonacci series up to {n} terms:", fib_series)
