
with open('day6_input.txt') as f:
    content = f.readlines()

instructions = map(int, [x.strip() for x in content])

steps = 0
position = 0
end = len(instructions)

while position < end:
    offset = instructions[position]
    if offset > 2:
        instructions[position] -= 1
    else:
        instructions[position] += 1
    position += offset
    steps += 1
    
print("Steps: " + str(steps))
