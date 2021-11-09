a=int(input("Istalgan 1-butun sonni kiriting A => "))
b=int(input("Istalgan 2-butun sonni kiriting B => "))
c=int(input("Istalgan 3-butun sonni kiriting С => "))
if a>b:
    if b>c:
        print(f"O'rtacha son {b}.")
    if b<c:
        if a>c:
            print(f"O'rtacha son {b}.")
        if a<c:
            print(f"O'rtacha son {b}.")
        if a==c:
            print("Afsuski sonlar teng bo'lib qoldi, o'rtacha sonni aniqmas!")
    if b==c:
        print("Afsuski sonlar teng bo'lib qoldi, o'rtacha sonni aniqmas!")        
if a<b:
    if b>c:
        if a>c:
            print(f"O'rtacha son {a}.")
        if a<c:
            print(f"O'rtacha son {a}.")
        if a==c:
            print("Afsuski sonlar teng bo'lib qoldi, o'rtacha sonni aniqmas!")
    if b<c:
        print(f"O'rtacha son {b}")
    if b==c:
        print("Afsuski sonlar teng bo'lib qoldi, o'rtacha sonni aniqmas!")
if a==b:
    if a>c:
        print("Afsuski sonlar teng bo'lib qoldi, o'rtacha sonni aniqmas!")
    if a<c:
        print("Afsuski sonlar teng bo'lib qoldi, o'rtacha sonni aniqmas!")
    if a==c:
        print("Ushbu sonlar bir-biriga teng.")