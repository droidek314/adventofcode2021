depth = 0
horizontal = 0
aim = 0
isTrue = True
while isTrue == True:
    input_a = input().split()
    input_numbers = [s for s in input_a if s.isdigit()]
    input_words = [s for s in input_a if not s.isdigit()]
    print(input_words, input_numbers)
    for i in range(0, len(input_words)):
        if input_words[i] == "up":
            aim -= int(input_numbers[i])
        elif input_words[i] == "down":
            aim += int(input_numbers[i])
        elif input_words[i] == "forward":
            horizontal += int(input_numbers[i])
            depth += aim * int(input_numbers[i])
        else:
            continue
    isTrue = False
print("Horizontal: " + str(horizontal) + "\nDepth:" + str(depth) + "\nAim: " + str(aim))
    