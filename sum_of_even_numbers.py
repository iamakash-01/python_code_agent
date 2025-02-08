def sum_of_even_numbers(n):
    """
    This function calculates the sum of all even numbers from 1 to n.
    
    Parameters:
    n (int): The upper limit.
    
    Returns:
    int: The sum of all even numbers from 1 to n.
    """
    even_sum = sum(num for num in range(1, n+1) if num % 2 == 0)
    return even_sum

# Example usage
n = 10
result = sum_of_even_numbers(n)
print(f"The sum of even numbers from 1 to {n} is: {result}")