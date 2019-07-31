list = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10 

def sum_two(list, target_sum):
    '''
    Returns a list with two values that sum up to 10

    Parameters:
    -----------
        list(iterables), target_sum(iterable): Takes two parameters

    Returns:
    --------
        Returns a list with two values that sum up to 10.

    Big-O notation:
    ---------------
        O(n):Linear complexity 
    '''

    for x in list:
        if(target_sum-x) in list and (x-target_sum) in list:
            print([x, target_sum - x])
                    
sum_two(list, target_sum)