try:
    year = int(input("请输入年份："))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")
except ValueError:
    print("输入无效，请输入一个有效的数字年份")

