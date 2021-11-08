a=int(input("Istalgan 1-butun sonni kiriting a => "))
b=int(input("Istalgan 2-butun sonni kiriting b => "))
if a-b>0:
    print(f"{a} soni {b} sonidan katta: Ya'ni {a} > {b}")
if a-b<0:
    print(f"{a} soni {b} sonidan kichik: Ya'ni {a} < {b}")
if a-b==0:
    print("Ushbu sonlar teng!")