a=int(input("Istalgan 1-butun sonni kiriting A => "))
b=int(input("Istalgan 2-butun sonni kiriting B => "))
c=int(input("Istalgan 3-butun sonni kiriting С => "))
if a==b and a<c:
    print("o'zaro teng bo'lmagan sonning tartib raqami: 3")
if a==b and a>c:
    print("o'zaro teng bo'lmagan sonning tartib raqami: 3")
if a==c and a<b:
    print("o'zaro teng bo'lmagan sonning tartib raqami: 2")
if a==c and a>b:
    print("o'zaro teng bo'lmagan sonning tartib raqami: 2")
if c==b and a>c:
    print("o'zaro teng bo'lmagan sonning tartib raqami: 1")
if c==b and a<c:
    print("o'zaro teng bo'lmagan sonning tartib raqami: 1")