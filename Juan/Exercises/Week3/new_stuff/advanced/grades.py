# Look at students.dat -> write a class (Student) with the following methods:
#     - get_average
#     - get_score
#     - get_last_score
#     - get_passing_grade
#
# for get score they should be able to enter a number that returns the score for
# the nth test.
#
# for get_passing_grade assume they have a final which counts for 1/2 their grade
# and return the minimum score they need to get to pass.
#
# Try to write the tests and then write the code to pass them.

class Student:
    def __init__(self, scores):
        self.scores = scores
    def get_average(self):
        scores = self.scores
        avg = 0
        for i in scores:
            avg += i
        avg /= len(scores)
        return avg
    def get_score(self, n):
        return self.scores[n - 1]
    def get_last_score(self):
        return self.scores[-1]
    def get_passing_grade(self):
        tot_points = len(self.scores) * 200
        score_needed = tot_points * 60 / 100
        for n in self.scores:
            score_needed -= n
        return score_needed / len(self.scores)

Stud = Student([99, 98, 97, 96, 95])
assert Stud.get_average() == 97

assert Stud.get_score(1) == 99

assert Stud.get_last_score() == 95

assert Stud.get_passing_grade() == 23
