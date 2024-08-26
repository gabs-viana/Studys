import random

def play():
    user = input("What's your choice? 'r' para Rock, 'p' para Paper, 's' para Scissor\n")
    ia = random.choice(['r', 'p', 's'])

    if user == ia:
        return 'Empate'
    
    if is_win(user, ia):
        return 'Você venceu'
    
    return 'Você perdeu bobão'
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
        

print(play()) 