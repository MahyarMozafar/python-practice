
def number_of_evens(nums):
    '''
    this function counts number of evens in list
    '''
    def is_even(n):
        return (n % 2 == 0)

    count = 0
    for n in nums:
        if is_even(n):
            count += 1
    return count


count = number_of_evens([1, 2, 3, 6, 10, 11])
print(count)