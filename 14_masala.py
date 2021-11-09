a=int(input("Istalgan 1-butun sonni kiriting A => "))
b=int(input("Istalgan 2-butun sonni kiriting B => "))
c=int(input("Istalgan 3-butun sonni kiriting С => "))
if a==b==c:
    print("Ushbu sonlarning barchasi bir-biriga teng.") 
if a==b and b<c:
    print(f"Ushbu sonlarning eng kichigi {a}, eng kattasi esa {c}.")
if a==b and b>c:
    print(f"Ushbu sonlarning eng kichigi {c}, eng kattasi esa {a}.")
if a==c and b>c:
    print(f"Ushbu sonlarning eng kichigi {c}, eng kattasi esa {b}.")
if a==c and b<c:
    print(f"Ushbu sonlarning eng kichigi {b}, eng kattasi esa {c}.")
if b==c and a>b:
    print(f"Ushbu sonlarning eng kichigi {b}, eng kattasi esa {a}.")
if b==c and a<b:
    print(f"Ushbu sonlarning eng kichigi {a}, eng kattasi esa {c}.")
if a<b and b<c:
    print(f"Ushbu sonlarning eng kichigi {a}, eng kattasi esa {c}.")
if c<b and b<a:
    print(f"Ushbu sonlarning eng kichigi {c}, eng kattasi esa {a}.")
if b<a and a<c:
    print(f"Ushbu sonlarning eng kichigi {b}, eng kattasi esa {c}.")
if c<a and a<b:
    print(f"Ushbu sonlarning eng kichigi {c}, eng kattasi esa {b}.")
if a<c and c<b:
    print(f"Ushbu sonlarning eng kichigi {a}, eng kattasi esa {b}.")
if b<c and c<a:
    print(f"Ushbu sonlarning eng kichigi {b}, eng kattasi esa {a}.")