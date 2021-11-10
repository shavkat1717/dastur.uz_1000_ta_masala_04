x=int(input("Milodiy yilni kiriting: "))
if (x%4==0 and x%100!=0):
    print("Ushbu yil kabisa yili va unda 366 kun bor.")
else:
    if x%400==0:
        print("Ushbu yil kabisa yili va unda 366 kun bor.")
    else:
        print("Ushbu yil kabisa yili emas va unda 365 kun bor.")       