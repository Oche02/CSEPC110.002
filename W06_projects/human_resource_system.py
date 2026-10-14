# open hr_system.txt file
with open("W06_projects/hr_system.txt") as hr_system_file:
    next(hr_system_file)  # skip the header line

    # read hr_system_file line by line
    for line in hr_system_file:

        # split each line into parts
        parts = line.split(" ")

        # assign parts to variables
        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])

        # calculate paycheck amount for the employee
        paycheck_amount = salary / 24  # assuming they are paid twice a month

        # calculate bonuses for engineers
        if job_title == "Engineer":
            bonus = 1000  # fixed bonus for engineers
            paycheck_amount += bonus

        # display the formatted output
        print(f"{name} ({id_number}), {job_title} - ${paycheck_amount:.2f}")
