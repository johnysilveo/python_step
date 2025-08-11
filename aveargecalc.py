def calculate_average(numbers):
    if not numbers:
        return None
    result = sum(numbers)
    avg = result / len(numbers)
    return avg
