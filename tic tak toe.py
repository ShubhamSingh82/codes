#Tic Tac Toe
box = [' ' for x in range(9)]

def print_box():
    row1 = "| {} | {} | {} |".format(box[0],box[1],box[2])
    row2 = "| {} | {} | {} |".format(box[3],box[4],box[5])
    row3 = "| {} | {} | {} |".format(box[6],box[7],box[8])
    print(row1)
    print(row2)
    print(row3)
    
def player_move(i):
    if i == "X":
        player = 1
    elif i == "0":
        player = 2
    print("now player {} turn".format(player))
    choice = int(input("enter your move(1-9):"))
    if box[choice - 1]==" ":
        box[choice - 1] = i
    else:
        print()
        print("the space is already filled!")
def is_win(i):
    if(box[0] == i and box[1] == i and box[2] == i):
        return True
    elif(box[3] == i and box[4] == i and box[5] == i):
        return True
    elif(box[6] == i and box[7] == i and box[8] == i):
        return True
    elif(box[0] == i and box[3] == i and box[6] == i):
        return True
    elif(box[1] == i and box[4] == i and box[7] == i):
        return True
    elif(box[2] == i and box[5] == i and box[8] == i):
        return True
    elif(box[0] == i and box[4] == i and box[8] == i):
        return True
    elif(box[2] == i and box[4] == i and box[6] == i):
        return True
    else:
        return False
def is_draw():
    if ' ' not in box:
        return True
    else:
        return False
while True:
    print_box()
    player_move('X')
    print_box()
    if is_win('X'):
        print("X won the match!")
        break
    elif is_draw():
        print("match is draw")
        break
    player_move('0')
    if is_win('0'):
        print_box()
        print("0 won the match!")
        break
    elif is_draw():
        print("match is draw")
        break