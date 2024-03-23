n = int(input())
score = list(map(int, input().split()))
newscore = []
max = max(score)
total = 0

for i in score:
    newscore.append(i/max)

for i in newscore:
    total = total + i

print(total*100/n)