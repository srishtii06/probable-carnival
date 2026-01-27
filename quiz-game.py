print("welcome to my computer quiz")
playing=input("do you want to play? ")
if playing.lower()!="yes":
    quit()  #it is in build infunction whuch exits you out of the code
    
print("okay! let's play :)")  

score=0

answer=input("What does CPU stands for? ").lower()
if answer=="central processing unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
answer=input("What does GPU stand for? ").lower() #converts to lower case to resolve case senstive prob
if answer=="graphics processing unit":   #idhr be .lower kr skte the
    print("Correct!")
    score+=1
else:
    print("Incorrect! ")  
    
answer=input("What does RAM stands for? ").lower()
if answer=="random access memory":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")
    
answer=input("What does PSU stands for? ").lower()
if answer=="power supply ":
    print("Correct! ")
    score+=1
else:
    print("Incorrect")    
    
print("You got"+str(score)+"questions correct")    #typecasting to concatenate
print("You got"+str((score/4)*100)+"%")   #display percentage
