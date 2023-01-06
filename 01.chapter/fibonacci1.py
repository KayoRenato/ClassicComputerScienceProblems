def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    print(fibonacci(5))
    print(fibonacci(50)) # Exponential Grow Up - Never Over