student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

## sum by python
sum_score = 0
total_score = sum(student_scores)
print(total_score)

#my sum test
for score in student_scores:
    sum_score += score
    print(sum_score)

## Max by python
max_score = max(student_scores)
print(max_score)

#my sum test
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)