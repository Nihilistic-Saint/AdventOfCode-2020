'''
--- Part One ---
Each line has a password policy and then the password.
The policy indicates the minimum and maximum number of times a given letter must appear for the password to be valid.
'''

import csv

def part1():
    with open('input.csv') as data:
        reader = csv.reader(data, delimiter=' ')
        lines = 0
        correct = 0
        incorrect = 0

        for line in reader:
            demand, letter, password = line[0], line[1][0], line[2]
            print(line)

            i = demand.index('-')
            min = int(demand[:i])
            max = int(demand[i+1:])
            #print(min, max, demand)
            count = 0
            for x in line[2]:
                #print(x)
                if x == letter:
                    count += 1
            if count >= min and count <= max:
                print(f"Password is correct.\n")
                #print(count)
                correct += 1
            else:
                print("Password is INCORRECT.\n")
                #print(count)
                incorrect += 1
            lines += 1

        print(f"You had {correct}/{lines} passwords that were correct!")
        return f"The rest {incorrect} were incorrect!\n"


'''
--- Part Two ---
Now the policy indicates a position a given letter has to be in.
One correct letter is enough for a valid password.
'''
def part2():
    with open('input.csv') as data:
        reader = csv.reader(data, delimiter=' ')
        for line in reader:
            demand, letter, password = line[0], line[1][0], line[2]
            print(line)

            i = demand.index('-')
            x = int(demand[:i])
            y = int(demand[i + 1:])
            one = int(demand[x])
            two = int(demand[y])
            print(x, y, demand)
            print(one, two)
            return ''

#print(part1())
print(part2())


