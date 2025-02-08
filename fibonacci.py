def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth number.
    
    Args:
        n (int): The number of terms in the sequence.
    
    Returns:
        list: A list of Fibonacci numbers.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage
n = 10  # Number of terms
print(fibonacci(n))