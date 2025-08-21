def flatten(lst: list) -> list:
    result = []
    for element in lst:
        if isinstance(element, list):
            resolved = flatten(element)
            result.extend(resolved)
        else:
            result.append(element)
    return result


print(flatten([1, [2, [3, 4], 5]]))
