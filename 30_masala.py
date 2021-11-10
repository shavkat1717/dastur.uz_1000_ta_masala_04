x=int(input("[1;999] oralig'ida istalgan butun son kiriting: "))
if 1<=x<=9:
    if x%2==0:
        print("Ushbu son bir xonalik juft son hisoblanadi.")
    else:
        print("Ushbu son bir xonalik toq son hisoblanadi.")
elif 10<=x<=99:
    if x%2==0:
        print("Ushbu son ikki xonalik juft son hisoblanadi.")
    else:
        print("Ushbu son ikki xonalik toq son hisoblanadi.")
elif 100<=x<=999:
    if x%2==0:
        print("Ushbu son uch xonalik juft son hisoblanadi.")
    else:
        print("Ushbu son uch xonalik toq son hisoblanadi.")
else:
    print("Masalaning shartiga e'tibor bering...[1;999] oraliqda son kiriting")