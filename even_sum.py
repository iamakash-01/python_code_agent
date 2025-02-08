def sum_even_numbers(n):
    """
    This function calculates the sum of all even numbers from 1 to n.
    
    Parameters:
    n (int): The upper limit for the range of numbers.
    
    Returns:
    int: The sum of all even numbers in the specified range.
    """
    even_sum = sum(i for i in range(1, n+1) if i % 2 == 0)
    return even_sum

# Example usage
n = 19
result = sum_even_numbers(n)
print(f"The sum of all even numbers from 1 to {n} is: {result}")