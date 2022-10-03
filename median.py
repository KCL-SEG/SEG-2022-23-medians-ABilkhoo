"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        numbers.sort()
        median = 0

        if len(numbers) % 2 == 0:
            upperIndex = len(numbers) // 2
            median = (numbers[upperIndex] + numbers[upperIndex-1]) / 2
        else:
            median = numbers[len(numbers) // 2]
        print(median)

