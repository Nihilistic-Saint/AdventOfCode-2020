import fileinput

data = []
file = open("input.txt", "r")
text = file.readlines()
for line in fileinput.input("input.txt"):
    data.append(line.strip())


def func1(list):
    print("---Part One---\n")
    x, y = 0, 0

    trees = 0
    while x + 1 < len(list):
        x += 1
        y += 3
        if list[x][y % len(list[x])] == "#":
            trees += 1
            #print(f"Ouch! You hit a tree.")
    return f"Ouch! I might have gotten a concussion from crashing into {trees} trees...\n"

def func2(list):
    attempts = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for slope in attempts:
        x, y = 0, 0
        trees = 0
        while x + 1 < len(list):
            x += slope[1]
            y += slope[0]
            if list[x][y % len(list[x])] == "#":
                trees += 1
        product *= trees
    return f"After {product} crashes later..."


print(func1(data))

print("---Part Two---\n")
print(f"{func2(data)}\nAlright, I definitely got a concussion after all those attempts.\n")
