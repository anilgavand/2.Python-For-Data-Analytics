

# Salary Slip Program

# Taking input from user
emp_no = input("Enter Employee Number : ")
emp_name = input("Enter Employee Name : ")
ctc = float(input("Enter Yearly CTC : "))

# Fixed Employee Details
designation = "Buyer Analyst"
grade_code = "G-7"

# Salary Calculation (based on sample percentage)
monthly_ctc = ctc / 12

basic = monthly_ctc * 0.50
hra = monthly_ctc * 0.357
edu_allowance = 200
lta = monthly_ctc * 0.075

new_gross_salary = basic + hra + edu_allowance + lta

pf_employee = 3000
gratuity = 1754
pf_employer = 3000

# Salary Slip
print("\n" + "=" * 60)
print("                    SALARY SLIP")
print("=" * 60)

print(f"Employee No : {emp_no}")
print(f"Employee Name : {emp_name}")
print(f"Designation : {designation}")
print(f"Grade Code : {grade_code}")

print("\nEARNINGS")
print("-" * 60)
print(f"001 BASIC           : ₹{basic:,.2f}")
print(f"002 HRA             : ₹{hra:,.2f}")
print(f"004 EDU ALLOWANCE   : ₹{edu_allowance:,.2f}")
print(f"008 LTA             : ₹{lta:,.2f}")

print("\nDEDUCTIONS / CONTRIBUTIONS")
print("-" * 60)
print(f"503 P.F. Employee   : ₹{pf_employee:,.2f}")
print(f"Gratuity            : ₹{gratuity:,.2f}")
print(f"503 P.F. Employer   : ₹{pf_employer:,.2f}")

print("\nSUMMARY")
print("-" * 60)
print(f"New Gross Salary    : ₹{new_gross_salary:,.2f}")
print(f"Monthly CTC         : ₹{monthly_ctc:,.2f}")
print(f"Yearly CTC          : ₹{ctc:,.2f}")

print("=" * 60)


