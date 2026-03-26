#Cliff Nallding Victor
# Dean's List or Honor 
# This app will record student names and their GPAs and determin wether the student is qualify for Dean's List or Honor society 

while True:
    student_last_name = input("Enter last name or enter ZZZ to quit:")
    if student_last_name == "ZZZ":
        break
    student_first_name = input("Enter first name:")
    student_GPA = float(input("Enter GPA:"))
    if student_GPA >= 3.5:
        print(student_last_name, "has made the Dean's List")
    elif student_GPA >= 3.25:
        print(student_last_name, "has made the Honor Roll")
    

# Tested with:
# Smith, John → 3.6 → Dean's List
# Pierre, Marie → 3.3 → Honor Roll
# Johnson, Alex → 2.8 → no list
# Nguyen, Chris → 3.8 → Dean's List
# Martinez, Sofia → 3.25 → Honor Roll
