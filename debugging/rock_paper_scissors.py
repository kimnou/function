# from random import randint
# def win():
#     print('You win!')
# def lose():
#     print('You lose!')
# while True:
#     player_choice=input('  What do you pick? (rock, paper, scissors):')
#     player_choice.strip()
#     random_move=randint(0, 2)
#     moves=['rock', 'paper', 'scissors']
#     computer_choice=moves[random_move]
#     if player_choice==computer_choice:
#         print ('Draw!')
#     elif player_choice=='rock' and computer_choice=='scissors':
#         win()
#     elif player_choice=='rock' and computer_choice=='paper':
#         lose()
#     elif player_choice=='paper' and computer_choice=='scissors':
#         lose()
#     elif player_choice=='scissors' and computer_choice=='paper':
#         win()
#     elif player_choice=='scissors' and computer_choice=='rock':
#         lose()
#     elif player_choice=='paper' and computer_choice=='rock':
#         win()
#     again=input('Do you want to play again? (y or n)').strip()
#     if again=='n':
#         break


# def function_add(k):
#     if k > 0:
#         res=k-1
#     else:
#         res=0
#     return res
# print(function_add(6))


# def add(k) :
#     if (k > 0): 
#         res=k + add(k - 1)
#         print(res)
#     else :
#         res=0
#     return res
# add(6)



