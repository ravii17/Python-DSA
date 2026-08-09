f = open ("Hello.txt", "a")
# this is how we can make changes in the file and write to it
f.write("\nThis is the append mode")
f.close()

# if we dont have file python can make that file for us

f = open ("Samaple.txt", "w")
f.write ("How will you make this code work if you this much error in it")
f.close()  

# r+ is used to over write the file.

