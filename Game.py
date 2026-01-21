p1 = input("Enter Player 1 name (X): ")
p2 = input("Enter Player 2 name (O): ")

b = ['1','2','3','4','5','6','7','8','9']
turn = 'X'

def winner(b, p):
    return (
        b[0]==b[1]==b[2]==p or
        b[3]==b[4]==b[5]==p or
        b[6]==b[7]==b[8]==p or
        b[0]==b[3]==b[6]==p or
        b[1]==b[4]==b[7]==p or
        b[2]==b[5]==b[8]==p or
        b[0]==b[4]==b[8]==p or
        b[2]==b[4]==b[6]==p
    )

while True:
    print("|",b[0],"|",b[1],"|",b[2],"|")
    print("!-----!-----!-----!")
    print("|",b[3],"|",b[4],"|",b[5],"|")
    print("!-----!-----!-----!")
    print("|",b[6],"|",b[7],"|",b[8],"|")

    name = p1 if turn == 'X' else p2
    pos = int(input(f"{name} ({turn}) choose position: ")) - 1

    if b[pos] != 'X' and b[pos] != 'O':
        b[pos] = turn

        if winner(b, turn):
            print(f"{name} wins!")
            break

        turn = 'O' if turn == 'X' else 'X'