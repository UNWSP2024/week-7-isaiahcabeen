def main():
    all_entered_values = []

    while True:
        year = input("Enter the year (enter 'done' when finish): ")
        if year.lower() == 'done':
            break

        state = input("Enter the name of the state: ")

        while True:
            try:
                population = int(input("Enter the population: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number for the population.")

        all_entered_values.append([int(year), state, population])

    year_to_sum = int(input("Enter a year to get total population: "))
    total_population = sum_population_for_year(all_entered_values, year_to_sum)

    print(f"Total population for the year {year_to_sum}: {total_population}")
def sum_population_for_year(all_entered_values, year_to_sum):
    total = sum(state[2] for state in all_entered_values if state[0] == year_to_sum)
    return total

if __name__ == '__main__':
    main()
