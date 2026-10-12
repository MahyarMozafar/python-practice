
def largest(nums):
    '''
    this function finds largest number in your list
    
    '''
    largest_number = nums[0]  # شروع با اولین عدد لیست
    for n in nums:            # بررسی هر عدد در لیست
        if largest_number < n:  # اگر عدد فعلی بزرگتر از مقدار فعلی باشد
            largest_number = n  # آن را به عنوان بزرگترین عدد جدید تنظیم کن
    return largest_number     # بزرگترین عدد را برمی‌گرداند

my_nums = [1, 5, 8, 3, 9, 11, 7]  # لیست اعداد
largest_number = largest(my_nums)   # فراخوانی تابع
print(largest_number)              # خروجی: 11