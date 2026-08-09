class student():
    def __init__ (self, name , marks):
        self.name=name
        self.marks=marks
        print("Database is created")

s1=student("Karan" , 67)  
print (s1.name, s1.marks)      