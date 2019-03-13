import random
turn=0
board=[0,1,2,
       3,4,5,
       6,7,8]
def show():
    print (board[0],'|',board[1],'|',board[2])
    print ('---------')
    print (board[3],'|',board[4],'|',board[5])
    print ('---------')
    print (board[6],'|',board[7],'|',board[8])

def winners():
     if turn==9:
         print("draw")
         if (board[0]==board[1] and board[1]==board[2])or (board[3]==board[4] and board[4]==board[5] )or (board[6]==board[7] and board[7]==board[8]) or  (board[0]==board[3] and board[3]==board[6]) or  (board[1]==board[4] and board[4]==board[7])or  (board[2]==board[5] and board[5]==board[8]) or (board[0]==board[4] and board[4]==board[8]) or ( board[2]==board[4] and board[4]==board[6]):
              if turn%2==0:
                 print('o wins')
              elif turn%2==1:
                 print('x wins')
        
while turn <9:
     show()
     
     input1= input("select a spot:")
     print(input1)
     if board[int(input1)] != 'x' and board[int(input1)] !='o':
        board[int(input1)] = 'x'
        turn+=1
        show()
        print('\n')
        winners()
     input2= input("select a spot:")
     print(input2)
     if board[int(input2)] != 'x' and board[int(input2)] !='o':
        board[int(input2)] = 'o'
        turn+=1
        show()
        print('\n')

        winners()
        
        
                
   


