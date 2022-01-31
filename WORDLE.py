f = open("words.txt")
arr = [i.strip('\n') for i in f if len(i) == 6]
res = arr.copy()
print("_____________________________________________________")
print(""" __      __________ __________________  .____     ___________ 
/  \    /  \_____  \\______   \______ \  |    |    \_   _____/ 
\   \/\/   //   |   \|       _/|    |  \|    |     |    __)_  
 \        //    |    \    |   \|    `   \    |___  |        \ 
  \__/\  / \_______  /____|_  /_______  /_______ \/_______  / 
       \/          \/       \/        \/        \/        \/  
       """)
print("_____________________________________________________")
print("List:  A B C D E")
print("Index: 1 2 3 4 5")
while 1:
    print("--------------------")
    print("1. Char not in list")
    print("2. Char in list but wrong place")
    print("3. Char in list and in right place")
    print("0. Get result")
    print("--------------------")
    mode = int(input()[0])
    if mode == 1:
        a = input("Input the char")[0]
        res = [x for x in res if a not in x and a.upper() not in x]
    if mode == 2:
        userInput = input("Input the char and index (EX:a 3)")
        character = userInput[0]
        index = int(userInput[2])
        if(index == 0):
            print("please try again")
            continue
        res = [x for x in res if x[index - 1] != character and x[index - 1] != character.upper()]
    if mode == 3:
        userInput = input("Input the char and index (EX:a 3)")
        character = userInput[0]
        index = int(userInput[2])
        if(index == 0):
            print("please try again")
            continue
        res = [x for x in res if x[index - 1] == character or x[index - 1] == character.upper()]
    if mode == 0:
        print("--------------------")
        print(res)
        print("--------------------")



