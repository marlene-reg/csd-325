import json

student = {
        "F_Name": "Ellen",
        "L_Name": "Ripley",
        "Student_ID": "45604",
        "Email": "eripley@gmail.com"
    },
{
        "F_Name": "Arthur",
        "L_Name": "Dallas",
        "Student_ID": "45605",
        "Email": "adallas@gmail.com"
    },
{
        "F_Name": "Joan",
        "L_Name": "Lambert",
        "Student_ID": "45714",
        "Email": "jlambert@gmail.com"
    },
{
        "F_Name": "Thomas",
        "L_Name": "Kane",
        "Student_ID": "68554",
        "Email": "tkane@gmail.com"
    }
    

student_dict = json.load(student)

print(type(student))
print(type(student_dict))


print(file.read())


