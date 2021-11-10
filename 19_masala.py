a=int(input("Istalgan 1-butun sonni kiriting A => "))
b=int(input("Istalgan 2-butun sonni kiriting B => "))
c=int(input("Istalgan 3-butun sonni kiriting С => "))
d=int(input("Istalgan 3-butun sonni kiriting D => "))
if a==b==c and a!=d:
    print("o'zaro teng bo'lmagan sonning tartib raqami: 4")
elif a==b==d and a!=c:
    print("o'zaro teng bo'lmagan sonning tartib raqami: 3")
elif a==c==d and a!=b:
    print("o'zaro teng bo'lmagan sonning tartib raqami: 2")
elif b==c==d and a!=c:
    print("o'zaro teng bo'lmagan sonning tartib raqami: 1")
elif a==b==c==d:
    print("Ushbu to'rtta son bir-biriga teng!")
else:
    print("Iltimos, masala shartiga muvofiq 3 ta sonni o'zaro teng qilib kiriting.")