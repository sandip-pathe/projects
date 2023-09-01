def oddNumbers(x):
    odd_numbers = []
    for number in range(x+1):
        if number%2 != 0:
            odd_numbers.append(number)
    return odd_numbers

print(oddNumbers(9))