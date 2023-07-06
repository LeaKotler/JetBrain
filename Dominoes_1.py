# Write your code here
import random
def split_pieces():
    global stock,computer,player
    for p in pieces:
        
        if len(computer)>6 and len(player)>6:
            x = 2
        elif len(computer)>6 and len(stock)>13:
            x = 3
        elif len(player)>6 and len(stock)>13:
            x = 1
        elif len(computer)>6:
            x = random.randint(2,3) 
        elif len(player)>6:
            x = random.randint(1,2)
        else:
            x = random.randint(1,3)
            
            
        if x == 2:
            stock.append(p)
        elif x == 1:
            computer.append(p)
        elif x == 3:
            player.append(p)
            
def print_print():
    global stock,computer,player,domino_snake,moove,rrr,ddd
    print('======================================================================')
    print('Stock size:',len(stock))
    print('Computer pieces:',len(computer))
    print()
    print(str(domino_snake)[1:-1])
    print()
    print("Your pieces:")
    i=1
    for p in player:
        print(f'{i}:{p}')
        i+= 1
    print()
def print_dom():
    global stock,computer,player,domino_snake,moove
    print_print()
    if moove == 'player':
        print("Status: It's your turn to make a move. Enter your command.\n")
        move_player()
        moove = 'computer'
    elif moove == 'computer':
        print('Status: Computer is about to make a move. Press Enter to continue...')
        move_comp()
        moove = 'player'
    elif not check_moove():
        print("false!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    chek_snake()
     
def check_moove():
    com = False
    for p in computer:
        if (p[0] or p[1]) == (domino_snake[0][0] or domino_snake[-1][1]):
            com = True
    for p in player:
        if (p[0] or p[1]) == (domino_snake[0][0] or domino_snake[-1][1]):
            com = True
    return com
        
        
        
def move_comp():
    global stock,computer,player,domino_snake,moove
    input()
    m = False
    stat=computer + domino_snake
    statistica=[]
    for i in range(0,7):
        count = 0
        for p in stat:
            if p[0] == i:
                count +=1
            if p[1] == i:
                count += 1
        statistica.insert(i,count)
    statistica_comp=[]
    i=0
 #   print(computer)
    st=[a for a in computer]
    new = []
    d=[]
    while len(st)>0 and not m:
        f = -1
        for p in st:
            a = statistica[p[0]]+ statistica[p[1]]
            statistica_comp.append(a)
            i+=1
        f = statistica.index(max(statistica))
        if st[f][0] == domino_snake[0][0]:
            d = st[f]
            domino_snake.insert(0,d[::-1])
            st.pop(f)
            m=True
            moove = 'player'
            
        elif st[f][1] == domino_snake[0][0]:
            d = st[f]
            domino_snake.insert(0,st[f])
            st.pop(f)
            m=True
            moove = 'player'
            
        elif st[f][1] == domino_snake[-1][1]:
            d = st[f]
            domino_snake.append(d[::-1])
            st.pop(f)
            m=True
            moove = 'player'
            
        elif st[f][0] == domino_snake[-1][1]:
            d = st[f]
            domino_snake.append(st[f])
            st.pop(f)
            m=True
            moove = 'player'
            
        else:
            st.pop(f)
    i=0
#    print(d)
 #   print(computer)
    for p in computer:
       # print(len(computer))
        if p == d:
            computer.pop(i)
            statistica.pop(i)
        i+=1   
    if not m:
        if len(stock)>0:
            i = random.randint(0,len(stock)-1)
            computer.append(stock[i])
            stock.pop(i)       
    moove = 'player'
    
    
            
        
    
    
    
    
            
def move_player():
    global stock,computer,player,domino_snake,moove
    x = input()
    if x in '1234567-1-2-3-4-5-6-7':
        x = int(x) 
        if x<0:
            x = -x
            y=x-1
            if player[y][0] == domino_snake[0][0]:
                d = player[y]
                domino_snake.insert(0,d[::-1])
                player.pop(y)
                moove = 'computer'
            elif player[y][1] == domino_snake[0][0]:
                domino_snake.insert(0,player[y])
                player.pop(y)
                moove = 'computer'
            else:
                print("Illegal move. Please try again.")
                move_player()
        
        elif x>0:
            x=x-1
            if player[x][0] == domino_snake[-1][1]:
                domino_snake.append(player[x])
                player.pop(x)
                moove = 'computer'
            elif player[x][1] == domino_snake[-1][1]:
                d = player[x]
                domino_snake.append(d[::-1])
                player.pop(x)
                moove = 'computer'
            else:
                print("Illegal move. Please try again.")
                move_player() 
    elif x in '0':
        moove = 'computer'
        if len(stock)>0:
            i = random.randint(0,len(stock)-1)
            player.append(stock[i])
            stock.pop(i)

    else:
        print('Invalid input. Please try again.')
        move_player()
    
    
    
def chek_snake():
    global stock,computer,player,domino_snake,moove, end
    end = True
    if len(domino_snake)>=8:
        if (domino_snake[0][0] or domino_snake[0][1] ) == (domino_snake[-1][0] or domino_snake[-1][1] ):
            end = False
    return end
        
    
    
pieces = []
for i in range(0,7):
    for j in range(i,7):
        pieces.append([i,j])
global stock,computer,player,domino_snake,moove
stock = []
computer = []
player = []
flag = True
while flag:
    split_pieces()
    dupl = [[x,x] for x in range(0,7)]
    moove = 0
    domino_snake = [[7,7]]
    
    for d in dupl:
        if d in computer:
            del domino_snake[0]
            domino_snake.append(d)
            moove = 'player'
        elif d in player:
            del domino_snake[0]
            domino_snake.append(d)
            moove = 'computer'
    if moove == 'player':
        computer.remove(domino_snake[0])
        flag = False
    elif moove == 'computer':
        player.remove(domino_snake[0])
        flag = False
end = True
rrr=1
ddd=1
while len(computer)>0 and len(player)>0 and chek_snake()and check_moove():
    print_dom()
if len(computer) == 0:
    print_print()
    print('Status: The game is over. The computer won!')
elif len(player) == 0:
    print_print()
    print('Status: The game is over. You won!')
else:
    print_print()
    print("Status: The game is over. It's a draw!")
#print(f'The player makes the first move (status = "{moove}")')
"""
print('Stock pieces:',stock)
print('Computer pieces:',computer)
print('player pieces:',player)
print('Domino snake:',domino_snake)
print('Status:',moove)
"""
    