import math

mark_list = []

# Ask user for Number of student and marks
student = int(input("Number of students: "))


# Putting List of student into Dict
marks_dic = {}
for i in range(1, student+1):
    student_marks = str(input("Enter marks a,b,c,d: "))
    marks_dic[i] = student_marks.split(',')
    
total = 0
# Total marks for each student
for i in range(1,student+1):
    marks_list = marks_dic[i]
    x = (int(marks_list[0])+int(marks_list[1])+int(marks_list[2])+int(marks_list[3]))
    print(f"Student {i}:   {x} marks")
    total += x
    

# Average for each test
mark_list1 = marks_dic[1]
mark_list2 = marks_dic[2]
mark_list3 = marks_dic[3]
print(f"Average for Test 1:   {((int(mark_list1[0])+int(mark_list2[0])+int(mark_list3[0])))//4} marks")
print(f"Average for Test 2:   {((int(mark_list1[1])+int(mark_list2[1])+int(mark_list3[1])))//4} marks")
print(f"Average for Test 3:   {((int(mark_list1[2])+int(mark_list2[2])+int(mark_list3[2])))//4} marks")
print(f"Average for Test 4:   {((int(mark_list1[3])+int(mark_list2[3])+int(mark_list3[3])))//4} marks")



    

average = math.ceil(total / student)
print(f'Average score per student:   {average} marks')