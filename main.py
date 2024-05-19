import art as a
import random as r
from art import data
from art import logo
# from art import youlose
# def ain(n1,n2,score):
    
def s(score):
    score+=1
    return score



def gameplay(game,n1,n2,score):
    while game:
        if n1==n2:
            n2=r.choice(data)
        print("Compare A:")
        for i in n1:
            if i=='country':
                print(f"from {n1[i]}",end='.')
            elif i!='follower_count':
                print(f"{i}: {n1[i]}",end=' ,')
            else:
                a=n1[i]
        # print("\n"*3)
        # print("\n",a) #n1 follower count



        print("""
         _    __    
        | |  / /____
        | | / / ___/
        | |/ (__  ) 
        |___/____(_)
        """)

        print("Against B:")
        for j in n2:
                if j=='country':
                    print(f"from {n2[j]}",end='.')
                elif j!='follower_count':
                    print(f"{j}: {n2[j]}",end=' ,')
                else:
                    b=n2[j]
        # print("\n",b) #n2 follower count
        
        abin=input("\n\nWho has more followers? type 'A' or'B':\n").upper()
        print("\n"*3)
        if abin=='A':
            # ain(n1,n2,score) 
            for i in n1:
                for j in n2:
                    if i=='follower_count' and j=='follower_count':
                        if n1[i]>n2[j]:
                            print("\n"*3)
                            score+=1
                            print(f"Your current score is:{score}")
                            # l1.append(n1)
                            n2=r.choice(data)
                            # l2.append(n2)
                            # l3.append(n3)
                            # print("iiiiiiiii")
                        else:
                            print("\n"*3)
                            game=False
                            print(f"Sorry you are wrong!!! Final Score is:{score}")
                            # print(youlose)
                            print("""
 __     ______  _    _   _      ____   _____ ______ _ _ _  
 \ \   / / __ \| |  | | | |    / __ \ / ____|  ____| | | | 
  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__  | | | | 
   \   /| |  | | |  | | | |   | |  | |\___ \|  __| | | | | 
    | | | |__| | |__| | | |___| |__| |____) | |____|_|_|_| 
    |_|  \____/ \____/  |______\____/|_____/|______(_|_|_) 
                                 """)
                            print(f"The Follower Count of {n2['name']} is {b}")
                            print(f"The Follower Count of {n1['name']} is {a}")
        

        elif abin=='B':
            for i in n1:
                for j in n2:
                    if i=='follower_count' and j=='follower_count':
                        if n1[i]<n2[j]:
                            print("\n"*3)
                            score+=1
                            print(f"Your Current score is:{score}")
                            # l1.append(n2)
                            n1=n2
                            n2=r.choice(data)
                            # l2.append(n1)
                            # print("jjjj")
                        else:
                            print("\n"*3)
                            game=False
                            print(f"Sorry you are wrong!!! Final Score is:{score}")
                            # print(youlose)
                            print("""
 __     ______  _    _   _      ____   _____ ______ _ _ _  
 \ \   / / __ \| |  | | | |    / __ \ / ____|  ____| | | | 
  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__  | | | | 
   \   /| |  | | |  | | | |   | |  | |\___ \|  __| | | | | 
    | | | |__| | |__| | | |___| |__| |____) | |____|_|_|_| 
    |_|  \____/ \____/  |______\____/|_____/|______(_|_|_) 
                                 """)
                            print(f"The Follower Count of {n1['name']} is {a}")
                            print(f"The Follower Count of {n2['name']} is {b}")


        else:
            print("INVALID!!!! TYPE 'A' or 'B'")
            game=False
    
print(logo)
n1=r.choice(a.data)
n2=r.choice(a.data)

game=True

score =0


while input("Do you want to paly Higher/Lower!!: type 'y' or 'n':\n").lower()=='y':
    gameplay(game,n1,n2,score)   
    print("\n")                
    print("THE END!!!!!!")
