def two_sum(numbers, target):
    for number in numbers:
        for ind, num in enumerate(numbers):
            if number + num == target and numbers.index(number) != ind:
                return (numbers.index(number), ind)

print(two_sum([2, 2, 3], 4))
