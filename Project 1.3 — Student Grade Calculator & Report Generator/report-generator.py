students = { 'Rony Kenoly' : {
                'Math' : [85, 90, 78, 92],
                'Statistics' : [50, 65, 89, 80],
                'DataScience' : [75, 80, 85, 90]
            },
            'Okafor Chidalu' : {
                'Math' : [65, 49, 78, 92],
                'Statistics' : [50, 65, 89, 80],
                'DataScience' : [75, 80, 85, 90]
            },
            'Alfred Johnson' : {
                'Math' : [85, 90, 78, 92],
                'Statistics' : [50, 65, 89, 80],
                'DataScience' : [75, 80, 85, 90]
            }
}


def calculate_grade(average):
    if average >= 80:
        return 'A', 5.0
    elif average >= 65:
        return 'B', 4.0
    elif average >= 50:
        return 'C', 3.0
    elif average >= 45:
        return 'D', 2.0
    elif average >= 40:
        return 'E', 1.0
    else:
        return 'F', 0.5
    

def student_summary(student_name, scores):

    subject_results = {}
    subject_averages = []


    for subject, marks in scores.items():

        average = sum(marks) / len(marks)

        grade, point = calculate_grade(average)
        subject_averages.append(average)
        
        subject_results[subject] = {
            'average': average,
            'grade': grade,
            'point': point
        }

    overall_average = sum(subject_averages) / len(subject_averages)
    overall_grade, overall_point = calculate_grade(overall_average)
    return {
            'name': student_name,
            'subjects': subject_results,
            'average': overall_average,
            'grade': overall_grade,
            'gpa': overall_point
            }

for name, scores in students.items():

    summary = student_summary(name, scores)
    all_students = []
    all_students.append(summary)
    ranked_students = sorted(
    all_students,
    key=lambda student: student['average'],
    reverse=True
)


summary = student_summary(
    'Rony Kenoly',
    students['Rony Kenoly']
)

print(summary)