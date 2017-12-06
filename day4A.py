
with open('day4_input.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

valid = 0

for row in content:
    entries = row.split()
    if len(entries) == len(set(entries)):
        valid += 1
    else:
        print(entries)
    
print("Valid: " + str(valid))
