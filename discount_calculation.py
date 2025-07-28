#variables
student_name = input("Enter Your Name:")
student_grade = int(input(Enter Your Grade(1-12):"))
base_tution_free = float(int("Enter Your Tution Free"))
academic_topper_states=input("Are You Topper(yes/no)")
discount = 0
if stident_grade<1 or student_grade>12:
print("Invalid Grade should be (1-12):")
exit()
 match student_grade:
 #For grade 10


case 10:
if student_grade == 10:
percent = 3
discount = base_tution_free*(percent/100)
print(f"Name : {student_name}")
print(f"Grade : {student_grade}")
print(f"Topprt Status : {academic_topper_states}")
print(f"Tution Frees: { base_tution_free}")
print(f"Discounted : {discount}(({percent})%) Applied")
print(f"Final Tution Frees{base_tution_fee_discount}")

#for grade 12
case 12:
percent = 5 
if student_grade == 12:
discount = base_tution_free*(percent/100)
print(f"Name : {student_name}")
print(f"Grade : {student_grade}")
print(f"Topprt Status : {academic_topper_states}")
print(f"Tution Frees: { base_tution_free}")
print(f"Discounted : {discount}(({percent})%) Applied")
print(f"Final Tution Frees{base_tution_fee_discount}")

#other academics
case_:
precent = 0
print(f"Name : {student_name}")
print(f"Grade : {student_grade}")
print(f"Topprt Status : {academic_topper_states}")
print(f"Tution Frees: { base_tution_free}")
print(f"Discounted : {discount}(({percent})%) Applied")
print(f"Final Tution Frees{base_tution_fee_discount}")