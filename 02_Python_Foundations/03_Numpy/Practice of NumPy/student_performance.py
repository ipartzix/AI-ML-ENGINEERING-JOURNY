import numpy as np

# Rows = students, Columns = subjects
marks = np.array([
    [78, 85, 90],
    [65, 70, 72],
    [88, 92, 95],
    [55, 60, 58]
])

average_per_student = np.mean(marks, axis=1)
average_per_subject = np.mean(marks, axis=0)

print("Average per student:", average_per_student)
print("Average per subject:", average_per_subject)

# Identify toppers
topper = np.argmax(average_per_student)
print("Topper student index:", topper)
