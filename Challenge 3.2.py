"""
implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA (cumulative grade point average) in desendng order . each student object
has the following attributes : name (string), roll_number (string) and cgpa (float). test the function 
with different input lists of students.
"""


class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #sort the list of students in desending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


#example usage:
students = [
    student("hari", "A123", 7.8),
    student("srikanth", "A124", 8.9),
    student("saumya", "A125", 9.1),
    student("mahidar", "A126", 9.9),
]

sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("name: {}, roll number: {}, CGPA{}".format(student.name,
                                                   student.roll_number,
                                                   student.cgpa))
