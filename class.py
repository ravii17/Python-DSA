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


#class & attribute 
