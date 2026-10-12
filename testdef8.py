family_costs = {
    'omid': 3,
    'kaveh': 21,
    'parisa': 50
}

def family_costs_analisit(costs):
    person = ''     # نام کسی با بیشترین هزینه
    min_person = '' # نام کسی با کمترین هزینه 
    total = 0       # جمع کل هزینه‌ها
    count = 0       # تعداد افراد
    max_cost = -1   # بیشترین هزینه (مقدار)
    min_cost = float('inf') # کمترین هزینه (مقدار)
    for name, nums in costs.items():
        total += nums
        count += 1
        # بررسی بیشترین هزینه
        if nums > max_cost: 
            person = name   # ذخیره نام کسی با بیشترین هزینه
            max_cost = nums # ذخیره مقدار بیشترین هزینه
        # بررسی کمترین هزینه
        if nums < min_cost:
            min_cost = nums    # ذخیره مقدار کمترین هزینه
            min_person = name   # ذخیره نام کسی با کمترین هزینه
    average_cost = int(total / count)
    return average_cost, total , person, min_person, min_cost , max_cost 

avg, total , max_person, min_person, lowest_cost, highest_cost= family_costs_analisit(family_costs)
print(f"total costs : {total}Toman")
print(f"average cost : {avg}Toman")
print(f"max_cost: {highest_cost}Toman (by {max_person})") # نام کسی با بیشترین هزینه
print(f"thanks to {min_person} for lowest cost") # نام کسی با کمترین هزینه