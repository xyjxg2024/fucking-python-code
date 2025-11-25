from fractions import Fraction
expr = input()
terms = expr.replace('+', ' +').replace('-', ' -').split()
result = Fraction(0, 1)
for term in terms:
    if '/' in term:
        num, den = map(int, term.split('/'))
        result += Fraction(num, den)
    else:
        result += Fraction(int(term), 1)
print(result)
#输入2/1+1/3-1/4
#输出25/12