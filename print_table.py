#import sys
import random

#cp949

def print_table(round, com_card, com_chips, player_chips, table_chips):
    print('\n-----------------------------------------------------')
    print('\n<< ROUND ' + "{0:2s}".format(str(round)) + ' >>')
    print('          ┌----------┐     ')
    print('          │'+com_card['suit']+'        │     '+'-Com Chips:', com_chips)
    print('          │    '+"{0:2s}".format(str(com_card['rank']))+'    │     ')
    print('          │        '+com_card['suit']+'│     ')
    print('          └----------┘     ')
    print('             (- __ -)     ')
    print('         ─────────     ')
    print('        *                  *     ')
    print('       *                    *     ')
    print('      *                      *     -Table Chips:', table_chips)
    print('     *                        *     ')
    print('    *    ┌--------------┐    *     ')
    print('   *     │              │     *     ')
    print('  *      │              │      *     ')
    print(' -───-│              │────     '+'-My Chips:',player_chips)
    print('         │              │     ')
    print('         │              │     ')
    print('         │              │     ')
    print('         │              │     ')
    print('         └--------------┘     ')   


 # 칩개수는 숫자로 / 카드표시 변수(사전형태)


#player_chips, cpu_chips = 30, 30
#playercard = {'suit' : '♠' , 'rank' : 11}
#print_table(0, playercard,player_chips,cpu_chips)
