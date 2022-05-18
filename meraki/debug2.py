#==============arbitraryArgument====================
def greet(*names):
    for name in names:
        print("Welcome", name)
greet("Rinki", "Vishal", "Kartik", "Bijender")



#==============default parameter value=================
# def info(name, age = "5"):
#     print(name + " is " + age + " years old")
# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")



# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
# studentDetails("Nilam","loop","rose")