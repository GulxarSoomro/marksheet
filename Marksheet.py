print("       Board of Intermediate and Secondary Education Karachi   ")
print    (                  "Class :  Matric")
Student_Name    =str(input("Enter the name of Student      : "))
roll_num = int(input("Enter Roll Number                    : "))
a = int(input("Enter Sindhi   Marks out of 75              : "))
b = int(input("Enter Urdu     Marks out of 75              : "))
c = int(input("Enter English 1 Marks out of 75             : "))
d = int(input("Enter English 2 Marks out of 75             : "))
a = int(input("Enter Islamiyat Marks out of 75             : "))
e = int(input("Enter Pak.Study Marks out of 75             : "))
f = int(input("Enter Physics(theory)    Marks out of 75    : "))
g = int(input("Enter Physics(Practical) Marks out of 25    : "))
h = int(input("Enter Chemistry(theory)  Marks out of 75    : "))
i = int(input("Enter Chemistry(Practical) Marks out of 25  : "))
j = int(input("Enter Mathametics Marks out of 100          : "))
k = int(input("Enter Biology(theory)   Marks out of 75     : "))
l = int(input("Enter Biology(Practical) Marks out of 25    : "))

obtain_marks = a + b + c + d + e + f + g + h + i + j + k + l
print ("Total Obtain Marks " , obtain_marks , "out of 850 ")
per = int(obtain_marks/850 * 100)
per = float(per)
if obtain_marks >= 680 and  obtain_marks <= 850:
    print ("Grade A1 and Percentage is " , per)
elif obtain_marks >= 595 and obtain_marks <= 679:
    print ("Grade A  and Percentage is " , per)
elif obtain_marks >= 510 and obtain_marks <= 594:
    print("Grade B   and Percentage is " , per)
elif obtain_marks >= 425 and obtain_marks <= 509:
    print("Grade C   and Percentage is " , per)
elif obtain_marks >= 340 and obtain_marks <= 524:
    print("Grade D   and Percentage is " , per)
elif obtain_marks <=390:
     print("Fail")
print ("Best of Luck")