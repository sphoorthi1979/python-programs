
array = list(map(int, input("Enter numbers: ").split(",")))
target = int(input("Enter target: "))


result = []

for l in range(0, len(array)):
    for j in range(l + 1, len(array)):
        if array[l] + array[j] == target:
            result.append([l, j])

if len(result) == 0:
    print(-1)
else:
    print(result)
