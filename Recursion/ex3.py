def rec_fibonaci(n):
    """ Fibonaci of number with recursion
    
    Args:
    n: Number for Fibonaci
    
    Return:
    Int
    """
    if n <= 1:
        return n
    else:
        return rec_fibonaci(n - 1) + rec_fibonaci(n - 2)

print(rec_fibonaci(6))

def print_feb(n):
    """ Print Fibonaci of number with recursion
    
    Args:
    n: Number for Fibonaci
    
    Return:
    List[Int]
    """
    if n <=0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        feb_series = print_feb(n - 1)
        feb_series.append(feb_series[-1] + feb_series[-2])
        return feb_series
    print(feb_series)

print(print_feb(6))