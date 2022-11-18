#average doesn't work, it only appends 1 score on line 25

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {'11/17/2022': True, 11/10/2022: True}
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
    else:
      pass
    
  def get_average(self):
    average = sum(grade.scores) / len(grade.scores)
    return print(average)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
    self.scores = []    #added
    self.scores.append(score)    #added
  
  def is_passing(self):
    if self.score >= Grade.minimum_passing:
      return print("{} is a passing score!".format(self.score))
    else:
      return print("{} is a failing score! =(".format(self.score))


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))
pieter.add_grade(Grade(70))

grade = Grade(65)
grade = Grade(100)    #added

grade.is_passing()

pieter.get_average()
