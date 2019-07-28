list = [7, 6, 4, -1, 1, 2]
target_sum = 16

def quadruplets(list, target_sum):
    '''
    Returns lists with four values each that sum up to 16

    Parameters:
    -----------
        list(iterables), target_sum(iterable): Takes two parameters

    Returns:
    --------
        Returns lists with four values that sum up to 16. 
    '''
    for i in list:
        for j in list:
            if j != i:
                for k in list:
                    if k != i and k != j: 
                        for l in list:
                            if l != i and l != j and l != k:
                                if int(i + j + k + l) == target_sum:
                                    print(i, j, k, l)

quadruplets(list, target_sum)