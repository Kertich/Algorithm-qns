list = [12, 3, 1, 2, -6, 5, -8, 6]
target_sum = 0

def triple(list, target_sum):
    '''
    Returns lists of arrays with three values that sum up to zero(0)

    Parameters:
    -----------
        list(iterables), target_sum(iterable): Takes two parameters

    Returns:
    --------
        Returns lists with three values that sum up to zero(0). 
    '''
    for i in list:
        for j in list:
            if j != i:
                for k in list:
                    if k != i and k != j: 
                        if int(i + j + k) == 0:
                            print([i, j, k])
triple(list, target_sum)
