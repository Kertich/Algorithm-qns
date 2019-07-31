array_a = [-1, 5, 10, 20, 28, 3]
array_b = [26, 134, 135, 15, 17]

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

    Big-O notation:
    ---------------
        O(n):Linear Compexity 
    '''
    getmin = []
    getmax = []
    for i in array_a:
        if i in array_a:
            getmin.append(i)
        
    minnum = min(getmin)
        
    for j in array_b:
        if j in array_b:
            getmax.append(j)
    maxnum = max(getmax)
     

    return print([minnum, maxnum])


smalldifference(array_a, array_b)

        