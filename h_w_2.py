
def count_and_sum_in_range(numbers: list[int], lower_bound: int, upper_bound: int, mode: str = 'normal') -> tuple[
    int, int]:
    assert isinstance(numbers, list) and all(isinstance(num, int) for num in numbers), "List must contain only integers"
    assert isinstance(lower_bound, int) and isinstance(upper_bound, int), "Bounds must be integers"
    # assert lower_bound <= upper_bound, "Lower bound must be less than or equal to upper bound"

    if lower_bound not in numbers or upper_bound not in numbers:
        print("Bounds must exist within the list")
        # raise (ValueError("Bounds must exist within the list"))

    if mode == 'normal':
        count = sum(lower_bound <= num <= upper_bound for num in numbers)
        total_sum = sum(num for num in numbers if lower_bound <= num <= upper_bound)

    elif mode in ['first_to_first', 'first_to_last']:
        start_idx = numbers.index(lower_bound)
        end_idx = (numbers.index(upper_bound, start_idx + 1) if mode == 'first_to_first'
                   else len(numbers) - 1 - numbers[::-1].index(upper_bound))

        count = end_idx - start_idx + 1
        total_sum = sum(numbers[start_idx:end_idx + 1])

    else:
        print("Invalid mode. Choose 'normal', 'first_to_first', or 'first_to_last'.")
        # raise (ValueError("Invalid mode. Choose 'normal', 'first_to_first', or 'first_to_last'."))
    return count, total_sum




numbers = [1, 2, 3, 4, 5, 6, 7, 8]
lower_bound = 1
upper_bound = 6

result = count_and_sum_in_range(numbers, lower_bound, upper_bound, mode='normal')
print(result)