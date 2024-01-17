class Student:
    def __init__(self,name,age,grade,section):
        self.name=name
        self.age=age
        self.grade=grade
        self.section=section
    
    def students(self):

        return f"my name is {self.name}"

    
    def school(self):
        return (f"I am in {self.grade} of section {self.section}")
        


my_students=Student("tejas",22,"XII","c")


print(my_students.students())
print(my_students.school())
