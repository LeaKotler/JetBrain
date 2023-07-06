.py
def plain(t):
    text = input('Text:')
    return t+text

def bold(t):
    text = input('Text:')
    return t+'**'+text+'**'

def italic(t):
    text = input('Text:')
    return t+'*'+text+'*'
    
def header():
    flag = True
    while flag:
        type_h = int(input("Level:"))
        if 1 <= type_h <= 6:
            text = input('Text:')
            flag = False
            return '#'*type_h +' '+ text+'\n'
        else:
            print('The level should be within the range of 1 to 6')
        
        

def link(t):
    label = input("Label:")
    url = input('URL:')
    return f'{t}[{label}]({url})'
    

def inline_code(t):
    text = input('Text:')
    return f'{t}`{text}`'
    

def ordered_list():
    global t
    n = int(input("Number of rows:"))

    if n <= 0:
        print("The number of rows should be greater than zero")
        ordered_list()
    for i in range(1,n+1):
        st = input(f"Row #{i}:")
        t=t+f"{i}. {st}\n"
  #  t = t[:-1]
 #   print(len(t),'ddd')
  #  return f'{t}'

   

def unordered_list():
    global t
    n = int(input("Number of rows:"))
    if n <= 0:
        print("The number of rows should be greater than zero")
        unordered_list()
    for i in range(n):
        st = input(f"Row #{i}:")
        t=f"{t}* {st}\n"
 #   t=t[0:-1]
 #   print(t)
 #   return t
    
def new_line(t):
   return f'{t}\n'

def done(t):
    my_file = open('output.md','w')
    my_file.write(t)
    my_file.close()


formatters = ['plain','bold','italic','header','link','inline-code','ordered-list','unordered-list','new-line','!help','!done','ordered-list']
choose = ''
t = ''
while choose != '!done':
    choose = input("Choose a formatter:")
    if choose not in formatters:
        print("Unknown formatting type or command")
    elif choose == '!help':
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif choose == 'plain':
        t = plain(t)
        print(t)

    elif choose == 'bold':
        t = bold(t) 
        print(t)

    elif choose == 'italic':
        t = italic(t)
        print(t)

    elif choose == 'new-line':
        t = new_line(t)
        print(t)

    elif choose == 'header':
        t = header()
        print(t)

    elif choose == 'link':
        t = link(t)
        print(t)

    elif choose == 'inline-code':
        t=  inline_code(t)
        print(t)

    elif choose == 'ordered-list':
        ordered_list()
        print(t)

    elif choose == 'unordered-list':
        unordered_list()
        print(t)

#    elif choose == 'done':

done(t)
