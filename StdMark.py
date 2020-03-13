StdNm = input("Enter student name:\t")      #Name of student will entered here
StdSur = input("Enter student surname:\t")
mrk = int(input("Enter student mark:\t"))   #his/her mark is entered

if 80<=mrk<=100:
    print(StdNm+" " + StdSur+": "+"Grade A - Outstanding")
elif 60<=mrk<=79:
    print(StdNm +" " + StdSur+":"+"Grade B - Satisfactory:")
elif 50<=mrk<=59:
    print(StdNm + StdSur,"Grade C - Pass")
else:
    print(StdNm + StdSur,"Dismal failure") 