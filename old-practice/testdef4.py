def is_even(n):
    return (n % 2 == 0)

def any_even_in_list(nums):
    '''
    returns True if any of numbers is even
    
    '''
    for n in nums:
        if is_even(n):
            return True
    return False
numbers = ([1, 2, 3 , 4 , 5 , 6])
print(any_even_in_list(numbers))
