# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    """Returns sum of two integers between 0 and 100"""

    test_for_valid_input = x >= 0 and x <= 100 and y >= 0 and y <=100

    if test_for_valid_input:
        return x + y
    else:
        return None
    
