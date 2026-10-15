# Store each country's life expectancy record from the CSV file.
records = []

# Open the CSV file and skip its column headings.
with open("life-expectancy.csv") as life_expectancy_file:
    next(life_expectancy_file)

    # Read each row, convert the year and life expectancy to numbers, and save it.
    for line in life_expectancy_file:
        parts = line.strip().split(",")
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

# Find the records with the lowest and highest life expectancy in the full dataset.
overall_min = records[0]
overall_max = records[0]

for row in records:
    if row["life_expectancy"] < overall_min["life_expectancy"]:
        overall_min = row
    if row["life_expectancy"] > overall_max["life_expectancy"]:
        overall_max = row

# Display the overall minimum and maximum values with their country and year.
print(
    f"The overall max life expectancy is: {overall_max['life_expectancy']:.3f} from {overall_max['country']} in {overall_max['year']}"
)
print(
    f"The overall min life expectancy is: {overall_min['life_expectancy']:.3f} from {overall_min['country']} in {overall_min['year']}"
)

# Make a list of the years that can be selected from the dataset.
available_years = {row["year"] for row in records}

# Ask for a year and keep asking until the user enters a year in the data.
while True:
    try:
        year_interest = int(input("Enter the year of interest: "))
    except ValueError:
        print("Please enter a year as a number.")
        continue

    if year_interest in available_years:
        break

    print("That year is not in the dataset. Please try again.")

# Collect all country records that match the selected year.
filtered_rows = [row for row in records if row["year"] == year_interest]

# Calculate the average life expectancy and find the year's minimum and maximum.
average_life = sum(row["life_expectancy"] for row in filtered_rows) / len(filtered_rows)
year_max = max(filtered_rows, key=lambda row: row["life_expectancy"])
year_min = min(filtered_rows, key=lambda row: row["life_expectancy"])

# Display the selected year's average, highest, and lowest life expectancy.
print(f"\nFor the year {year_interest}:")
print(f"The average life expectancy across all countries was {average_life:.2f}")
print(
    f"The max life expectancy was in {year_max['country']} with {year_max['life_expectancy']:.2f}"
)
print(
    f"The min life expectancy was in {year_min['country']} with {year_min['life_expectancy']:.3f}"
)

# Ask which country's life expectancy the user wants to explore over time.
country_interest = input(
    "\nEnter a country to see its life expectancy through the years: "
).strip()

# Match the entered country without requiring the same capitalization.
country_rows = [
    row for row in records if row["country"].casefold() == country_interest.casefold()
]

# If the country exists, order its records by year to create a timeline.
if country_rows:
    country_rows.sort(key=lambda row: row["year"])

    # Display the country's life expectancy for every year available in the data.
    print(f"\nLife expectancy timeline for {country_rows[0]['country']}:")
    for row in country_rows:
        print(f"{row['year']}: {row['life_expectancy']:.2f} years")

    # Compare the first and last available values to show the overall change.
    first_record = country_rows[0]
    last_record = country_rows[-1]
    change = last_record["life_expectancy"] - first_record["life_expectancy"]
    print(
        f"Change from {first_record['year']} to {last_record['year']}: "
        f"{change:+.2f} years"
    )
else:
    # Explain when the requested country does not appear in the dataset.
    print(f"No records were found for '{country_interest}'. Check the spelling.")
