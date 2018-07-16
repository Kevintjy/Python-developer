"""
This file is used to edit the result.txt

NOTICE:
file.read() means we get the whole file as a str
file.readlines() means we get the file as a list, each line is a str element in the list
"""
file = 'result.txt'


def course_number() -> int:
    """
    return how many course you have
    """
    with open(file, 'r') as f:
        f = f.read()
        return f.count('$')


def get_all_course() -> list:
    """
    return the courses student has in a list,
    each course is a str element in the list
    """
    temp = []
    with open(file, 'r') as f:
        f = f.read()
        f = f.split('$')[1:]
        for i in f:
            temp.append(i[:6])
    return temp


def transfer_gpa(percentage: int) -> str:
    """
    transfer the int mark to the str gpa like 'A', 'B-'
    """
    if 0 <= percentage <= 49:
        return "F 0.0"
    if 50 <= percentage <= 52:
        return "D- 0.7"
    if 53 <= percentage <= 56:
        return "D 1.0"
    if 57 <= percentage <= 59:
        return "D+ 1.3"
    if 60 <= percentage <= 62:
        return "C- 1.7"
    if 63 <= percentage <= 66:
        return "C 2.0"
    if 67 <= percentage <= 69:
        return "C+ 2.3"
    if 70 <= percentage <= 72:
        return "B- 2.7"
    if 73 <= percentage <= 76:
        return "B 3.0"
    if 77 <= percentage <= 79:
        return "B+ 3.3"
    if 80 <= percentage <= 84:
        return "A- 3.7"
    if 85 <= percentage <= 89:
        return "A 4.0"
    if 90 <= percentage <= 100:
        return "A+ 4.0"


if __name__ == '__main__':
    print(get_all_course())



