name=input("Enter your name: ")
attendence=int(input("Enter your attendance percentage:"))
registeration=input("Enter have your registered or not (yes/no) :")
if attendence>=75 and registeration.lower()=="yes":
    print("you are eligible for the exam")
else:
    print("you are not eligible for the exam")