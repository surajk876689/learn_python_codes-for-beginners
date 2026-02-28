student_marks = []  # Create an empty list to store student marks   
Student1=float(input("Enter marks of student 1: "))  # Take input for student 1 marks and convert it to integer
student_marks.append(Student1)  # Append student 1 marks to the list
Student2=float(input("Enter marks of student 2: "))  # Take input for student 2 marks and convert it to integer
student_marks.append(Student2)  # Append student 2 marks to the list    
Student3=float(input("Enter marks of student 3: "))  # Take input for student 3 marks and convert it to integer
student_marks.append(Student3)  # Append student 3 marks to the list
Student4=float(input("Enter marks of student 4: "))  # Take input for student 4 marks and convert it to integer
student_marks.append(Student4)  # Append student 4 marks to the list
Student5=float(input("Enter marks of student 5: "))  # Take input for student 5 marks and convert it to integer
student_marks.append(Student5)  # Append student 5 marks to the list
print("Marks of students before sorting: ", student_marks)  # Print the marks of students before sorting
student_marks.sort()  # Sort the marks in ascending order
print("Marks of students after sorting: ", student_marks)  # Print the marks of students after sorting