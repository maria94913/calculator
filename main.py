a= int(input("Введи перше число:"))
b= int(input("Введи друге число:"))
c=input("Введи оперицію:")
if c == "+":
    print(a + b)
if c == "-":
    print(a - b)
if c == "*":
    print(a * b)
if c == "/":
    if b == 0:
        print("Помилка")
    else:
        print(a / b)
