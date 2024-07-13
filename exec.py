import time
import logging

logging.basicConfig(level=logging.INFO)

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
        return result
    return wrapper

@measure_time
def expensive_task(n):
    """A computationally expensive task: calculating the sum of prime numbers up to n."""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    return sum(num for num in range(2, n+1) if is_prime(num))

# Example usage
result = expensive_task(100000)
print(f"Sum of primes: {result}")


