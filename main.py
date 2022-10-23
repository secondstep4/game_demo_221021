from cPackage import Cplace, Centity
import os
import random

def clearing():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

def main_text():
    global map_now
    print('*********************************')
    print('')
    print('now you are in...{0}'.format(map_now.name))
    print('')
    print('===Select your action===\n')
    print('1. move to another place')
    print('2. search for the place')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('**********************************')
    
def dice(num, max) -> list:
    roll_result = []
    for _ in range(num):
        roll = random.randint(1,max)
        roll_result.append(roll)
    return roll_result

def encount_enemy(enemy : Centity) -> bool:
    global entity_hero
    global diff
    

    print('you encounter the enemy')
    print('! -------------------------------- !')
    while True:
        
        dice_result = dice(2,6)
        print('')
        print('****************************************************')
        print('enemy [HP : {0}/{1}] [Power : {2}]'.format(enemy.current_hp, enemy.max_hp, enemy.power))
        print('your [HP : {0} / {1}]'.format(entity_hero.current_hp, entity_hero.max_hp))
        print('your power is...{0}'.format(dice_result))
        print('****************************************************')
        print('')
        input('press any key to attack...')
        
        enemy_power = enemy.power
        your_power = sum(dice_result)

        if enemy_power > your_power :
            if entity_hero.get_dmg(enemy_power) :
                input('you died!')
                return False
            input('you attacked by enmey !')
            input('you got {0} damage!'.format(enemy_power))
        elif enemy_power < your_power :
            if enemy.get_dmg(your_power):
                input('you killed enemy!')
                diff += 1
                return True
            input('you attacked the enemy !')
            input('enemy got {0} damage!'.format(your_power))
        else:
            input('draw !')







def action_move():
    global map_now
    map_list = map_now.get_linked_place()
    print('you can move to...\n')
    for i in range(len(map_list)):
        print('{0}. {1}\n'.format(i, map_list[i].name))
    
    while True:
        command = input('you move to...')
        if 0 <= int(command) and int(command) < len(map_list):
            print('you move to {0}\n\n'.format(map_list[int(command)].name))
            map_now = map_list[int(command)]
            return
        else :
            print('nope!')

def action_search():
    global map_now
    events = Cplace.get_event_list(map_now)
    
    if len(events) == 0 :
        print('nothing here...sad')
        return

    if events.pop(0) == '#event_encount_enemy' :
        entity_enemy = Centity('monster', 20, dice(1,6)[0] + diff)
        if encount_enemy(entity_enemy) :
            print('battle ended, you win !')

        

#it's difficulty
diff = 0
#set map
game_map = []
for i in range(0,5):
    new_map = Cplace('[[map_name_{0}]]'.format(str(i)))
    game_map.append(new_map)
    #set event
    Cplace.add_event(game_map[i], '#event_encount_enemy')


for i in range(0,4):
    game_map[i].add_place(game_map[i+1])
    
map_now = game_map[0]

#set character
entity_hero = Centity('you', 30, 99)

#main loop
while True :
    os.system('cls')
    main_text()
    command = input('I\'ll do... : ')
    if command == '1':
        action_move()
    elif command == '2':
        action_search()
    else :
        print('unknown action, plz write again\n')

    input('press any key to continue....')

    if entity_hero.current_hp == 0 :
        while True :
            input('your story end...')


