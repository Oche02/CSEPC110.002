# open the file and read the contents
with open("web_traffic.csv") as web_traffic_file:
    total_time = 0

    # read each line in the file
    for line in web_traffic_file:

        # split lines into parts
        parts = line.split(",")

        # assign parts to variables
        page = parts[0]
        time = parts[1]
        referer = parts[2]

        total_time += float(time)

        # display output
        print(f"Page: {page} Referer by {referer} spent {time} seconds")
    print(f"Total time: {total_time}")
