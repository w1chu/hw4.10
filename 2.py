result = []

def divider(a, b):
    try:
        if a < b:
            return a / b
    except ValueError:
        return b
    except TypeError:
        return b
    try:
        if b > 100:
            return a / b
    except ZeroDivisionError:
        return b
    try:
        return a / b
    except:
        return a


data = {10: 2, 2: 5, "123": 4, 18: 0, "[]": 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)
    print(result)
