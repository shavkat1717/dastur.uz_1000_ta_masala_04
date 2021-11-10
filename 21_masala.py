x=int(input("Nuqtaning absissalar o'qidagi nuqtasini kiriting x => "))
y=int(input("Nuqtaning ordinatalar o'qidagi nuqtasini kiriting y => "))
if x==0 and y==0:
    print(0)
if x!=0 and y==0:
    print(1)
if x==0 and y!=0:
    print(2)
if x!=0 and y!=0:
    print(3)