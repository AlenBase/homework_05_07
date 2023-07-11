def fibonacci(number: int):
    if number <=2 :
        return 1
    return fibonacci(number - 1) +  fibonacci(number - 2)

gss = fibonacci(15)
print(gss)