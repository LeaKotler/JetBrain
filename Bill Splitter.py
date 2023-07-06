# write your code here
import random
print('Enter the number of friends joining (including you):')
n = int(input())
friends={}
if n >0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(n):
        friends[input()]=0
    print()
    print('Enter the total bill value:')
    bill = int(input())
 
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    if lucky == 'Yes':
        r = random.choice([x for x in friends])
        print(f'{r} is the lucky one!')
        print()
        for x in friends:
            if x not in r:
                friends[x] = round(bill / (n-1),2)
    
    else:
        print()
        print('No one is going to be lucky')
        for x in friends:
            friends[x] = round(bill / (n),2)
    print()
    print(friends)
    
else:
    print('No one is joining for the party')