
with open('day4_input.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

valid = 0


def isValid(entrySet):
    ordered = list(map(lambda s: ''.join(sorted(s)), entrySet))
    return len(ordered) == len(set(ordered))


for row in content:
    entries = row.split()
    entrySet = set(entries)
    if len(entries) == len(entrySet) and isValid(entrySet):
        valid += 1
    
print("Valid: " + str(valid))
