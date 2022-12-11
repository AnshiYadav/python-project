print('PROGRAM TO PRINT TABLE UPTO SENTINEL NUMBER N')

while True:
    sen=int(input('Enter sentinel number: '))
    print()
    for i in range(2,sen+1):
        print('Table of:',i)
        
        a=1
        for j in range(i,(i*10)+1,i):
            print(i,'x',a,'=',j)
            a=a+1
        print()
    again=input('Do you want to continue??(Y/N): ')
    if again=='Y' or again=='y':
        continue
    else:
        break

    
