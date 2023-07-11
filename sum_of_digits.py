def sum_of_digits(num: int):
    if num == 0:
        return num
    
    return num % 10 + sum_of_digits(num // 10)

gss = sum_of_digits(208)
print(gss)