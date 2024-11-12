board = ['_','_','_',
         '_','_','_',
         '_','_','_']
possible = [1,2,3,4,5,6,7,8,9]
def display():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("_"*5)
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("_"*5)
    print(f"{board[6]}|{board[7]}|{board[8]}")
def move():
    count = 1
    play = 0
    while play<=8:
        if count%2!=0:
            pos = int(input("enter the position: "))
            if pos+1 in possible:
                board[pos]='x'
                possible.remove(pos+1)
                count =  count + 1
                display()
                if win()==True:
                    break
        else:
            pos = int(input("enter the position: "))
            if pos+1 in possible:
                board[pos]='o'
                possible.remove(pos+1)
                count = count + 1
                display()
                if win()==True:
                    break
        play = play + 1

def win():
    win1 = False
    #rows
    if board[0] == board[1] == board[2] and board[0] != '_':
        print(f"Game over! {board[0]} wins")
        win1 = True
    elif board[3] == board[4] == board[5] and board[3] != '_':
        print(f"Game over! {board[3]} wins")
        win1 = True
    elif board[6] == board[7] == board[8] and board[6] != '_':
        print(f"Game over! {board[6]} wins")
        win1 = True
    
    #columns
    elif board[0] == board[3] == board[6] and board[0] != '_':
        print(f"Game over! {board[0]} wins")
        win1 = True
    elif board[1] == board[4] == board[7] and board[1] != '_':
        print(f"Game over! {board[1]} wins")
        win1 = True
    elif board[2] == board[5] == board[8] and board[2] != '_':
        print(f"Game over! {board[2]} wins")
        win1 = True
    
    #diagonals
    elif board[0] == board[4] == board[8] and board[0] != '_':
        print(f"Game over! {board[0]} wins")
        win1 = True
    elif board[2] == board[4] == board[6] and board[2] != '_':
        print(f"Game over! {board[2]} wins")
        win1 = True

    return win1

def main():
    display()
    move()
main()