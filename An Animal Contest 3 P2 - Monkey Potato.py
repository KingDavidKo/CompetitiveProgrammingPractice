K, D = map(int, input().split())
digits = list(map(int, input().split()))
num = ''
if 0 in digits:
    digits.pop(digits.index(0))
    if len(digits) == 0:
        num = '-1'
    elif K > 1:
        minDigit = str(min(digits))
        num = minDigit
        for i in range(K-2):
            num += "0"
        num += minDigit
    else:
        num = str(min(digits))
else:
    minDigit = str(min(digits))
    for i in range(K):
        num += minDigit
print(num)