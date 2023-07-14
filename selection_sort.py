def selection_sort(array: list) -> list :
    if not isinstance(array, list):
        raise TypeError('Only list')
    try:
        for i in range(len(array)):
            min = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min]:
                    min = j
            array[i], array[min] = array[min], array[i]
    except Exception:
        raise ValueError('Elements must me int or float')
    return array



gss = [22,11,64,85,76,103]
sort = selection_sort(gss)
print(sort)