a=int(input())
if a<= 150:
 c=0.4463*a
 round_c = round(c, 1)
 print(round_c)
elif 150<a<=400:
    c=0.4663*(a-150)+66.945
    round_c = round(c, 1)
    print(round_c)
elif a>400:
    c=0.5663*(a-400)+183.52
    round_c = round(c, 1)
    print(round_c)
