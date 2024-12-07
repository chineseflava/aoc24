import itertools

def get_combinations(numbers):
    operators = ["+", "*"]
    combinations = []

    for ops in itertools.product(operators, repeat=len(numbers) - 1):
        expression = numbers[0]
        for i in range(len(ops)):
            expression += ops[i] + numbers[i + 1]
        combinations.append(expression)

    return combinations

numbers = ["1", "2", "3"]
combinations = get_combinations(numbers)

for expression in combinations:
    print(expression)
    print(eval(expression))

a = ["1", "2", "3"]
get_combinations(a)