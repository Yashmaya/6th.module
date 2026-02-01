def sum_of_list(numbers):
    total=0
    for num in numbers:
        total += num
    return total
list_of_numbers = [9,7,5,1]
result = sum_of_list(list_of_numbers)
print(result)
