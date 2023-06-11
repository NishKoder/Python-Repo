def rec_sum(n):
    """ Sum of number with recursion
    
    Args:
    n: Number for Sum
    
    Return:
    Integer
    """
    if n == 1:
        return 1
    else:
        return n + rec_sum(n - 1)

print(rec_sum(6))