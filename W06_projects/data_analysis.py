# i added the life expectancy gap between the highest and lowest countries for the selected year.

records = []

# open life-expectancy.csv file
with open("life-expectancy.csv") as life_expectancy_file:
    next(life_expectancy_file)  # skip the header

    # split data
    for line in life_expectancy_file:
        parts = line.split(",")

        # arrange spitted data into parts
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        records.append(
            {
                "country": country,
                "code": code,
                "year": year,
                "life_expectancy": life_expectancy,
            }
        )

# overall max and min across the whole dataset
overall_min = records[0]
overall_max = records[0]

for row in records:
    if row["life_expectancy"] < overall_min["life_expectancy"]:
        overall_min = row
    if row["life_expectancy"] > overall_max["life_expectancy"]:
        overall_max = row

print(
    f"The overall max life expectancy is: {overall_max['life_expectancy']:.3f} from {overall_max['country']} in {overall_max['year']}"
)
print(
    f"The overall min life expectancy is: {overall_min['life_expectancy']:.3f} from {overall_min['country']} in {overall_min['year']}"
)

# take user interest
year_interest = int(input("Enter the year of interest: "))

filtered_rows = [row for row in records if row["year"] == year_interest]

if not filtered_rows:
    print("Invalid Input")
    year_interest = int(input("Enter the year of interest: "))
else:
    # average for the selected year
    average_life = sum(row["life_expectancy"] for row in filtered_rows) / len(
        filtered_rows
    )

    # highest and lowest for the selected year
    year_max = max(filtered_rows, key=lambda row: row["life_expectancy"])
    year_min = min(filtered_rows, key=lambda row: row["life_expectancy"])

    print(f"\nFor the year {year_interest}:")
    print(f"The average life expectancy across all countries was {average_life:.2f}")
    # Show the average as a simple bar, with each # representing five years.
    print(f"Average: {'#' * int(average_life // 5)} (each # = 5 years)")
    print(
        f"The max life expectancy was in {year_max['country']} with {year_max['life_expectancy']:.2f}"
    )
    print(
        f"The min life expectancy was in {year_min['country']} with {year_min['life_expectancy']:.3f}"
    )
    print(
        f"The gap between the highest and lowest was "
        f"{year_max['life_expectancy'] - year_min['life_expectancy']:.2f} years."
    )
