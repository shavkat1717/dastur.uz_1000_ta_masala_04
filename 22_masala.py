x=int(input("Nuqtaning absissalar o'qidagi nuqtasini kiriting x => "))
y=int(input("Nuqtaning ordinatalar o'qidagi nuqtasini kiriting y => "))
if x>0 and y>0:
    print("Mazkur nuqta I chorakda joylashgan.")
if x<0 and y>0:
    print("Mazkur nuqta II chorakda joylashgan.")
if x<0 and y<0:
    print("Mazkur nuqta III chorakda joylashgan.")
if x>0 and y<0:
    print("Mazkur nuqta IV chorakda joylashgan.")
if x!=0 and y==0:
    print("Mazkur nuqta OX o'qida joylashgan.")
if x==0 and y!=0:
    print("Mazkur nuqta OY o'qida joylashgan.")
if x==0 and y==0:
    print("Mazkur nuqta OX va OY o'qlari keshismasida joylashgan.")