def read_students(filename):
    students = {}
    with open(filename, 'r', encoding='utf-8') as f:
        next(f) 
        for line in f:
            student_id, name = line.strip().split(', ')
            students[student_id] = name
    return students

def read_scores(filename):
    scores = {}
    with open(filename, 'r', encoding='utf-8') as f:
        next(f) 
        for line in f:
            student_id, _, score = line.strip().split(', ')
            score = int(score)
            if student_id in scores:
                scores[student_id].append(score)
            else:
                scores[student_id] = [score]
    return scores

def calculate_grades(students, scores):
    results = []
    for student_id, name in students.items():
        student_scores = scores.get(student_id, [])
        total_scores = len(student_scores)
        sum_scores = sum(student_scores)
        avg_score = round(sum_scores / total_scores, 1) if total_scores > 0 else 0.0
        results.append((student_id, name, total_scores, sum_scores, avg_score))
    return results

def write_grades(filename, results):
    """Writes the calculated grades to a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Student ID,Name,Total Scores,Sum of All Scores,Score Average\n")
        for record in results:
            f.write(",".join(map(str, record)) + "\n")
    print(f"Grades saved to {filename}")

def main():
    student_file = "student_clean.txt" 
    scores_file = "scores_clean.txt" 
    output_file = "grades.txt"  

    students = read_students(student_file)
    scores = read_scores(scores_file)
    results = calculate_grades(students, scores)
    write_grades(output_file, results)

if __name__ == "__main__":
    main()