n = int(input())
arr = list(map(int, input().split()))

sorted_arr = []
for i in range(1, n+1):
    sorted_arr.append(arr[i-1])
    if i % 2:
        sorted_arr.sort()
        print(sorted_arr[i//2], end = ' ')