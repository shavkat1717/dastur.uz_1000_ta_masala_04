x=int(input("Istalgan butun son kiriting: "))
if x>0 and x%2==0:
    print("Ushbu son musbat juft son.")
elif x<0 and x%2==0:
    print("Ushbu son manfiy juft son.")
elif x>0 and x%2!=0:
    print("Ushbu son musbat toq son.") 
elif x<0 and x%2!=0:
    print("Ushbu son manfiy toq son.")
else:
    print("Son nolga teng!")