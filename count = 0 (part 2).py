count = 0
i = 0
inputs = []
while True:
    while True:
        input_a = input()
        if input_a != '':
            inputs.append(int(input_a))
        else:
            break
    try:    
        for i in range(0, len(inputs)):
            a_sum = inputs[i] + inputs[i+1] + inputs[i+2]
            b_sum = inputs[i+1] + inputs[i+2] + inputs[i+3]
            if a_sum < b_sum:
                count+=1
                print("Count: " + str(count))
            else:
                continue
    except IndexError:
        continue

