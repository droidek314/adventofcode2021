count = 0
previous_input = 0
i = 0
while True:
    input_a = input().split()
    for i in range(0, len(input_a)):
        input_a[i] = int(input_a[i])
    for i in input_a:
        if previous_input != 0:
            if i - previous_input > 0:
                count+=1
                print("Count:" + str(count))
            else:
                previous_input = i
                continue
        else:
            previous_input = i
            continue
        previous_input = i
