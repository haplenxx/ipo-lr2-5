num = int(input("Введите число, состоящие из 8 разрядов: "))
sum = (num // 10000000) + (num // 1000000 % 10) + (num // 100000 % 10) + (num // 10000 % 10) + (num // 1000 % 10) + (num // 100 % 10) + (num // 10 % 10) + (num % 10)
print(sum)
