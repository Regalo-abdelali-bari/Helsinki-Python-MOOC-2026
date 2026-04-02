# Write your solution here
def remove_smallest(numbers: list):
    i = numbers[0]
    for num in numbers:
        if num < i :
            i = num
    numbers.remove(i)