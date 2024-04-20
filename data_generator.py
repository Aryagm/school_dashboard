import numpy as np
from scipy.stats import skewnorm


def generate_grades(num_grades):
    subjects = [
        "physics",
        "computer science",
        "english",
        "art",
        "law",
        "engineering",
        "chemistry",
    ]
    grades = {subject: [] for subject in subjects}

    # skewness parameter, positive value means right skew. random num between 3.5 and 4.5
    alpha = 3.5

    # generate random grades with right-skewed normal distribution
    math_grades = skewnorm.rvs(alpha, loc=70, scale=11, size=num_grades)
    # cap grades at 99 and round to nearest integer
    math_grades = np.round(np.clip(math_grades, 40, 99))

    for grade in math_grades:
        for subject in subjects:
            grade_uncertainty = np.random.randint(1, 5)
            # round final grade to nearest integer
            grades[subject].append(int(np.clip(grade + grade_uncertainty, 40, 99)))

    physics_shift = -7
    computer_science_shift = 8
    english_shift = -2
    art_shift = 10
    law_shift = 9
    engineering_shift = 8
    chemistry_shift = -5

    # apply shifts to grades
    grades["physics"] = [grade + physics_shift for grade in grades["physics"]]
    grades["computer science"] = [
        grade + computer_science_shift for grade in grades["computer science"]
    ]
    grades["english"] = [grade + english_shift for grade in grades["english"]]
    grades["art"] = [grade + art_shift for grade in grades["art"]]
    grades["law"] = [grade + law_shift for grade in grades["law"]]
    grades["engineering"] = [
        grade + engineering_shift for grade in grades["engineering"]
    ]
    grades["chemistry"] = [grade + chemistry_shift for grade in grades["chemistry"]]

    # clip grades to 40-100
    for subject in subjects:
        grades[subject] = np.clip(grades[subject], 40, 100)

    return grades


grades = generate_grades(200)

np.save("./data/grades.npy", grades)
