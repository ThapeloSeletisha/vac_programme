class Student(object):
    """
    This is a blueprint for the student demographic data
    """
    def __init__(self, firstname, lastname,student_number):
        self.firstname =  firstname
        self.lastname = lastname
        self.student_number = int(student_number)

    def __repr__(self):
        """
        """
        return "{} {}".format(self.firstname, self.lastname)
    
class Course(object):
    """
    This is a blueprint for course information
    """
    def __init__(self, course_name, course_code, lecturer):
        self.course_name = course_name
        self.lecturer = lecturer
        self.course_code =  course_code
        self.assignments = list()

    def __repr__(self):
        return "{}: {}".format(self.course_name, self.lecturer)

    def add_assessment(self, lecturer, date):
        """
        This function allows lecturers to add Assignment
        args:
            lecturer: this is a lectures name
            date: this this the date in format DD/MM/YYYY
        returns:
            returns true on success and false on failure
        """
        r  = Assessment(lecturer, date)
        self.assignments.add(r)

class Question(object):
    """
    A blueprint for storing a question and its answer
    """
    def __init__(self, question_statement, correct_answer):
        self.question_statement = question_statement
        self.correct_answer = correct_answer

    def __repr__(self):
        return "{} {}".format(self.question_statement, self.correct_answer)

    def get_ask_and_evaluate(self):
        """
        This method prints the question and
        accepts the solution from the student.
        It returns true if the students gets the correct answer
        Else return false
        """
        print(self.question_statement)
        user_solution = input("")
        if user_solution == self.correct_answer:
            return True
        else:
            return False

class Assessment(object):
    """
    This is blueprint for asssignment details
    """
    def __init__(self, title, date):
        self.title = title
        self.date = date
        self.questions = list()
        self.marks = 0
    
    def __repr__(self):
        pass

    def add_question(self, question):
        """
        Adds question to the questions list
        """
        questions.append(question)


    


# student_1 = Student("Thapelo", "Seletisha", "1234567")
# student_demo_1 = student_1.print_demographic()
# print(student_demo_1)


# student_2 = Student("Teboho", "Molise", "24681012")
# student_demo_2 = student_2.print_demographic()
# print(student_demo_2)

# student_1 = Student("Thapelo", "Seletisha", "1234567")
# print(student_1)

# course_obj = Course("Linear Algebra", "MATH2025", "Genius")
# print(course_obj)

question_obj = Question("Was Mandela born on the 18th of July, 1950", "False")
question_1 = question_obj.get_ask_and_evaluate()
if (question_1):
    print("The answer is correct")
else:
    print("The answer is incorrect")
