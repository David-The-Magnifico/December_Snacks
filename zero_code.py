def zero_code(numbers):
    if len(numbers) >= 1:
        numbers[0] = 0
    if len(numbers) >= 2:
        numbers[-1] = 0
    return numbers
