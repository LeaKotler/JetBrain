# Write your code here
import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute('DROP TABLE card')

cur.executescript('''
CREATE TABLE card(id INTEGER PRIMARY KEY AUTOINCREMENT,
number TEXT,
pin TEXT,
balance INTEGER DEFAULT 0);
''')


class Card:
    def __init__(self):
        self.number = 0
        self.password = 0
        
    def create(self):
        number_a = 400000000000000 + random.randint(0, 999999999)
        number_b = str(number_a)
        x = 0
        count = 0
        for b in number_b:
            i = int(b)
            if count % 2 == 0:
                j = i * 2
            else:
                j = i
            if j > 9:
                j -= 9
            x += j
            count += 1
        if x % 10 == 0:
            c = 0
        else:
            c = 10 - x % 10
        self.number = number_a * 10 + c
        self.password = random.randint(1000, 9999)
        print("Your card number:")
        print(self.number)
        print("Enter your PIN:")
        print(self.password)
        cur.execute('INSERT INTO card (number,pin) VALUES (?,?)', (str(self.number), str(self.password)))
        conn.commit()




def balance(num):
     cur.execute('SELECT balance FROM card WHERE number=?', (num,))
     balan = cur.fetchone()
     print("Balance:",balan)



def do_transfer(num):
    my_number =num
    print(my_number)
    print("Transfer")
    transf_card =input("Enter card number:\n")
    print(transf_card)
     # if int(transf_card) == self.number:
       ##     print("You can't transfer money to the same account!")
      #      menu2(self)

    if not luhn(transf_card):
        print("Probably you made mistake in card number. Please try again!")
        menu2(num)
    else:
        cur.execute('SELECT balance FROM card WHERE number=?', (transf_card,))
        bal = cur.fetchone()
        if bal is None:
            print("Such a card does not exist.")
            menu2(num)
        else:
            m_tran = int(input("Enter how much money you want to transfer:\n"))
            cur.execute('SELECT balance FROM card WHERE number=?', (my_number,))
            bal2 = cur.fetchall()
            balan2 = bal2[0]
            balan= bal[0]
            if int(balan2[0]) > m_tran:
                 if int(transf_card) ==my_number:
                     print("dont")
                     menu2(num)
                 else:
                     cur.execute('UPDATE card SET balance = balance - ? WHERE number =?', (m_tran,my_number))
                     cur.execute('UPDATE card SET balance = balance + ? WHERE number =?', (m_tran,transf_card))
                     conn.commit()
                     print("Success!")
                     menu2(num)
            else:
                 print('Not enough money!')
                 menu2(num)
def log_in():
    print("Enter your card number:")
    num = input()
    print("Enter your PIN:")
    pas = input()
    cur.execute('SELECT pin FROM card WHERE number=?', (num,))
    pin_to_test = cur.fetchone()
    if pin_to_test is None:
         print("Wrong card number!")
    else:
         if pas not in pin_to_test:
             print("Wrong PIN!")
         else:
             print("You have successfully logged in!")
             menu2(num)


def add_income(num):
     add_in =int(input("Enter income:\n"))
     cur.execute('SELECT balance FROM card WHERE number=?', (num,))
     balan = cur.fetchone()
     balan = int(balan[0])+add_in
     cur.execute('UPDATE card SET balance = (?) WHERE number =?', (str(balan),num))
     conn.commit()
     print("Income was added!")
     menu2(num)
def close_account(num):
    cur.execute('DELETE FROM card WHERE number =?', (num,))
    conn.commit()
    print("Deleted!")

def menu2(num):
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")
    n = int (input())
    if n == 1:
        balance(num)
    elif n == 2:
        add_income(num)
    elif n ==3:
        do_transfer(num)
        print(num)
    elif n ==4:
        close_account(num)
    elif n ==5:
        print("5")
    elif n ==0:
        print("Bye!")
        global flag
        flag=False
    else:
        print('Wrong number')
        menu2(num)

def menu1():
    global flag
    flag = True
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    while flag:
        choise = int(input())
        if choise == 1:
            new_card.create()
            menu1()
        elif choise == 2:
            log_in()
        elif choise == 0:
            print('Bye!')
            flag = False
        else:
            print("wrong number!")

def luhn(num):
    count = 0
    x=0
    for b in num:
        i = int(b)
        if count % 2 == 0 and count<len(num)-1:
            j = i * 2
        else:
            j = i
        if j > 9:
            j -= 9
        x += j
        count += 1
    if x % 10 == 0:
        return True
    else:
        return False

global flag
flag = True
new_card = Card()
menu1()