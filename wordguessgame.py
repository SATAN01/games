import random 
  
name = input("What is your name? ") 
  
print("Good Luck ! ", name) 
  
words = ['remainder', 'computer', 'science', 'programming',  
         'python', 'mathematics','engineerinng', 'player', 'condition',  
         'reverse', 'water', 'board', 'kitty', 'hydrogen' , 'complex', 'keratine','kreatimine', 'kepler']  
  
word = random.choice(words) 
  
  
print("Guess the characters") 
  
guesses = '' 
  
turns = 5
  
  
while turns > 0: 
    failed = 0
      
    for char in word:  
          
        if char in guesses:  
            print(char) 
              
        else:  
            print("_") 
              
            failed += 1
              
  
    if failed == 0: 
        print("You Win")  
          
        print("The word is: ", word)  
        break
      
    guess = input("guess a character:") 
      
    
    guesses += guess  
      
 
    if guess not in word: 
        
          
        turns -= 1
           
        print("Wrong") 
          
        if turns != 0:
            print("You have", + turns, 'more guesses left') 
          
          
        if turns == 0: 
            print('The word was : ',word)
            print("You Loose! bettter luck next time")
            
