attend=int(input("Enter Classes attended by you: "))
total_classes=int(input("Enter total number of classes: "))
percent=(attend/total_classes)*100
if percent>=75:
    print("Enough Attendance")
else:
    print("Less attendance .You need more attendance to give Exam.")
    