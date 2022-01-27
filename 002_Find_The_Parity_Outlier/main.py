def find_outlier(integers):
    odd = [num for num in integers if num % 2 == 0]
    even = [num for num in integers if num % 2 == 1]
    return odd[0] if len(odd) == 1 else even[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))