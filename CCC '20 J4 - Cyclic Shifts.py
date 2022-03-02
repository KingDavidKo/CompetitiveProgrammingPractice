def cyclicShift():
    text = input()
    string = input()
    for i in range(len(string)):
        if string in text:
            return 0
        else:
            temp = string[0]
            string = string[1:]
            string += temp
if cyclicShift() == 0:
    print("yes")
else:
    print("no")