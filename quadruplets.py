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

    Big-O notation:
        O(n^4)
    '''
    for i in range(0, len(list) - 3):
        for j in range(i + 1, len(list) - 2):
            for k in range(j + 1, len(list) - 1):
                for l in range(k + 1, len(list)):
                    if list[i] + list[j] + list[k] + list[l] == target_sum:
                        n = print([list[i], list[j], list[k], list[l]])
                        return n
   

quadruplets(list, target_sum)