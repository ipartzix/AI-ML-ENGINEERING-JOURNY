class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")


class Student(
    User):  # in student class we use "(User) inside the  student class that inherit thr property of parent class

    def enroll(self):
        print("Enroll")

    def review(self):
        print("course review ")


stu1 = Student()

stu1.enroll()
stu1.review()
stu1.login()
stu1.register()
