def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not triangle"
    results = []

    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]
    if a * a + b * b == c * c:
        results.append("Right triangle")
    elif a * a + b * b < c * c:
        results.append("Obtuse triangle")
    else:
        results.append("Acute triangle")
    if a == b or b == c or a == c:
            results.append("Isosceles triangle")
    if a == b == c:
            results.append("Equilateral triangle")
    return "\n".join(results)
a, b, c = map(int, input().split())
print(classify_triangle(a, b, c))
