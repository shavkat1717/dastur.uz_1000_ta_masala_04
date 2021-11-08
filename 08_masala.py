a=int(input("Istalgan 1-butun sonni kiriting a => "))
b=int(input("Istalgan 2-butun sonni kiriting b => "))
if a-b>0:
    print(f"Mazkur sonlar taqqoslandi! Katta son {a}\nKichik son esa {b}")
if b-a>0:
    print(f"Mazkur sonlar taqqoslandi! Katta son {b}\nKichik son esa {a}")
if a-b==0:
    print("Ushbu sonlar teng!")