class TargetNotFoundException(Exception):
    pass


def binary_search(num, target):
    if not isinstance(num, list):
        raise TypeError('Only list')
    try:
        lef, rig = 0, len(num) - 1
        while lef <= rig:
            mid = (lef + rig) // 2
            if num[mid] == target:
                return mid
            if num[mid] < target:
                lef = mid + 1
            else:
                rig = mid - 1
    except Exception:
        raise TargetNotFoundException('Target not found in the list')
    return -1
    
gss = binary_search([1,2,3,4,5],3)
print(gss)