students=int(input("number of students? "))
date=input ("what was the date of the test ")
attempt=int(0)
while int(attempt<students):
    attempt=attempt+1
    name=input("what is the students name? ")
    score=int(input("what is there score on the test "))
    if int(score==100):
        print("they scored an A**")
    elif int(90<score<100):
        print ("they got a A*")
    elif int(80<score<87): 
        print("you got A")
    elif int(87<score<90):
        print ("they got an A")
    elif int(70<score<80):
        print ("they git a B")
    elif int(60<score<70):
        print ("they got a C")
    elif int(50<score<60):
        print("they got a D")
    elif int(13<score<50):
        print("you failed :(")
    elif int(0<score<13): 
        print("you failed :(")
    elif int(score==90): 
        print("they got an A*")
    elif int(score==80):
        print ("they got an A")
    elif int(score==70):
        print("they got a B")
    elif int(score==60):
        print("they got a C")
    elif int(score==50):
        print("they got a D")
    elif int(score==13):
        print("happy halloween from yours truly Connor")
    elif int(score==87):
        print("WAS THAT THE BITE OF 87!!!")