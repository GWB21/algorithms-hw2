def make_balance(arr):
    if not arr:
        return []

    result = []
    work_list = [(0, len(arr) - 1)]

    while work_list:
        start, end = work_list.pop(0)
        if start > end:
            continue

        mid = (start + end) // 2
        result.append(arr[mid])
        work_list.append((start, mid - 1))
        work_list.append((mid + 1, end))

    return result

def make_balance_recursive(arr):
    def helper(start, end, depth, levels):
        if start > end:
            return

        mid = (start + end) // 2
        if depth < len(levels):
            levels[depth].append(arr[mid])
        else:
            levels.append([arr[mid]])

        helper(start, mid - 1, depth + 1, levels)
        helper(mid + 1, end, depth + 1, levels)

    levels = []
    helper(0, len(arr) - 1, 0, levels)

    result = []
    for level in levels:
        result.extend(level)
    return result


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(make_balance(arr))
print(make_balance_recursive(arr))
