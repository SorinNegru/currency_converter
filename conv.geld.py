print("Hey I can convert your money in (D)ollars , (E)uro ,(G)pb")
money = input('Pick what money do you have ').upper()
amount = float(input('How much do you have? '))
money_2 = input("Pick what money to convert ").upper()
while money == 'D':
     if money_2 == 'E':
          print(f'You have {amount * 0.70} euros ')
          break
     elif money_2 == 'G':
          print(f'You have {amount * 0.38} gpb')
          break
     else:
          print('sorry i dont understand')
          break
while money == 'E':
     if money_2 == 'D':
          print(f'You have {round(amount / 0.70)} dollars')
          break
     elif money_2 == 'G':
          print(f'You have {amount *  0.28} gpb')
          break
     else:
         print('sorry i dont understand')
         break
while money == 'G':
     if money_2 == 'D':
          print(f'You have {round(amount / 0.38)} dollars')
          break
     elif money_2 == 'E':
          print(f'You have {round(amount / 0.28)} euros')
          break
     else:
          print('sorry i dont understand')
          break