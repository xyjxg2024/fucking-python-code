def swim_steps(s):
    step = 1
    distance = 2
    total_distance = 2
    while total_distance < s:
        distance *= 0.98
        total_distance += distance
        step += 1
    return step

s = float(input())

print(swim_steps(s))