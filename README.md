## Student Grade Tracker (Python)

This Python program is a simple student grade tracker that allows you to:

* Add grades for specific subjects.
* Calculate and view the overall average grade.
* View a list of all entered grades for a student.

### Usage

1. **Run the Script:**
   Save the code as `student_grade_tracker.py` and run it from your terminal using:

   ```bash
   python student_grade_tracker.py
   ```

2. **Student Information:**
   The program will prompt you to enter a student's name. This name will be used to track their grades.

3. **Menu:**
   The program presents a menu with the following options:

   - **1. Add Grade:** Enter a subject name and a grade (between 0 and 100) to add it to the student's record.
   - **2. Print Grades:** View the student's name, list of grades for each subject, and overall average (if grades have been added).
   - **3. Exit:** Terminate the program.

   Select your choice by entering the corresponding number (1-3) and pressing Enter.

### Features

* **Grade Addition:** Add grades for multiple subjects with their corresponding values.
* **Average Calculation:** Calculates the overall average grade for all entered subjects.
* **Grade Display:** View a list of all entered grades and the calculated average (formatted to two decimal places).
* **Input Validation:** Ensures entered grades are within the valid range (0-100).

### Future Enhancements

This is a basic implementation, and you can consider extending it with features like:

* **Letter Grade Conversion:** Convert the overall average grade to a letter grade based on a defined scale (e.g., A for 90-100, B for 80-89, etc.).
* **Grade Deletion:** Allow removing previously entered grades for a subject.
* **Data Persistence:** Implement saving and loading student data to a file (e.g., CSV, JSON) to persist information across program runs.

## Dependencies

This program requires Python 3 to run. No additional libraries are needed.
