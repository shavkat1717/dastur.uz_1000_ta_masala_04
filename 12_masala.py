a=int(input("Istalgan 1-butun sonni kiriting A => "))
b=int(input("Istalgan 2-butun sonni kiriting B => "))
c=int(input("Istalgan 3-butun sonni kiriting С => "))
if a>b:
    if b>c:
        print(f"Eng kichik son {c}.")
    else:
        print(f"Eng kichik son {b}.")
if a<b:
        if a>c:
            print(f"Eng kichik son {c}.")
        if a<c:
            print(f"Eng kichik son {a}.")
        if a==c:
            print(f"Eng kichik son {c}.")
if a==b:
    if a>c:
        print(f"Eng kichik son {c}")
    if a<c:
        print(f"Eng kichik son {a}")
    if a==c:
        print("Ushbu sonlar bir-biriga teng.")