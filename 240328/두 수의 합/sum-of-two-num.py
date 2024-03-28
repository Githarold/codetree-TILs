n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic = {}
for num in arr:
    dic[num] = dic.get(num, 0) + 1

count = 0
for num in arr:
    target = k - num
    # 현재 수를 딕셔너리에서 제거하거나 감소시켜 중복 계산 방지
    dic[num] -= 1
    if target in dic and dic[target] > 0:
        count += dic[target]
    # 해당 수가 더 이상 없다면, 딕셔너리에서 제거
    if dic[num] == 0:
        del dic[num]

print(count)