rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game=[rock, paper, scissors]
print("Welcome to RoCk_PaPeR_ScIsSoR Game!😎")
choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
print(game[choose])
import random
rand=random.randint(0,2)
if (rand==0 and choose==1):
  print(f"Computer choose:\n{game[rand]}\nYou Win.💃")
elif (rand==0 and choose==2):
  print(f"Computer choose:\n{game[rand]}\nYou Lose.\nBETTER_LUCK_NEXT_TIME🙃.")
elif (rand==1 and choose==0):
  print(f"Computer choose:\n{game[rand]}\nYou Lose.\nBETTER_LUCK_NEXT_TIME🙃.")
elif (rand==1 and choose==2):
  print(f"Computer choose:\n{game[rand]}\nYou Win.💃")
elif (rand==2 and choose==0):
  print(f"Computer choose:\n{game[rand]}\nYou Win.💃")
elif (rand==2 and choose==1):
  print(f"Computer choose:\n{game[rand]}\nYou Lose.\nBETTER_LUCK_NEXT_TIME🙃.")
elif (rand<0 or choose>=3):
  print(f"You typed an invalid number, You Lose!\nBETTER_LUCK_NEXT_TIME🙃.")
else:
  print(f"Computer choose:\n{game[rand]}\nYou Draw.😅")