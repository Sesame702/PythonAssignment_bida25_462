# Student Grade Management System
A Python-based grading system developed to digitize and manage student records, calculate academic metrics, and enable dynamic data operations across multiple subjects.

## Project Overview
This project was built iteratively across three main devlopment phases:

* **Section A: Initial Setup (Scalar Objects & Loops)**
*  Basic student data entry using scalar variables (`float`, `int`).
*  Grade input validation loop requiring numeric scores between 0 and 100.
*  Calculation and display of class total and overall average grades.

* **Section B: Expanding with Data Structures (Lists & Tuples)**
* Multi-subject grade management (Math, English, Science).
* Data modeling using immutable tuples for student records: `(name, [grades_list])`.
* Class-wide analytics capturing highest and lowest subject scores using `max()` and `min()`.
* Formatted summary table reporting individual student subject averages.

* **Section C: Advanced Management (Nested Dictionaries)**
* Transition to key-value mapping: `students = {"Name": {"Subject": [Grade]}}`.
* Iteractive CLI menu allowing continuous operations:
 * **Add**: Insert new student profiles with subject lists.
 * **Update**: Modify individual subject scores.
 * **Remove**: Delete student entries using key deletion('del').
 * **Search**: Query student records by name to retrieve subject breakdown and overall average.
 * **Filter**: View subject-specific grade distributions across the whole class.

## File Structure
* `bida25-462_assignment.py` - Main Python program script.
* `README.md` - Project documentation and submission details.

## How to Run the Program
1. Ensure Python 3.x is installed on your system.
2. Open termina;/IDE (e.g., PyCharm) in the project directory.
3. Execute the script:
   ```bash
   python bida25-462_assignment.py
