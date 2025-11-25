m, h = map(float, input().split())
a="{:.4f}".format(m/h/h)
if m/h/h<18.5:
    print("Underweight")
elif 18.5<m/h/h<24:
    print("Normal")
elif 24<m/h/h:
    print(a)
    print("Overweight")

