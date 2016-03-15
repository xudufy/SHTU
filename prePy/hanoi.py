def hanoi(*haha):
    if int(haha[0])==1:
        print(haha[1],'->',haha[2],end='')
        for i in haha[3:]:
            print(i,sep='',end='')
    else:
        hanoi(int(haha[0])-1,haha[1],chr(294-ord(haha[1])-ord(haha[2])),haha[3:])
        print(haha[1],'->',haha[2],end='')
        for i in haha[3:]:
            print(i,sep='',end='')
        hanoi(int(haha[0])-1,chr(294-ord(haha[1])-ord(haha[2])),haha[2],haha[3:])

hanoi('5','a','b','shit')
