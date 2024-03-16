array = [30, 20, 22, 15, 58, 42, 31]

def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

    return array


# print(insertion_sort(array))    
      
        






    