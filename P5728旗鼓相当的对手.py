def is_competitors(score1, score2):
    for i in range(3):
        if abs(score1[i] - score2[i]) > 5:
            return False
    if abs(sum(score1) - sum(score2)) > 10:
        return False
    return True
def count_competitors(N, scores):
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if is_competitors(scores[i], scores[j]):
                count += 1
    return count

N = int(input())
scores = []
for _ in range(N):
    scores.append(list(map(int, input().split())))

result = count_competitors(N, scores)
print(result)
