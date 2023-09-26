import random
import os
def init2():
    B=[]
    Dim = int(input("Enter the Dimension of Game: "))
    for r in range(0,Dim):
        arow=[]
        for c in range(0,Dim):
            arow.append('-')
        B.append(arow)
    
    Sym=[]
    PNames=[]
    for i in range(0,2):
        PNames.append(input(f"Player {i+1}'s Name: "))
        Sym.append(input(f"Player {i+1}'s Symbol: "))    

    return B,Dim,Sym,PNames

def init():
    B=[]
    Dim=int(input("Dim: "))
    NOP=int(input("NOP: "))
    for r in range(0,Dim):
        arow=[]
        for c in range(0,Dim):
            arow.append('-')
        B.append(arow)
    
    
    Sym=[]
    PNames=[]
    for i in range(0,NOP):
        PNames.append(input(f"Player {i+1}'s Name: "))
        Sym.append(input(f"Player {i+1}'s Symbol: "))    

    Turn=random.randint(0,NOP-1)
    return B,Dim,NOP,Sym,PNames,Turn
    



def PrintBoard(B,dim):
    os.system('cls')
    for r in range(0,dim):
        for c in range(0,dim):
            print(B[r][c],end="")
        print()


def TurnMsg(msg):
    print(f"{msg}'s Turn: ")


def SelectPosition(Dim):
    pr=int(input(f"Select Row(1...{Dim}): "))
    pc=int(input(f"Select Col(1...{Dim}): "))
    pr-=1
    pc-=1
    return pr,pc


def IsValid(pr,pc,Dim,B):
    if pr<0 or pr>Dim-1 or pc<0  or pc>Dim-1 or (B[pr][pc] != '-'):
        return False
   
    return True

def PlaceMove(B,pr,pc,aiksym):
    B[pr][pc]=aiksym




def IsLeftDiagonal(B, Dim, wincount, r, c, sym):
    count = 0
    if (c+wincount>Dim) or (r+wincount>Dim):
       return False
    for i in range(wincount):
        if B[r + i][c + i] == sym:
            count += 1
        if B[r + i][c + i] != sym:
            count == 0
    if count == wincount:
        return True
    return False


def IsRightDiagonal(B, Dim, wincount, ri, ci, Sym):
    if (ci-wincount<0) or (ri+wincount>Dim):
       return False
    count = 0
    for i in range(wincount):
        if B[ri + i][ci - i] == Sym:
            count += 1
    if count == wincount:
        return True
    return False


def IsHorizontal(B, Dim, wincount, r, c, sym):
    if  (c + wincount > Dim):
        return False;
    count = 0
    for i in range(0,wincount):
        if (B[r][c + i] == sym):
            count += 1
            
    if (count == wincount):
            return True
    else:    
       return False

def IsVertical(B, Dim, wincount, r, c, sym):
    if  (r + wincount > Dim):
        return False;
    count = 0
    for i in range(0,wincount):
        if B[r+i][c] == sym:
            count += 1
            
        if count == wincount:
            return True
    return False



def IsWin(B, Dim, wincount, Sym):
    for ri in range(Dim):
        for ci in range(Dim):
            if  IsHorizontal(B, Dim, wincount, ri, ci, Sym):
                return True
            elif  IsVertical(B, Dim, wincount, ri, ci, Sym):
                return True
            elif IsRightDiagonal(B, Dim, wincount, ri, ci, Sym):
                return True
            elif IsLeftDiagonal(B, Dim, wincount, ri, ci, Sym):
                return True
    return False



def IsDraw(B, Dim):
    for r in range(0,Dim):
        for c in range(0,Dim):
            if B[r][c] == '-':
                return True
    return False



def ComputerMove(B, Dim,Sym, wincount):
    for ri in range(Dim):
        for ci in range(Dim):
            pr=ri
            pc=ci
            if IsValid(pr, pc, Dim, B):
                B[ri][ci] = Sym[0]
                if IsWin(B, Dim, wincount, Sym[0]):
                    B[ri][ci] = '-'
                    return pr,pc
                B[ri][ci] = '-'
                
    for ri in range(Dim):
         for ci in range(Dim):
             pr=ri
             pc=ci
             if IsValid(pr, pc, Dim, B):
                 B[ri][ci] = Sym[1]
                 if IsWin(B, Dim, wincount, Sym[1]):
                     B[ri][ci] = '-'
                     return pr,pc
                 B[ri][ci] = '-'
            
    
    r=0
    c=0
    while not IsValid(r, c, Dim, B):
        r = random.randint(0, Dim-1)
        c = random.randint(0, Dim-1)
    return r,c



def TurnChange(Turn,NOP):
    Turn=(Turn+1)%2
    return Turn
    















                      #   H VS C
#-------------------------------------------------------------------#

def main2():    
    B,Dim,Sym,PNames = init2()
    wincount = int(input("Enter the count for Win: "))
    
    Turn = random.randint(0,1)
    PrintBoard(B,Dim)
    win=False
    draw=True
    
    while win==False:
           print()
           TurnMsg(PNames[Turn])
           print()
           if Turn==0:
               while True:
                   pr,pc=SelectPosition(Dim);
                   if IsValid(pr, pc, Dim,B):
                       PlaceMove(B,pr,pc,Sym[Turn])
                       break
                   else:
                       print("Wrong Input...! Kindly Enter the Correct Row and Col")
                    
           else:
               pr,pc=ComputerMove(B, Dim,Sym, wincount)
               PlaceMove(B,pr,pc,Sym[Turn])
            
           PrintBoard(B,Dim) 
           win = IsWin(B, Dim,wincount,Sym[Turn])
           if win == True:
                print("Congratulations!!!......" + PNames[Turn] + "!! You won the Game ")
           draw = IsDraw(B, Dim)
           if draw == False:
                print("Game is Drawn")
                break
        
           Turn=TurnChange(Turn,2)          
                   
            
        
#------------------------------------------------------------------------#              
        
    
    
                                # H VS H
#------------------------------------------------------------------------#
def main1():
  
    B,Dim,NOP,Sym,PNames,Turn= init()
    wincount=int(input("How many count you want for win: "))
    PrintBoard(B,Dim)
    win=False;
    draw=True
    while(win==False):
        TurnMsg(PNames[Turn])
        while True:
            pr,pc=SelectPosition(Dim)
            if IsValid(pr, pc, Dim,B):
                break
            else:
                print("Wrong Input...! Kindly Enter the Correct Row and Col")
        PlaceMove(B,pr,pc,Sym[Turn])
        PrintBoard(B,Dim)
        win = IsWin(B, Dim,wincount, Sym[Turn])
        if win == True:
            print("Congratulations!!!......" + PNames[Turn] + "!! You won the Game ")
        draw = IsDraw(B, Dim)
        if draw == False:
            print("Game is Drawn")
            break
    
        Turn=TurnChange(Turn,NOP)
    
#------------------------------------------------------------------------#    
    
    
    
N=0
print("______________________________Gomuku____________________________")
print()
print("1. For Human vs Human")
print()
print("2. For Human vs Computer ")

N=input("Enter your choice: ")
N=int(N)

if (N==1):
    main1()
if (N==2):
    main2()
    
    
    
    
    
    
    