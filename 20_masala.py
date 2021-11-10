a=int(input("Sonlar o'qidagi 1-nuqtani kiriting A => "))
b=int(input("Sonlar o'qidagi 2-nuqtani kiriting B => "))
c=int(input("Sonlar o'qidagi 3-nuqtani kiriting С => "))
import math
if a<b<c:
    print(f"A nuqtaga eng yaqin nuqta {b} va ular orasidagi masofa {math.fabs(b-a)} ga teng.")
if a<c<b:
    print(f"A nuqtaga eng yaqin nuqta {c} va ular orasidagi masofa {math.fabs(c-a)} ga teng.")
if c<b<a:
    print(f"A nuqtaga eng yaqin nuqta {b} va ular orasidagi masofa {math.fabs(a-b)} ga teng.")
if b<c<a:
    print(f"A nuqtaga eng yaqin nuqta {c} va ular orasidagi masofa {math.fabs(a-c)} ga teng.")
if b<a<c:
    if math.fabs(a-b)>math.fabs(c-a):
        print(f"A nuqtaga eng yaqin nuqta {c} va ular orasidagi masofa {math.fabs(c-a)} ga teng.")
    if math.fabs(a-b)<math.fabs(c-a):
        print(f"A nuqtaga eng yaqin nuqta {b} va ular orasidagi masofa {math.fabs(a-b)} ga teng.")
    if math.fabs(a-b)==math.fabs(c-a):
        print(f"A nuqtadan ikkala nuqtagacha bo'lgan masofalar teng va {a-b} ga teng.")
if c<a<b:
    if math.fabs(a-c)>math.fabs(b-a):
        print(f"A nuqtaga eng yaqin nuqta {b} va ular orasidagi masofa {math.fabs(b-a)} ga teng.")
    if math.fabs(a-c)<math.fabs(b-a):
        print(f"A nuqtaga eng yaqin nuqta {c} va ular orasidagi masofa {math.fabs(a-c)} ga teng.")
    if math.fabs(a-c)==math.fabs(b-a):
        print(f"A nuqtadan ikkala nuqtagacha bo'lgan masofalar teng va {math.fabs(b-a)} ga teng.")