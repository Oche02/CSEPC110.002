with open("courses.txt") as courses_file:
    for courses in courses_file:
        print(courses.strip())
