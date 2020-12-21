'''
Find two values from input.txt that sum to 2020 and then multiply those two numbers together.
'''

data = []

file = open("input.txt", "r")
text = file.readlines()
file.close()
for values in text:
    data.append(int(values))

# Creating list
def function (list):

    # Finding the two values
    x = 0
    for z in range(len(list)):
        for y in range(len(list)):
            output = list[x] + list[y]
            if output == 2020:
                print(f"Index:{str(x)} \nIndex:{str(y)} \nEquals: 2020")
                print(f"{list[x]} + {list[y]} = 2020\n")

                # Multiplying values
                print(f"{list[x]} * {list[y]} = {list[x] * list[y]}")
        x += 1

def part2(list):
    x = 1
    for z in range(len(list)):
        for y in range(len(list)):
            output = list[x] + list[y]
            print(f"{str(x)} <-> {str(y)} -> {str(z)}\n")

            if output == 2020:
                print(f"Index:{str(x)} \nIndex:{str(y)} \nEquals: 2020")
                print(f"{list[x]} + {list[y]} = 2020\n")

                # Multiplying values
                print(f"{list[x]} * {list[y]} = {list[x] * list[y]}")
        x += 1


#print(function(data), "\n")

print(part2(data))

