students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
a=sorted(students,key=lambda s:s[1],reverse=True)
print(a)
print(students[:2])