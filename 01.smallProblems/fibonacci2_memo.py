# Recursive Solution

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1} # base cases

def fibonacci(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2) # memorization
        return memo[n]
    return memo[n]

if __name__ == "__main__":
    print(fibonacci(5))
    print(fibonacci(50))
    print(memo)
