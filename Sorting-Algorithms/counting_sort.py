array = [2, 3, 2, 1, 5, 4, 3, 1, 2, 7]


size = max(array)
count = [0] * (size + 1)

output = [0] * (size + 1)

# Store the count of each elements in count array
for i in range(0, len(array)):
    count[array[i]] += 1

print('count = ', count)
# Store the cummulative count
for i in range(1, size+1):
    count[i] += count[i - 1]

print(count)

i = size - 1
while i >= 0:
    output[count[array[i]] - 1] = array[i]
    count[array[i]] -= 1
    i -= 1

print(output)