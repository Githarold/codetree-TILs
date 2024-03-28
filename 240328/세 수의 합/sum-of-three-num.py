n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))

count = 0

for i in range(n - 2):
    left, right = i + 1, n - 1
    while left < right:
        current_sum = arr[i] + arr[left] + arr[right]
        if current_sum == k:
            count += 1
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                count += 1
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                count += 1
                right -= 1
        elif current_sum < k:
            left += 1
        else:
            right -= 1

print(count)