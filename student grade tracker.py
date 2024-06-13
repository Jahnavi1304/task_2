class Student:
  """
  A class to represent a student with name and grades.
  """
  def __init__(self, name):
    self.name = name
    self.grades = {}  # Dictionary to store grades (subject: grade)

  def add_grade(self, subject, grade):
    """
    Adds a grade for a specific subject to the student's record.
    """
    self.grades[subject] = grade

  def calculate_average(self):
    """
    Calculates the average grade for all subjects.
    """
    if not self.grades:
      return None  # Return None if no grades added
    total = sum(grade for grade in self.grades.values())
    average = total / len(self.grades)
    return average

  def print_grades(self):
    """
    Prints the student's name, grades for each subject, and overall average.
    """
    if not self.grades:
      print(f"{self.name} has no grades entered yet.")
      return
    print(f"Student Name: {self.name}")
    for subject, grade in self.grades.items():
      print(f"\tSubject: {subject}, Grade: {grade}")
    average = self.calculate_average()
    if average:
      print(f"\tAverage Grade: {average:.2f}")  # Format average to 2 decimal places

def main():
  # Create a new student
  student_name = input("Enter student name: ")
  student = Student(student_name)

  while True:
    # User options
    print("\nMenu:")
    print("1. Add Grade")
    print("2. Print Grades")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
      subject = input("Enter subject name: ")
      grade = float(input("Enter grade (0-100): "))
      # Validate grade input (between 0 and 100)
      if 0 <= grade <= 100:
        student.add_grade(subject, grade)
        print("Grade added successfully!")
      else:
        print("Invalid grade. Please enter a value between 0 and 100.")
    elif choice == '2':
      student.print_grades()
    elif choice == '3':
      print(f"Goodbye! Thanks for using the student grade tracker.")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
  main()
