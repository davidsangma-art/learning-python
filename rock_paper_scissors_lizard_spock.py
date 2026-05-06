import random
player=0
CPU=0

print('1.✊ rock')
print('2.✋ paper')
print('3.✌️ scissor')
print('4.🦎 lizard')
print('5.🖖 spock')
player=int(input('Pick a number (1-5)'))

CPU= random.randint(1,3)

choices={1:'✊ rock', 2:'✋ paper', 3:'✌️ scissor',4:'🦎 lizard', 5:'🖖 spock'}
print(f"You picked:{choices[player]}")
print(f"CPU picked:{choices[CPU]}")

wins={1:3,2:1,3:2,1:4,4:5,5:3,3:4,2:5,5:1,}
if player==CPU:
    print('tie')
elif wins[player]==CPU:
    print('You won!')
else:
    print('CPU won!')



