def insertion_sort(array: list) -> list:
    if not isinstance(array, list):
        raise TypeError('Only list')
    try:
        for i in range(1, len(array)):
            temp = array[i]
            j = i - 1
            while (j >= 0 and temp < array[j]):
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = temp
    except Exception:
        raise ValueError('Elements must me int or float')
    return array

gss = insertion_sort([1,2.5,3,4.8,25,102,36])
print(gss)