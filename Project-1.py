#Developed By Nishikanta Ngangom
#Project On
#Quize Application

#Menu Function
def Menu():
    print("\nChoose a category : ")     
    print("1). Animals\n2). Plants\n3). History\n4). Exit\n")
    op = input() 
    return op        
    
#Score Function    
def Score(scores):
    print("\nYour Score: %d / 10" %scores)

#Main Function
player = input("Enter your name: ") #Input Player's Name
print("\nWelcome Mr/Ms. ", player)   #Display Player's Name
points = 0
option = Menu()
while option != '4':
    print("\nYou Have Choosen Option: ", option)
    if option == '1':
        for i in range(1,11):
            if i == 1:
                choice = int(input("Q. Which is the largest mammal in the earth?\n1) White Shark 2) Blue Whale 3) Elephant 4) Human\n"))
                if choice == 2:
                    points += 1
                else:
                    pass
            elif i == 2:
                choice = int(input("Q. What is the name of the largest cat in the world?\n1) Siberian Tiger 2) Lion 3) Elephant 4) White Tiger\n"))
                if choice == 1:
                    points += 1
                else:
                    pass
            elif i == 3:
                choice = int(input("Q. An ungulate animal has what?\n1) Red Eyes 2) Short Tails 3) Hoofs 4) Furs\n"))
                if choice == 3:
                    points += 1
                else:
                    pass 
            elif i == 4:
                choice = int(input("Q. Which animal can see both ultra-violet and infra-red lights?\n1) Shark 2) Gold Fish 3) Turtle 4) Dolphin\n"))
                if choice == 2:
                    points += 1
                else:
                    pass 
            elif i == 5:
                choice = int(input("Q. The tortoise belongs to which class of animals\n1) Reptiles 2) Fish 3) Amphibians 4) Mammal\n"))
                if choice == 1:
                    points += 1
                else:
                    pass
            elif i == 6:
                choice = int(input("Q. What will you call a rhinoceroses group?\n1) Flock 2) Crowd 3) Lump 4) Crash\n"))
                if choice == 4:
                    points += 1
                else:
                    pass
            elif i == 7:
                choice = int(input("Q. Which mammal sleeps on its back?\n1) Dogs 2) Elephants 3) Monkeys 4) Humans\n"))
                if choice == 4:
                    points += 1
                else:
                    pass
            elif i == 8:
                choice = int(input("Q. What is known as the largest reptile in the world?\n1) Anaconda 2) Saltwater Crocodile 3) Turtle 4) Frog\n"))
                if choice == 2:
                    points += 1
                else:
                    pass
            elif i == 9:
                choice = int(input("Q. Which land snake is known as the fastest moving snake in this world?\n1) Black Mamba 2) Cobra 3) Python 4) Asian Pipe Snake\n"))
                if choice == 1:
                    points += 1
                else:
                    pass
            else:
                choice = int(input("Q. Which cat cannot retract its claws?\n1) Home Cat 2) Tiger 3) Cheetah 4) Tabby Cat\n"))
                if choice == 3:
                    points += 1
                else:
                    pass  
        Score(points)                                                                   
    elif option == '2':
        for i in range(1,11):
            if i == 1:
                choice = int(input("Q. Trees are leafless for a shorter or longer season of the year in?\n1) Scrub Jungle forest 2) Evergreen forest 3) Tropical 4) Desert\n"))
                if choice == 1:
                    points += 1
                else:
                    pass
            elif i == 2:
                choice = int(input("Q. Oxygen liberated during photosynthesis is coming from?\n1) Leave 2) Stem 3) Water 4) Root\n"))
                if choice == 3:
                    points += 1
                else:
                    pass
            elif i == 3:
                choice = int(input("Q. The age of a tree can be determined more or less accurately by?\n1) Skin 2) Counting numbers of rings in the trunk 3) Number of Branch 4) Leave Color\n"))
                if choice == 2:
                    points += 1
                else:
                    pass
            elif i == 4:
                choice = int(input("Q. What type of roots are the hanging structures in a banyan tree?\n1) Tree roots 2) Branch roots 3) Stem roots 4) Prop roots\n"))
                if choice == 4:
                    points += 1
                else:
                    pass
            elif i == 5:
                choice = int(input("Q. Which of the following is the tallest perennial grass?\n1) Lemon grass 2) Tulsi 3) Bamboo 4) Ferns\n"))
                if choice == 3:
                    points += 1
                else:
                    pass
            elif i == 6:
                choice = int(input("Q. Cotton fibre is obtained from which part of the plant?\n1) Petals 2) Leaves 3) Fruit 4) Seeds\n"))
                if choice == 3:
                    points += 1
                else:
                    pass
            elif i == 7:
                choice = int(input("Q. The common edible mushroom is a?\n1) Black Mushroom 2) Mass of fungal spores 3) White Mushroom 4) Dead Part\n"))
                if choice == 2:
                    points += 1
                else:
                    pass
            elif i == 8:
                choice = int(input("Q. Which among the following is not a true fruit?\n1) Apple 2) Mango 3) Lichi 4) Pineapple\n"))
                if choice == 1:
                    points += 1
                else:
                    pass
            elif i == 9:
                choice = int(input("Q. Which of the following plants is referred to as a living fossil?\n1) Ginkgo 2) Sea Umbra 3) Bushes 4) Shrubs\n"))
                if choice == 1:
                    points += 1
                else:
                    pass
            else:
                choice = int(input("Q. Sandalwood tree is considered a?\n1) Big Tree 2) Long Living 3) Partial root parasite 4) Have ring formation\n"))
                if choice == 3:
                    points += 1
                else:
                    pass
        Score(points)        
    elif option == '3':
        for i in range(1,11):
            if i == 1:
                choice = int(input("Q. Who is famous in the name of 'Sher-a-Punjab'?\n1) Rajguru 2) Bhagat Singh 3) Udham Singh 4) Lala Lajpat Raj\n"))
                if choice == 4:
                    points += 1
                else:
                    pass
            elif i == 2:
                choice = int(input("Q. The first Indian Governor of Independent India-General-\n1) Rajgopalachari 2) Surindnath 3) Rajendra Prasad 4) B.R.Ambedkar\n"))
                if choice == 1:
                    points += 1
                else:
                    pass
            elif i == 3:
                choice = int(input("Q. The first secret ruler who issued coins-\n1) Shrigupta 2) Chandragupta First 3) Samundragupta 4) Chandragupta Second\n"))
                if choice == 2:
                    points += 1
                else:
                    pass
            elif i == 4:
                choice = int(input("Q. When was the National Council of Education established?\n1) 15 Aug 1906 2) 15 Aug 1903 3) 15 Aug 1904 4) 15 Aug 1905\n"))
                if choice == 1:
                    points += 1
                else:
                    pass
            elif i == 5:
                choice = int(input("Q. When was the muslim league established?\n1) 1904 2) 1906 3) 1910 4) 1915\n"))
                if choice == 2:
                    points += 1
                else:
                    pass
            elif i == 6:
                choice = int(input("Q. What movement is the relationship of 'do or die'?\n1) Dandi 2) Ashawagoa 3) Khaliphate 4) Quit India\n"))
                if choice == 4:
                    points += 1
                else:
                    pass
            elif i == 7:
                choice = int(input("Q. When was Mahatma Gandhi first arrested during 'Satyagraha'?\n1) 1906 2) 1908 3) 1913 4) 1917\n"))
                if choice == 2:
                    points += 1
                else:
                    pass
            elif i == 8:
                choice = int(input("Q. Who was the last Mughal Emperor?\n1) Babur 2) Noor Jehan 3) Akbar 4) Bahadur Shah\n"))
                if choice == 4:
                    points += 1
                else:
                    pass
            elif i == 9:
                choice = int(input("Q. Panchayati Raj comes under-\n1) Residual List 2) Concurrent List 3) Static List 4) Union List\n"))
                if choice == 3:
                    points += 1
                else:
                    pass
            else:
                choice = int(input("Q. Red Cross was founded by-\n1) A.Cursetji 2) Badel Powell 3) J.H.Durant 4) Tygve Lie\n"))
                if choice == 3:
                    points += 1
                else:
                    pass
        Score(points)        
    else:
        print("Please Enter A Vald Option!\n")
    
    print("\nWant to try again!")
    option = Menu()

print("Program Has Been Ended!")
#End Of Program       