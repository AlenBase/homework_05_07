def bubble_sort(array: list) -> list:
    if not isinstance(array, list):
        raise TypeError('Only list')
    try:
        for i in range(len(array)-1):
            for j in range((len(array)-1)- i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j+1], array[j]
    except Exception:
        raise ValueError('Elements must me int or float')
    return array


gss = bubble_sort([4,1,18,5,23,87,56])
print(gss)