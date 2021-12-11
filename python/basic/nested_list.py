"""
https://www.hackerrank.com/challenges/nested-list/
"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = []
    for score in sorted([score for [name, score] in students]):
        if score not in scores:
            scores.append(score)
    # print(sorted_scores)
    print("\n".join(sorted([
        student[0]
        for student in students
        if student[1] == scores[1]
    ])))
 