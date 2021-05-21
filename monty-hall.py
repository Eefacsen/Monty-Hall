from os import times
import random

# FUNCTIONS

def game_on():
    try:
        runs = 0
        wins = 0

        while runs < 100000:
            #set doors
            doors = ['door_1','door_2','door_3']
            #set prize_door
            prize_door = random.choice(doors)
            #set choice_1
            choice_1 = random.choice(doors)
            #show info
            if runs == 0:
                print('\n\n[1] [2] [3]')
                print('you have chosen {}'.format(choice_1))
            #remove 1 door
            if prize_door == choice_1:
                doors.remove(prize_door)
                open_door = random.choice(doors)
                doors.remove(open_door)
            else:
                doors.remove(prize_door)
                doors.remove(choice_1)
                open_door = doors[0]
                doors.remove(open_door)
                doors.append(prize_door)
            #show info
            if runs == 0:
                print('The host opens {} revealing nothing inside'.format(open_door))
                #ask user for change or no change
                print('You are now asked if you would stick to your original chosen door or do you change your choice')
                lever = int(input('[1] - Stick\n[2] - Change\n-->:'))
            #set choice_2 door
            if lever == 999:
                print('back to main menu')
                break;
            elif lever == 1:
                choice_2 = choice_1
            elif lever == 2:
                choice_2 = doors[0]        
            #compare prize door to choice_door
            if choice_2 == prize_door:
                wins += 1
                status = 'won'
            else:
                status = 'lost'
            runs += 1

        #show results
        print(f'We ran the game show {runs} times')
        print(f'You won the car {wins} times')
        print(f'success rate of {wins/runs*100}%')

        input('\nPress enter to continue')
    except Exception as e:
            print('Error in game_on : {}'.format(e))



# VARIABLES

projectName = 'Monty Hall Problem'

# MAIN LOOP

def menu1():
    usingMenu1 = True
    while usingMenu1:
        print('------------')
        print(' {} '.format(projectName))
        print('------------')
        
        print('You are on a game show. There are 3 doors and behind 1 door is a car.')
        print('The first door you choose is random and auto selected by this program')
        print('The game show host now reveals 1 of the remaining 2 doors which does NOT contian the car')
        print('His question is now, do you change your door choice to the remaining door or stay with your original selection?')
        print('This program with run 100 000 senarios of your choice and return your new statistics')

        print('\n[1] - Start')
        print('At any time enter 999 to return')
        try:
            op = int(input('--> : '))
            if op == 999:
                usingMenu1 = False
                print('Good Bye')
            elif op == 1:
                game_on()
            else:
                print('Invalid selection')
        except Exception as e:
            print('Error in usingMenu1 : {}'.format(e))

if __name__ == '__main__':
    menu1()