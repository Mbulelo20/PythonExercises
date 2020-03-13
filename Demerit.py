DrvNm = input("Enter your name:\t")      #Driver enters his full names
Spd = int(input("Enter your current speed:\t")) #Driver enters his current speed

points = int((Spd - 60)//5)  #points calculated by program
if Spd<=60:
    print("OK!")
elif points >=12:
    print("You have ",points,"points.","Time to go to jail")
else:
    print("You have been penalised: ",points,"points")