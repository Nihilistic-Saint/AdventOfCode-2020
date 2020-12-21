'''
--- Part One ---
Find two values from input.txt that sum to 2020 and then multiply those two numbers together.
'''

data = []

file = open("input.txt", "r")
text = file.readlines()
file.close()
for values in text:
    data.append(int(values))

# Creating list
def function1 (list):
    # Finding the two values
    for z in range(len(list) - 1):
        for y in range(z + 1, len(list)):
            output = list[z] + list[y]
            if output == 2020:
                print("\n---Part One---")
                print(f"Index:\t{str(z)}\t\t{str(y)}")
                print(f"Values:\t{list[z]}\t + \t{list[y]} = {list[z] + list[y]}\n")
                return (f"Multiplying values:\n{list[z]} * {list[y]} = {list[z] * list[y]}")



'''
--- Part Two ---
Find three values from input.txt that sum to 2020 and then multiply those three numbers together.
'''

def function2(list):
    for z in range(len(list) - 2):
        for y in range(z + 1, len(list)):
            for x in range(y + 1, len(list)):
                output = list[z] + list[y] + list[x]
                if output == 2020:
                    print("\n---Part Two---")
                    print(f"Index:\t{str(z)}\t\t{str(y)}\t\t{str(x)}")
                    print(f"Values:\t{list[z]}\t + \t{list[y]} + \t{list[x]} = {list[z] + list[y] + list[x]}\n")
                    return (f"Multiplying values:\n{list[z]} * {list[y]} * {list[x]} = {list[z] * list[y] * list[x]}\n")


print(function1(data))
print(function2(data))
