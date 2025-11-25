from fractions import Fraction
a,b,c= map(int, input().split())
if a<b<c:
    v=Fraction(a,c)
    print(v)
elif b<a<c:
    v = Fraction(b,c)
    print(v)
elif c<a<b:
    v = Fraction(c,b)
    print(v)
elif a<c<b:
    v = Fraction(a, b)
    print(v)
elif b<c<a:
    v = Fraction(b,a)
    print(v)
elif c<b<a:
    v = Fraction(c,a)
    print(v)
