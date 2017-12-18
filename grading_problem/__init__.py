"""Grading problem.

HackerLand University has the following grading policy:
- Every student receives an initial grade in the inclusive range of whole
numbers from 0 to 100.
- A modification is made to the initial grade before it becomes a final grade.
- Any final grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's initial
grade according to these rules:
- If the difference between the initial grade and the next multiple of 5 is
less than 3, round the grade up to the next multiple of 5.
- If the value of the initial grade is less than 38, no rounding occurs as the
result will still be a failing grade.
"""
_input = [73, 67, 38, 33]


def solve(initial_scores):
    """Solve."""
    final_scores = []

    for score in initial_scores:
        if score < 38:
            final_scores.append(score)
        else:
            dist_to_next_multiple_of_5 = 5 - (score % 5)
            if dist_to_next_multiple_of_5 < 3:
                final_scores.append(score + dist_to_next_multiple_of_5)
            else:
                final_scores.append(score)

    return final_scores


if __name__ == '__main__':
    solve(_input)
