'''
--- Part One ---
Each line has a password policy and then the password.
The policy indicates the minimum and maximum number of times a given letter must appear for the password to be valid.
'''

import csv

def part1():
    print("--- Part One ---")
    with open('input.csv') as data:
        reader = csv.reader(data, delimiter=' ')
        lines = 0
        correct = 0
        incorrect = 0

        for line in reader:
            demand, letter, password = line[0], line[1][0], line[2]

            i = demand.index('-')
            min = int(demand[:i])
            max = int(demand[i+1:])
            count = 0
            for x in line[2]:
                #print(x)
                if x == letter:
                    count += 1
            if count >= min and count <= max:
                correct += 1
            else:
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
    print("--- Part Two ---")
    with open('input.csv') as data:
        reader = csv.reader(data, delimiter=' ')
        count = 0
        incorrect = 0
        for line in reader:
            demand, letter, password = line[0], line[1][0], line[2]

            i = demand.index('-')
            x = int(demand[:i])
            y = int(demand[i + 1:])

            one = password[x - 1] == letter
            two = password[y - 1] == letter

            if (one and not two) or (two and not one):
                count += 1
            elif letter == one and two:
               incorrect += 1
            else:
                incorrect += 1
        print(f"Total of valid passwords -> {count}")
        return (f"Total of invalid passwords -> {incorrect}")

print(part1())
print(part2())


