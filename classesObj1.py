# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno

#     def info(self):
#         pass
#         print("Student name is ", self.name," and rollno is",self.rollno)
#         # print("name","rollno")
# a=input("Enter name")
# b=input("Enter rollno")

# student1=student(a,b)
# student2=student("oppo","66")
# student1.info()
# student2.info()
# print(id(student1))
# print(id(student2))

# class person:
#     def __init__(self):
#         self.name="Gaurav"
#         self.number=32
#     def compare(self, other):
#         if (self.number==other.number):
#             return True
#         else:
#             return False

# p1=person()
# p2=person()

# # p1.name="lakshay"
# p1.number=15
# if p2.compare(p1):
#     print("Same")
# else:
#     print("not Same ")
# print(p1.name)
# print(p2.name)


# class car:
#     wheels=4
#     def __init__(self):
#         self.company="BMW"
#         self.mileage=10
# car1=car()
# car2=car()
# # car.wheels=5
# print(car1.company,car.wheels)
# print(car1.mileage,car.wheels)


class student:
    collegename="LPU"
    def __init__(self,python,web,math):
        self.subject1=python
        self.subject2=web
        self.subject3=math
    def avg(self):
        return (self.subject1+self.subject2+self.subject3)/3

    def collegeDetail(cls):
        return cls.collegename



student1=student(4,5,8)
student2=student(5,7,8)
print(student1.avg())
print(student2.avg())
# print(student.collegename)
print(student.collegeDetail(cls=student))