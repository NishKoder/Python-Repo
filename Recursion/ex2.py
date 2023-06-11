def rec_mul(n):
    """ Mulplier of number with recursion
    
    Args:
    n: Number for mulipler
    
    Return:
    Integer
    """
    if n == 1:
        return 1
    return n * rec_mul(n - 1)

print(rec_mul(5))