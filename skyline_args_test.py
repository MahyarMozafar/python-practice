def skyline(*args):
    if not args:  # بررسی اینکه آیا ورودی وجود دارد یا خیر
        return 0
    return max(args)  # بازگرداندن بیشترین ارتفاع

# دریافت ورودی از کاربر
data = input().split()
heights = [int(x) for x in data]
print(skyline(*heights))