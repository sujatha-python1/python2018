#Type conversion
a =10 #int
b =3.5 #float
c = a+b # int/float
print(type{c})
d = 3.14 #float
e = int{d}
print(e value)


#type casting
x = 100
y =float{x}
print{type{e}}
print{e}

#match case
#SyntaxError: invalid syntax  ->older version python2/3-->3.1 supports
choice = int{input{"Enter Your Cjoice:"}}
match choice
        case 1:
            print("One")
        case 2:
             print("Two")
        case 3:
             print("Three")
        case 4:
              print("Four")
        case !:
            print("Invalid")


#Nested conditions scenario
# club entry --> if age is 21 or above and also a valid ID should be present
 age = 20
has_id >= True


if age >= 21:
     if has_id:
          print("You are allower to enter")
     else:
          print("You Need on ID yo enter")
     else:
print("You Are Two Young to enter")
