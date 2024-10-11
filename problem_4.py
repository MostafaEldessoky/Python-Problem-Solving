


def rotateLeft(d:int, arr:list[int]):
    for _ in range(d):
        h = arr.pop(0)
        arr.append(h)
    return arr


print(rotateLeft(10, [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]))