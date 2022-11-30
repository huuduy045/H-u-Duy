import math
print("Độ dài 3 cạnh tam giác là: a,b,c:")
a=int(input("Nhập a = "))
b=int(input("Nhập b = "))
c=int(input("Nhập c = "))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác là:", S)