list = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10 

def sum_two(list, target_sum):
    '''
    Returns lists with two values that sum up to 10

    Parameters:
    -----------
        list(iterables), target_sum(iterable): Takes two parameters

    Returns:
    --------
        Returns lists with two values that sum up to 10. 
    '''
    for i in list:
       
        for j in list:
            if j != i:
         
                if i + j == 10:
                    print([i, j])
sum_two(list, target_sum)