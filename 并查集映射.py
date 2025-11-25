def find(x):
    if f[x] != x:
        f[x] = find(f[x])
    return f[x]

def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx != ry:
        f[ry] = rx

dict_a = {}
dict_b = {}
f = {}
i = 0
last_parent = None

while True:
    s = input().strip()
    if s == '$':
        break
    cmd = s[0]
    body = s[1:].strip()

    if cmd == '#':
        name = body
        if name not in dict_b:
            dict_a[i] = name
            dict_b[name] = i
            f[i] = i
            i += 1
        last_parent = name
    elif cmd == '+':
        child = body
        if child not in dict_b:
            dict_a[i] = child
            dict_b[child] = i
            f[i] = i
            i += 1
        if last_parent is not None:
            union(dict_b[last_parent], dict_b[child])

    elif cmd == '?':
        name = body
        if name in dict_b:
            root = find(dict_b[name])
            print(name, dict_a[root])
        else:
            print("no")