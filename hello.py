import math
a = float(input("输入a的值："))
b = float(input("输入b的值："))
c = float(input("输入c的值："))
if a==0:
    print("a不能为0")
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("△<0,无解！")
    elif delta == 0:
        x = -b/(2*a)
        print (x)
    else:
        p = -(b/(2*a))
        q = (math.sqrt(b*b-(4*a*c))/(2*a))
        x1 = p+q
        x2 = p-q
        print (x1)
        print(x2)
    
        