"""MEDIUM - Select students"""


# Solution 1
def select_student(students, threshold):
    """Telling apart accepted and refused students according to a threshold."""
    a, r = [], []
    for n, i in students:
        if i < threshold:
            r.append([n, i])
        else:
            a.append([n, i])
    return {
        "Accepted": sorted(a, key=lambda x: x[1], reverse=True),
        "Refused": sorted(r, key=lambda x: x[1]),
    }


# Solution 2
def select_student2(students, threshold):
    """Telling apart accepted and refused students according to a threshold."""
    return {
        "Accepted": sorted(
            [s for s in students if s[1] >= threshold], key=lambda x: x[1], reverse=True
        ),
        "Refused": sorted(
            [s for s in students if s[1] < threshold], key=lambda x: x[1]
        ),
    }


# Solution 3
from operator import itemgetter
from bisect import bisect_left


def select_student3(students, threshold):
    """Telling apart accepted and refused students according to a threshold."""
    students.sort(key=itemgetter(1))
    res = bisect_left([s[1] for s in students], threshold)
    return {"Accepted": students[res:][::-1], "Refused": students[0:res]}


if __name__ == "__main__":
    my_class = [
        ["Kermit Wade", 27],
        ["Hattie Schleusner", 67],
        ["Ben Ball", 5],
        ["William Lee", 2],
    ]
    answer1 = {
        "Accepted": [["Hattie Schleusner", 67], ["Kermit Wade", 27]],
        "Refused": [["William Lee", 2], ["Ben Ball", 5]],
    }
    answer2 = {
        "Accepted": [["Hattie Schleusner", 67]],
        "Refused": [["William Lee", 2], ["Ben Ball", 5], ["Kermit Wade", 27]],
    }

    for p in [
        select_student,
        select_student2,
        select_student3,
    ]:
        assert p(my_class, 20) == answer1
        print(f"{p.__name__:20} \033[92m[ PASS 1 ]\033[0m")
        assert p(my_class, 50) == answer2
        print(f"{p.__name__:20} \033[92m[ PASS 2 ]\033[0m\n")
