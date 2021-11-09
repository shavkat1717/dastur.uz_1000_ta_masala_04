a=int(input("Istalgan 1-butun sonni kiriting A => "))
b=int(input("Istalgan 2-butun sonni kiriting B => "))
c=int(input("Istalgan 3-butun sonni kiriting С => "))
x=a+b; y=a+c; z=b+c
if x>=y:
    if x>z:
        print(f"{a} va {b} sonlar juftligining yig'indisi eng katta!")
    if x<z:
        print(f"{b} va {c} sonlar juftligining yig'indisi eng katta!")
    if x==z:
        print(f"Bu holatda {a} + {b} = {b} + {c} [yig'indilar teng]")
if x<y:
    if y>z:
        print(f"{a} va {c} sonlar juftligining yig'indisi eng katta!")
    if y<z:
        print(f"{b} va {c} sonlar juftligining yig'indisi eng katta!")
    if y==z:
        print(f"Bu holatda {a} + {c} = {b} + {c} [yig'indilar teng]")
if x==y:
    if x==z:
        print("Bunda uchchala sonlar juftligi yig'indilari teng']")    