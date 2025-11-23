import os


print("===== STUDENT MARKS & GRADE CALCULATOR =====\n")

# basic details
name = input("Student Name : ")
roll = input("Roll No.     : ")

# marks input (6 subjects)
print("\nEnter marks of these 6 subjects (out of 100):\n")

hindi = float(input("Hindi          : "))
eng = float(input("English          : "))
maths = float(input("Mathematics    : "))
sci = float(input("Science          : "))
sansk = float(input("Sanskrit       : "))
sst = float(input("Social Studies   : "))

# grade function for each subject
def get_grade(m):
    if m >= 90:
        return "A++"
    if m >= 80:
        return "A+"
    if m >= 70:
        return "A"
    if m >= 60:
        return "B"
    if m >= 50:
        return "C"
    if m >= 33:
        return "D"
    return "F"

# total calculation
total = hindi + eng + maths + sci + sansk + sst
percent = (total / 600) * 100

# overall grade
if percent >= 90:
    overall = "A++"
elif percent >= 80:
    overall = "A+"
elif percent >= 70:
    overall = "A"
elif percent >= 60:
    overall = "B"
elif percent >= 50:
    overall = "C"
elif percent >= 33:
    overall = "D"
else:
    overall = "F"

# check pass & fail
sub_marks = [hindi, eng, maths, sci, sansk, sst]
if all(m >= 33 for m in sub_marks):
    result = "PASS"
else:
    result = "FAIL"

# ask if subjectwise grade needed
ask = input("\nDo you want subject-wise grades? (Yes/No): ")

subject_text = ""
if ask.lower() == "yes":
    subject_text += "\n--------------------------------\n"
    subject_text += "Subject-wise Grades:\n"
    subject_text += "--------------------------------\n"
    subject_text += f"Hindi          : {get_grade(hindi)}\n"
    subject_text += f"English        : {get_grade(eng)}\n"
    subject_text += f"Mathematics    : {get_grade(maths)}\n"
    subject_text += f"Science        : {get_grade(sci)}\n"
    subject_text += f"Sanskrit       : {get_grade(sansk)}\n"
    subject_text += f"Social Studies : {get_grade(ssts)}\n" if False else f"Social Studies : {get_grade(sst)}\n"
    subject_text += "--------------------------------\n"
    print(subject_text)

# print final report
print("\n===== REPORT CARD =====")
print(f"Name        : {name}")
print(f"Roll Number : {roll}")
print("------------------------------")
print(f"Total Marks : {total}/600")
print(f"Percentage  : {percent:.2f}%")
print(f"Grade       : {overall}")
print(f"Result      : {result}")
print("==============================")

# folder creation
folder = "ReportCards"
os.makedirs(folder, exist_ok=True)

# filename
fname = f"{name.replace(' ', '')}{roll}.txt"
full_path = os.path.join(folder, fname)

# prepare report text
report_data = f"""
===== STUDENT REPORT CARD =====
Name        : {name}
Roll Number : {roll}
--------------------------------
Marks:
Hindi          : {hindi}
English        : {eng}
Mathematics    : {maths}
Science        : {sci}
Sanskrit       : {sansk}
Social Studies : {sst}
--------------------------------
Total Marks : {total}/600
Percentage  : {percent:.2f}%
Grade       : {overall}
Result      : {result}
"""

if ask.lower() == "yes":
    report_data += subject_text

report_data += "================================"

# saving to file
with open(full_path, "w") as f:
    f.write(report_data)

print(f"\nReport saved successfully at: {full_path}")