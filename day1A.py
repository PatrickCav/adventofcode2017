infile = open('day1_input.txt', 'r')

data = infile.readline()

previousChar = ""

print(data)
print(previousChar)

count = 0

for char in data:
    if char == previousChar:
        count += int(char)
    previousChar = char

print(count)


