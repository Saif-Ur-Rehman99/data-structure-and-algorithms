from insertion_sort import insertion_sort

array = [0.79, 0.13, 0.64, 0.39, 0.20, 0.89, 0.35, 0.42, 0.06, 0.94]


def bucket_sort(array):
    # create empty buckets [0 to 9]
    bucket = []
    for i in range(len(array)):
        bucket.append([])

    # make each floating point value an index and append the value
    for j in array:
        index = int(10 * j)
        bucket[index].append(j)

    # sort the elements of each bucket
    sorted_array = []
    for k in range(len(bucket)):
        each_bucket = insertion_sort(bucket[k])
        for value in each_bucket:
            sorted_array.append(value)
    
    return sorted_array



print(bucket_sort(array))    
