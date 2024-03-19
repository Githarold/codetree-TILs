n = int(input())

a_list = list(map(int, input().split()))

answer = float('inf')
for i in range(n):
    dist_sum = 0
    for j in range(n):
        dist_sum += abs(i-j) * a_list[j]
    if dist_sum < answer:
        answer = dist_sum

print(answer)