def rainfall():
    rainfall_data = []

    for month in range(1, 13):
        while True:
            try:
                rain = float(input(f"Enter the total rainfall for month {month}: "))
                rainfall_data.append(rain)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    total_rainfall = sum(rainfall_data)
    average_rainfall = total_rainfall / 12
    highest_rainfall = max(rainfall_data)
    lowest_rainfall = min(rainfall_data)
    highest_month = rainfall_data.index(highest_rainfall) + 1
    lowest_month = rainfall_data.index(lowest_rainfall) + 1

    print(f"Total rainfall for the year: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"Highest rainfall was in month {highest_month}: {highest_rainfall:.2f}")
    print(f"Lowest rainfall was in month {lowest_month}: {lowest_rainfall:.2f}")

rainfall()
