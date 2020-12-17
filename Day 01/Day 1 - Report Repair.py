'''
Find two values from input.txt that sum to 2020 and then multiply those two numbers together.
'''

list = []

file = open("input.txt", "r")
text = file.readlines()
file.close()

# Creating list
def function (list):
    for values in text:
        list.append(int(values))

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

print(function(list), "\n")

