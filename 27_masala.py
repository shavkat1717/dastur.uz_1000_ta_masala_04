x=float(input("x ni kiriting: "))
import math
if x<0:
    print(0)
else:
    a=math.floor(x)
    if a%2==0:
        print(1)
    else:
        print(-1)  