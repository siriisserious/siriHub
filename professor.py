'''
WORK IN PROGRESS, can play but can't submit yet
'''

import random

problems = []

def main():
    level = get_level()
    generate_integer(level)

    try:
        score = 0
        for problem in problems:
            wrong_counter = 0
            while True:
                answer = input(f"{problem} = ")
                x, y = problem.strip().split("+")

                if int(x) + int(y) == int(answer):
                    score += 1
                    break
                else:
                    if wrong_counter < 3:
                        print("EEE")
                        wrong_counter += 1
                        continue
                    else:
                        ans = int(x) + int(y)
                        print(f"{problem} = {ans}")
                        break
    except ValueError:

        print(f"Score: {score}")


def get_level():
    while True:
        try:
            while True:
                n = int(input("Level: "))

                if 1 <= n <= 3:
                    return n
                else:
                    continue
        except ValueError:
                continue

def generate_integer(level):
    if level == 1:
        for i, j in zip(range(10), range(10)):
            i = random.randrange(0, 9)
            j = random.randrange(0, 9)
            problem = f"{i} + {j} "
            problems.append(problem)

    if level == 2:
        for i, j in zip(range(10), range(10)):
            i = random.randrange(10, 99)
            j = random.randrange(10, 99)
            problem = f"{i} + {j} "
            problems.append(problem)

    if level == 3:
        for i, j in zip(range(10), range(10)):
            i = random.randrange(100, 999)
            j = random.randrange(100, 999)
            problem = f"{i} + {j} "
            problems.append(problem)

if __name__ == "__main__":
    main()
