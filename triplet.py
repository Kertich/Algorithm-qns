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

    Big-O notation:
    ---------------
        O(n^3):Cubic complexity
    '''
    for i in range(0, len(list) - 2):
        for j in range(i + 1, len(list) - 1):
            for k in range(j + 1, len(list)):
                if list[i] + list[j] + list[k] == target_sum:
                    print([list[i], list[j], list[k]])


  
triple(list, target_sum)
