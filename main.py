#Day 4 Final Challenge from 100 Days of Code - The Complete Python Pro Bootcamp for 2021 on Udemy

import random 

#---------------------------------------------------------------------------------
def main():

#---------------------------------------------Game Images-----------------------------------

# I could have chosen to store these images in an array so I would only have to remember each word's position in the array instead of each word, but it's rock-paper-scissors. I think it's easier to rememer that instead. . . 

    rock = '''
        _______
    ---'   ____)
         (_____)
         (_____)
          (____)
    ---.___(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              ________)
            _________)
    ----_________)
    '''

    scissors = ''' 
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)

    '''

#-----------------------------------------------------------------------------------------------

    your_score = 0
    computer_score = 0
    keep_playing = True

    while keep_playing == True:

        computer_choice = random.randint(0,2)

        if computer_choice == 0:
            computer_chose = "rock"
        elif computer_choice == 1:
            computer_chose = "paper"
        else:
            computer_chose = "scissors"

        user_choice = input("What will you choose? Tye 0 for rock, 1 for paper, or 2 for scissors.\n\n")

        if user_choice == "0":
            print("\nYou chose rock.\n")
            print(rock + "\n")
        elif user_choice == "1":
            print("\nYou chose paper.\n")
            print(paper + "\n")
        elif user_choice == "2":
            print("\nYou chose scissors.\n")
            print(scissors + "\n")
        else:
            print("\nThat wasn't a choice!\n")

        print("The computer chose " + computer_chose + "\n")

        if computer_choice == 0:
            print(rock)
        elif computer_choice == 1:
            print(paper)
        elif computer_choice == 2:
            print(scissors)
        else:
            print("ERROR")

        if user_choice == "0":
            if computer_choice == 0:
                print("It's a tie!")
            elif computer_choice == 1:
                print("The computer wins!")
                computer_score += 1
            else:
                print("You win!")
                your_score += 1
        elif user_choice == "1":
            if computer_choice == 0:
                print("You win!")
                your_score += 1
            elif computer_choice == 1:
                print("It's a tie!")
            else:
                print("The computer wins!")
                computer_score += 1
        else:
            if computer_choice == 0:
                print("The computer wins!")
                computer_score += 1
            elif computer_choice == 1:
                print("You win!")
                your_score += 1
            else:
                print("It's a tie!")

        print (f"Your score is {your_score}: The computer's score is {computer_score}")

#---------------------------------Play Again?----------------------------------------------
        play_again = input("Play again? (y/n)\n").lower()
        if play_again == "y":
            print ("\n")
        else:
            print("\n")
            if your_score > computer_score:
                print ("You were the overall winner! This time. . .")
            elif your_score == computer_score:
                print("It was an overall tie, there were no real winners today. . .")
            else:
                print("The computer won a majority of the time. .  .")
            print("Goodbye!")
            keep_playing = False

#------------------------------------------START GAME-----------------------------
game_start = input("Would you like to play a game of rock paper scissors? (y/n)\n").lower()

if game_start == "y":
    print ("\n")
    main()
else:
    print("\n")
    print("Goodbye!")
    keep_playing = False
#-------------------------------------------------------------------------------------