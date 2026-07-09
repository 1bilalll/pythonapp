
def calculate_love_score():
    score=0
    score2=0
    name1=input("can you give name: ")
    name2=input("can you give name2: ")
    name1_liste=list(name1)
    name2_liste=list(name2)
    
    for i in name1_liste:
        if i=="t":
            score +=1  
        if i=="r":
            score +=1  
        if i=="u":
            score +=1  
        if i=="e":
            score +=1 
        
    for j in name2_liste:
        if j=="l":
            score2 +=1  
        if j=="o":
            score2 +=1
        if j=="v":
            score2 +=1
        if j=="e":
            score2 +=1
        
    print(f"Love Score :{score+score2}")
calculate_love_score()