import random

from sklearn.utils import compute_class_weight

def play():
    user = input("What\s your choice? 'r' for ROCK, 'p' for PAPER, 's' for SCISSORS: \n")
    computer = random.choice(['r', 'p', 's'])
    # r > s, p > r, r > s
    if user == computer:
        return 'It\s a TIE'
    
    if is_win(user, computer):
        return 'Yay! You WON!'
    
    return 'Sorry! You LOST'



def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 'r' and opponent == 's'):
        return True

print(play()) 
