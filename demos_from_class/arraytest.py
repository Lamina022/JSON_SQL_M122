myarrary = []
inputIsNotEmpty = True

while inputIsNotEmpty:
    uin = input()
    if uin == "":
        break
    else:
        myarrary.append(int(uin))
    
sum = 0
for number in myarrary:
    sum = sum + number

print(sum)