key=int(input())
stxt=input()
dtxt=""
for s in stxt:
    sn=ord(s)
    if 'a' <= s <= "z":
        dn = (sn - 97 + key) % 26 + 97
    elif 'A' <= s <= "Z":
        dn = (sn - 65 + key) % 26 + 65
    else:
        dn = sn
    dtxt =dtxt + chr(dn)
print(dtxt)