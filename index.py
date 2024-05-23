mark=int(input("Enter the grades"))
def calculate_grade(mark):
    if mark<0 or mark>100:
        return"Invalid Marks"
    elif mark>79:
        return "A"
    elif mark>=60 and mark<=79:
        return "B"
    elif mark>49 and mark<=59:
        return "C"
    elif mark>=40 and mark<=49:
        return "D"
    else:
        return "E"  

print(calculate_grade(mark))                      
