def add_comma_after_fourth(numbers):
    # Convert the list of numbers to a string and group every four numbers with a comma
    result = ""
    for i in range(len(numbers)):
        result += str(numbers[i])
        # After the fourth number, add a comma
        if (i + 1) % 4 == 0 and i != len(numbers) - 1:
            result += ", "
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
formatted_string = add_comma_after_fourth(numbers)
print(formatted_string)