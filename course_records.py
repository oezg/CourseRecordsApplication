class Course:
    def __init__(self, course: str, grade: int, credit: int) -> None:
        self.__course = course
        self.__grade = grade
        self.__credit = credit
    
    @property
    def name(self):
        return self.__course
    
    @property
    def grade(self):
        return self.__grade
    
    def upgrade(self, new_grade):
        if new_grade > self.grade:
            self.__grade = new_grade
    
    @property
    def credit(self):
        return self.__credit

    def __str__(self) -> str:
        return f"{self.name} ({self.credit} cr) grade {self.grade}"

class Record:
    def __init__(self) -> None:
        self.__courses = {}

    @property
    def courses(self):
        return self.__courses
    
    def add_course(self, course, grade, credit):
        if course not in self.courses:
            self.courses[course] = Course(course, grade, credit)
        else:
            self.courses[course].upgrade(grade)
    
    def get_course_data(self, course):
        try:
            print(self.courses[course])
        except KeyError:
            print("no entry for this course")
            

    def statistics(self):
        number = len(self.courses)
        total_credit = sum(course.credit for course in self.courses.values())
        total_grade = sum(course.grade for course in self.courses.values())
        mean = total_grade / number
        print(f"{number} completed courses, a total of {total_credit} credits")
        print(f"mean {mean:.1f}")
        self.print_grade_distribution()
    
    def print_grade_distribution(self):
        print("grade distribution")
        distribution = {}.fromkeys(range(5, 0, -1), 0)
        for course in self.courses.values():
            distribution[course.grade] += 1
        for grade in distribution:
            print(f"{grade}: {'x'*distribution[grade]}")

class Application:
    def __init__(self) -> None:
        self.__record = Record()

    @property
    def record(self):
        return self.__record

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))
        self.record.add_course(course, grade, credit)
    
    def get_course_data(self):
        course = input("course: ")
        self.record.get_course_data(course)

    def statistics(self):
        self.record.statistics()

    def execute(self):
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            elif command == "0":
                break
            else:
                self.help()

course_records = Application()
course_records.execute()