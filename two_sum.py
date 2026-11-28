array = [1, 2, 3, 10, 20]
target = 30

result = []

for l in range(0, len(array)):
    for j in range(l + 1, len(array)):
        if array[l] + array[j] == target:
            result.append([l, j])

if len(result) == 0:
    print(-1)
else:
    print(result)
