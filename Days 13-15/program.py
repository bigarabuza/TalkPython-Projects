from custom_classes import Player, Roll
import random

def main():
    print_header()
    
    name = get_players_name()
    
    rolls = build_the_three_rolls()
    
    player1 = Player(name)
    player2 = Player('computer')

    game_loop(player1, player2, rolls)
    
def get_players_name():
    return input('Enter name: ')

def print_header():
    print()
    print('------------------------------------')
    print('       Rock, Paper, Scissors!       ')
    print('------------------------------------')
    print()

def build_the_three_rolls():
    return [Roll() for _ in range(3)]
    

def game_loop(player1, player2, rolls):
    count = 0
    results = []
    while count < 3:
        p2_roll = random.choice(rolls)
        p1_roll = Roll(input('Pick rock, paper, or scissors: '))

        outcome = p1_roll.can_defeat(p2_roll.name)
        results.append(outcome)
        
        # display throws
        print(f'{player1.name} rolled: {p1_roll.name}')
        print(f'{player2.name} rolled: {p2_roll.name}')

        # display winner for this round
        print(f'{player1.name} {outcome}s')

        count += 1
    
    # Compute who won    
    if results.count('win') > results.count('lose'):
        print(f'{player1.name} wins the game!')
    elif results.count('win') == results.count('lose'):
        print('It\'s a draw!')
    else:
        print(f'{player1.name} loses!')

if __name__ == "__main__":
    main()