"""
Student
 - First name
 - Last name
 - Student number

Course
 - Course name
 - Course code  
 
Assessment
 - Questions 10
 - Marks
 - Date
 - Lecturer
 - Answers
"""

class Student(object):
    """
    This is a blueprint for the student demographic data
    """
    
    def __init__(self, student_firstname, student_lastname,student_number):
        self.student_firstname =  student_firstname
        self.student_lastname = student_lastname
        self.student_number = int(student_number)

    def print_demographic(self):
        """
        This is the function that returns students demographic data
        """

        return "{} {}".format(self.student_firstname, self.student_lastname)
    
class Course(object):
    """
    This is a blueprint for course information
    """
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = int (course_code)
        self.assignments = list()


    def print_information(self):
        """
        This function returns a course's information
        """
        return "{}: {}".format(self.course_code, self.course_name)

    # def add_assessment(self, lecturer, date):
    #     """
    #     This function allows lecturers to add Assignment
    #     """
    #     r  = Assessment(lecturer, date)
    #     self.assignments.add(r)

student_1 = Student("Thapelo", "Seletisha", "1234567")
student_demo_1 = student_1.print_demographic()
print(student_demo_1)


student_2 = Student("Teboho", "Molise", "24681012")
student_demo_2 = student_2.print_demographic()
print(student_demo_2)