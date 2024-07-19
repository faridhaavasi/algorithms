# تعریف تابعی برای پیدا کردن اعداد تکراری در لیست
def find_duplicates(input_list):
    # ایجاد دیکشنری برای شمارش تکرار هر عدد
    count_dict = {}

    # شمارش تعداد تکرار هر عدد در لیست
    for num in input_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # لیست اعداد تکراری
    duplicates = []
    for num, count in count_dict.items():
        if count > 1:
            duplicates.append(num)

    return duplicates


# تست برنامه با یک لیست نمونه
sample_list = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7, 8, 9, 7]
duplicates = find_duplicates(sample_list)

# چاپ اعداد تکراری
print("اعداد تکراری در لیست عبارتند از:", duplicates)
