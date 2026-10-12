def is_even(n):
    return n % 2 == 0  # بررسی زوج بودن عدد

def get_odds(nums):
    odds = []  # لیست خالی برای ذخیره اعداد فرد
    count = 0 # تعداد شمارش فرد که صفر هستش

    for number in nums:  # بررسی هر عدد در لیست
        if not is_even(number):  # اگر عدد فرد باشد (نه زوج)
            odds.append(number)  # آن را به لیست اضافه کن
            count += 1 # هر دفعه فرد دیدی یدونه بشمر

    return count, odds  # بازگرداندن لیست اعداد فرد و تعداد انها

my_list = [1, 2, 6, 8, 2, 5, 3]  # لیست اعداد ورودی
odds_count, my_odds = get_odds(my_list)  # فراخوانی توابع
print(my_odds, odds_count, sep= '\n')  # 3 خروجی: [1, 5, 3]
