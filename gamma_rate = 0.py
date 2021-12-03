gamma_rate = 0
epsilon_rate = 0
num = [0] * 12
isTrue = True
while isTrue:
    input_a = input().split()
    print(len(input_a))
    for i in range(0, len(input_a)):
        word = input_a[i]
        for a in range(0, len(word)):
            if(word[a] == "1"):
                num[a] += 1
            else:
                num[a] -= 1
    print(num)
    for i in range(0, len(num)):
        if(num[i] > 0):
            num[i] = 1
        else:
            num[i] = 0
    print(num)
    isTrue = False
print(int(''.join(map(str, num)), 2))