computer_choice = 'scissor'
user_choice = input('Do you want a rock, paper, scissor, lizard, spock?\n')
if computer_choice == user_choice:
    print("SERI")
elif user_choice == "rock" and computer_choice == "scissor":
    print("User win")
elif user_choice == "rock" and computer_choice == "lizard":
    print("User win")   
elif user_choice == "paper" and computer_choice == "rock":
    print("User win")
elif user_choice == "paper" and computer_choice == "spock":
    print("User win")
elif user_choice == "scissor" and computer_choice == "paper":
    print("User win")
elif user_choice == "scissor" and computer_choice == "lizard":
    print("User win")
elif user_choice == "lizard" and computer_choice == "spock":
    print("User win")
elif user_choice == "lizard" and computer_choice == "paper":
    print("User win")
elif user_choice == "spock" and computer_choice == "rock":
    print("User win")
elif user_choice == "spock" and computer_choice == "scissor":
    print("User win")
else:
    print("You lose :( Computer Win :)")