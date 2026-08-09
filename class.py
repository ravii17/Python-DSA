"""
class student():
    college_name= "KIIT"
    def __init__ (self, name , marks, age ):
        self.name=name
        self.marks=marks
        self.age=age 
        print("Success")
        
    def welcome(self):
        print("Welcome student", self.name)
    
s1=student("Karan" , 67, 18)  
    

s2=student("ravi" , 89, 16)
print (s1.name, s1.marks, s1.age)  
print (s2.name, s2.marks, s2.age)
print(student.college_name)



s1.welcome()

"""
#class & attribute 

class Student:
    def __init__ (self, name, marks):
        self.name = name 
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print ("hi", self.name , "your avg of marks is :", sum/3)


s1 = Student("Rigya" , [99,99,99])
s1.get_avg()
