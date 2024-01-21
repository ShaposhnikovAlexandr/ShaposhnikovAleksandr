def factorial(n):
    res = 1; i = 1
    while i <= n:
        res*=i
        i+=1
    return res

n = int(input("Введите n: "))

print("n! = "+str(factorial(n)))
