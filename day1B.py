infile = open('day1_input.txt', 'r')

data = infile.readline()
firstHalf = data[:len(data)/2]
secondHalf = data[len(data)/2:]

print("First half: " + str(len(firstHalf)) + " Second half: " + str(len(secondHalf)))

count = 0

for i in range(0, len(firstHalf)):
    char = firstHalf[i]
    if char == secondHalf[i]:
        count += int(char)

print(2 * count)


