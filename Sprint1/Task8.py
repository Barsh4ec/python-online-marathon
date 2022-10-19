def studying_hours(a):
    count = 0
    res = []
    for i in range(len(a) - 1):
        if a[i] <= a[i + 1]:
            count += 1
        else:
            count = 0
        res.append(count)
    return max(res) + 1


if __name__ == '__main__':
    a = [2, 2, 9]
    print(studying_hours(a))