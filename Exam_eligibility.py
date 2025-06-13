cause=input("Do you have a medical cause? [Y/N]=")
if cause=='Y':
    print("Student is allowed to take the exam")
elif cause=='N':
    attendence=float(input("Enter the attendence="))
    if attendence>75:
        print("Student is allowed to take the exam")
    else:
        print("Student is not allowed to take the exam")
else:
    print("Enter a valid input")