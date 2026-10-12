donations = {
    'dariush': 20,
    'golnar': 800,
    'farhad': 12,
    'nasrin': 9
}

def donations_analiysis(don):
    person = ''
    total = 0
    count = 0
    max_donation = -1  # شروع با -1 برای پوشش موارد صفر
    for name, value in don.items():  # بررسی هر کلید-مقدار در دیکشنری
        total += value  # جمع کردن مبالغ
        count += 1     # شمارش تعداد کاربران
        
        if value > max_donation:  # بررسی اینکه آیا مبلغ فعلی بیشتر از بیشترین مبلغ قبلی است؟
            person = name  # ذخیره نام کاربر
            max_donation = value  # به‌روزرسانی بیشترین مبلغ

    average = int(total / count)  # محاسبه میانگین بصورت عدد صحیح
    return average, total, person  # بازگرداندن سه مقدار

avg, total, max_person = donations_analiysis(donations)
print(f"total donations: {total}")
print(f"average donation id {avg}")  # تایپو: باید "is" باشد
print(f"thanks to {max_person}")