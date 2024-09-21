size = int(input())
for line in range(size):
    numbers = [str(line + 1) for _ in range(size - line)]
    print(' ' .join(numbers))