array_a = [-1, 5, 10, 20, 28, 3]
array_b = [26, 134, 135, 15, 17]
get = []
def smalldifference(array_a, array_b):
    '''
    Prints a list of two values each from different array(array_a, array_b). 
    The difference of the two values returns the smallest difference.

    Parameters:
    ----------
        array_a(iterable), array_b(iterable): Takes in two lists of arrays

    Returns:
    -------
        Returns a list of with two values each from a different array(array_a and array_b) 
    '''
    for i in array_a:
        for j in array_b:

            n = i - j
            m = j - i
            get.append(m)
            get.append(n)
    for k in get:
        if k == min(get):
            n =print([i, j])
            return n

smalldifference(array_a, array_b)

        