class duplicate():
    def Find_Duplicate(self, dup):
        dup.sort()
        for i in range (1, len(dup)):
            if(dup[i] == dup[i-1]):
                return True
                # duplicate = dup[i] == dup[j]
        return False

sol=duplicate()
Bring=[1,2,3,4,1]
print("The Duplicate is:", sol.Find_Duplicate(Bring))
