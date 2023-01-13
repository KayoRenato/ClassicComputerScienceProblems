# Interactive Solution
# The Solution with the best performance than the others presented so far.

def fibonacci(n: int) -> int:
    if n == 2:
        return n

    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next

    return next


if __name__ == "__main__":
    print(fibonacci(5))
    print(fibonacci(50))  
