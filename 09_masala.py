A=float(input("Istalgan 1-butun sonni kiriting A => "))
B=float(input("Istalgan 2-butun sonni kiriting B => "))
if A-B>0:
    print(f"Kichik son A={B}ga, katta son esa B={A} ga o'zlashtirildi")
if A-B<0:
    print(f"Kichik son A={A}ga, katta son esa B={B} ga o'zlashtirildi")
if A-B==0:
    print("Ushbu sonlar teng!")