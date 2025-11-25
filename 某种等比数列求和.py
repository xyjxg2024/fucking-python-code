def sha_bi(s):
     b = 1
     c = 2
     x = 2
     while x < s:
        c*= 0.98
        x += c
        b += 1
     return b
s=float(input())
print(sha_bi(s))
