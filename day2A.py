
with open('day2_input.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

checkSum = 0

for row in content:
    entries = map(int, row.split())
    largest = max(entries)
    # print(largest)
    smallest = min(entries)
    checkSum += (largest - smallest)

print(checkSum)


