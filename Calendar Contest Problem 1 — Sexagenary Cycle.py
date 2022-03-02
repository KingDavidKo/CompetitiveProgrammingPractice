stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
branches = [ "子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
N = int(input())
for i in range(N):
    temp = int(input()) - 4
    print(stems[temp%10] + branches[temp%12])