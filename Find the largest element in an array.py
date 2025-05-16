def two_sum(arr, target):
    for slower in range(0,len(arr)):
        for faster in range(slower,len(arr)):
            if arr[faster]+arr[slower] == target:
                return [faster,slower]


arr = [1, 2, 3, 4, 5, 6]
target = 10
print(two_sum(arr, target))  # Output: [3, 5] (since 4 + 6 = 10)
