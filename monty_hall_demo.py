import random as rand

def run_with_switch():
    return 1

def run_without_switch():
    """ Simulates one contestant playing Monty hall problem 
        without switching their choice after goat is revealed """

    # Setup doors, put one "win" behind a random door
    doors = [False, False, False]
    doors[rand.randrange(3)] = True

    # Select choice randomly
    choice = rand.randrange(3)

    # Return 1 if choice has "win" behind is, false otherwise
    if doors[choice]:
        return 1
    else:
        return 0



def total(l):
    """ Total all the elements in a list """
    total = 0
    for e in l:
        total += e
    return total


def main():
    with_switch = []
    without_switch = []

    for i in range(10000):
        with_switch.append(run_with_switch())
        without_switch.append(run_without_switch())

    total_wins_with_switch = total(with_switch)
    win_percent_with_switch = (total_wins_with_switch / len(with_switch)) * 100

    total_wins_without_switch = total(without_switch)
    win_percent_without_switch = (total_wins_without_switch / len(without_switch)) * 100

    print()
    print(f"Win percent when consistently sticking to first choice: {win_percent_without_switch}%")
    print(f"               Win percent when consistently switching: {win_percent_with_switch}%")
    print()



if __name__ == "__main__":
    main()


