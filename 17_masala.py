a=int(input("Istalgan 1-butun sonni kiriting A => "))
b=int(input("Istalgan 2-butun sonni kiriting B => "))
c=int(input("Istalgan 3-butun sonni kiriting С => "))
if a<b<c:
    print(f"Sonlar o'sish tartibida berildi:\n {2*a}, {2*b}, {2*c} ")
elif a>b>c:
    print(f"Sonlar kamayish tartibida berildi:\n {2*a}, {2*b}, {2*c} ")
else:
    print(f"Sonlar o'sish yoki kamayish tatibida berilmadi:\n{-1*a}, {-1*b}, {-1*c} ")