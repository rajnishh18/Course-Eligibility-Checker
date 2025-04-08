name=input("name :")
Age=int(input("age:"))
Course=input("course:")
Marks=int(input("marks in 12th :"))


print("Hii ",name)
print("It is Your result")
"""print("My age is ",Age)
print("I want the course",Course)
print("My marks is ",Marks,"%")"""


if (Marks>=95):
    print("You are directly eligible for the course")
    print("First you fill the form ")
    
elif(Age<=16 and (Marks==60 or Marks<=94)):
    print("You are eligible for the Course But You have to submit the paper")

else:
    print("You are not eligible for this course ")
    print("You Choose another course ")
    print("These are the Course:")
    print("B.TECH(ELE)")
    print("B.TECH(Mac)")
    print("BCA")
    print("BBA")





