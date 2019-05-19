

def run_with_switch():
    return 1

def run_without_switch():
    return 1

def total(l):
    """ Total all the elements in a list """
    total = 0
    for e in l:
        total += e
    return total


def main():
    with_switch = []
    without_switch = []

    for i in range(100):
        with_switch.append(run_with_switch())
        without_switch.append(run_without_switch())

    total_wins_with_switch = total(with_switch)
    win_percent_with_switch = (total_wins_with_switch / 100) * 100

    total_wins_without_switch = total(without_switch)
    win_percent_without_switch = (total_wins_without_switch / 100) * 100

    print()
    print(f"Win percent when consistantly sticking to first choice: {win_percent_without_switch}%")
    print(f"               Win percent when consistantly switching: {win_percent_with_switch}%")
    print()



if __name__ == "__main__":
    main()


