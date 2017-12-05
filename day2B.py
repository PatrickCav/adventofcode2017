
with open('day2_input.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

checkSum = 0


def divible(first, second):
    if(first > second):
        return first % second == 0
    else:
        return second % first == 0


def rowDivisor(entries):
    rowCount = len(entries)
    for i in range(0, rowCount):
        for j in range(i + 1, rowCount):
            print("i = " + str(i) + " j = " + str(j))
            first = entries[i]
            second = entries[j]
            if(divible(first, second)):
                if(first > second):
                    return first/second
                else:
                    return second/first


for row in content:
    checkSum += rowDivisor(map(int, row.split()))

                
print(checkSum)
