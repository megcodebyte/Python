import random

playOne = 0
playTwo = 0

print ("Welcome to the game of Chutes and Ladders! ")
    
while playOne < 100 or playTwo < 100:
        # Player One 
        print ("Player One! ")
        print ("Player One you are on ", playOne, " space. ")
        print ("Rolling the dice...")
        print ("The values are...")
        rand = (random.randint (1, 6)) #Random function for dice roll
        print (rand)
        playOne = rand + playOne  #This variable adds the dice roll to the players space
        print ("Player One is on ", playOne, " space.")
        
        # Player Two
        print ("Player Two! ")
        print ("Player Two you are on ", playTwo, " space. ")
        print ("Rolling the dice...")
        print ("The values are...")
        answer = (random.randint (1, 6)) #Random function for dice roll
        print (answer)
        playTwo = answer + playTwo #This variable adds the dice roll to the players space  
        print ("Player Two is on ", playTwo, " space.")
        
        #Conditionals for ladders
        if playOne == 1: 
           playOne = 38
            
        elif playTwo == 1:
           playTwo = 38
            
        elif playOne == 4:
            playOne = 14
                
        elif  playTwo == 4:
            playTwo = 14
                
        elif playOne == 9:
            playOne = 31
                    
        elif playTwo == 9:
            playTwo = 31
                    
        elif playOne == 21:
            playOne = 42
                        
        elif playTwo == 21:
            playOne = 42
                        
        elif playOne == 28:
            playOne = 84
                            
        elif playTwo == 28:
            playTwo = 84
                            
        elif playOne == 36: 
            playOne = 44
                                
        elif playTwo == 36:
            playTwo = 44
                                
        elif playOne == 51:
          playOne = 67
                                    
        elif playTwo == 51:
            playTwo = 67
                                    
        elif playOne == 71:
            playOne = 91
                                        
        elif playTwo == 71:
            playTwo = 91
                                    
        elif playOne == 80:
            playOne = 100
                                            
        elif playTwo == 80:
            playTwo = 100
        
        
        
        #Condiontals for chutes
        elif playOne == 98: 
               playOne = 78
            
        elif playTwo == 98:
                playTwo = 78
            
        elif playOne == 96:
            playOne = 75
                
        elif  playTwo == 96:
            playTwo = 75
                
        elif playOne == 93:
            playOne = 73
                    
        elif playTwo == 93:
            playTwo = 73
                    
        elif playOne == 87:
            playOne = 24
                        
        elif playTwo == 87:
            playOne = 24
                        
        elif playOne == 62:
             playOne = 10
                            
        elif playTwo == 62:
            playTwo = 10
                            
        elif playOne == 64: 
             playOne = 60
                                
        elif playTwo == 64:
            playTwo = 60
                                
        elif playOne == 56:
            playOne = 53
                                    
        elif playTwo == 56:
           playTwo = 53
                                    
        elif playOne == 48:
            playOne = 26
                                        
        elif playTwo == 48:
            playTwo = 26
                                    
        elif playOne == 49:
            playOne = 11
                                            
        elif playTwo == 49:
            playTwo = 11
                                                 
        elif playOne == 16:
            playOne = 6
                                                     
        elif playTwo == 16:
            playTwo = 6

        #If a player is over 100 the space is reset to 100     
        elif playOne > 100:
            playOne = 100
            
        elif playTwo > 100:
            playTwo = 100
            

        #Condionals for winning the game at space 100   
        elif playOne == 100:
            print ("You Won!!", " Player One is on space:", playOne,)
        elif playTwo == 100:
            print ("You Won!! "," Player Two is on space:", playTwo,)
            exit()

