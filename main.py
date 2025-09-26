try:
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")
except ValueError:
    print()
