def main():
    headings, winners_by_year = create_list_from_csv("wimbledon.csv")
    champions = get_unique_values_from_list("Champion", headings, winners_by_year)
    champions_to_win_count = determine_number_of_wins(champions, winners_by_year)
    winning_countries = get_unique_values_from_list("Country", headings, winners_by_year)

    print_wimbledon_champions(champions, champions_to_win_count)
    print_winning_countries(winning_countries)


def print_winning_countries(winning_countries):
    print(f"\nThese {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(winning_countries)))


def print_wimbledon_champions(champions, champions_to_win_count):
    print("Wimbledon Champions:")
    for champion in champions:
        print(f"{champion}: {champions_to_win_count[champion]}")


def determine_number_of_wins(champions, winners_by_year):
    """Determines how many times each champion has won Wimbledon"""
    champions_to_win_count = {}
    for champion in champions:
        win_count = sum(winner[2] == champion for winner in winners_by_year)
        champions_to_win_count[champion] = win_count
    return champions_to_win_count


def get_unique_values_from_list(label, headings, winners_by_year):
    """Creates a set of unique values in a set"""
    index = headings.index(label)
    champions = {winner[index] for winner in winners_by_year}
    return champions


def create_list_from_csv(filename):
    """Creates a list of lists of each line in a csv file"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        headings = in_file.readline().strip().split(',')
        winners_by_year = [line.strip().split(",") for line in in_file.readlines()]
    return headings, winners_by_year


main()
