import math
def add(*x):
    print("Sum is "+ str(math.fsum(x)))
    
print(add(20,30, 50))

#Arbitary number of arguments
def students (*student_name): #receive parameter as tuple
    print(student_name, type(student_name))
    for student in student_name:
        print(student)
students('Ahmad', 'Istiak', 'Muhaimeen')
students()
students('Ahmad')
print('--------------------')

#positional and arbitary arguments mixing
def students (captain, *other_student): #receive parameter as tuple
    print('Captain', captain)
    print('Other', other_student)
students('Ahmad', 'Istiak', 'Muhaimeen')

#arbitary keyword arguments
def students (captain, **other_student): #receive parameter as dictionary
    print('Captain', captain)
    print('Other', other_student)
students('Ahmad', f='Istiak', l='Muhaimeen')
