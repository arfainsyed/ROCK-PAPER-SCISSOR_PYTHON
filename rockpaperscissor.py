import random
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("*       *PAPER * ROCK * SCISSOR          *")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("Lets start the game!!....")
point=0
ai=0
hs=0
cs=0
ma=0
while(True):
    if(ma>5):
        print("##############################")
        print("Total Match:",ma)
        print("Human Score:",hs)
        print("AI Score:",cs)
        if(hs>cs):
            print("Congrats you won")
        elif(cs>hs):
            print("AI won....Better luck next time")
        else:
            print("MATCH DRAW")
        Print("##############################")
        break
    c=input("Choose Paper->p Rock->r Scissor->s Stop->stop:")
    if(c=="p"):
        print("paper")
        point=10+random.randint(1,3)
        match point:
            case 11:
                ma=ma+1
                hs=hs+1
                print("Human: paper","AI: Rock")
                print("Match:",ma,"Human Score:",hs, "AI Score:",cs)
                print("Human: win","AI:lost")
                print("_________")
                
            case 12:
                ma=ma+1
                cs=cs+1
                print("Human: Paper","AI: scissor")
                print("Match:",ma,"Human Score:",hs, "AI Score:",cs)
                print("Human:lost","AI: win")
                print("________")
            case 13:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("Human: Paper","AI: Paper")
                print("Match:",ma,"Human Score:",hs, "AI Score:",cs)
                print("Match Draw")
                print("_________")
    elif(c=="r"):
        print("rock")
        point=20+random.randint(1,3)
        match point:
            case 21:
                ma=ma+1
                print("Human: Rock","AI: Scissor")
                print("Match:",ma,"Human Score:",hs, "AI Score:",cs)
                print("Human: win","AI:lost")
                print("_________")
            case 22:
                ma=ma+1
                print("Human: Rock","AI: Paper")
                print("Match:",ma,"Human Score:",hs, "AI Score:",cs)
                print("Human: lost","AI: won")
                print("________")
            case 23:
                ma=ma+1
                print("Human: Rock","AI: Rock")
                print("Match:",ma,"Human Score:",hs, "AI Score:",cs)
                print("Match Draw")
                print("_________")
    elif(c=="s"):
        print("scissor")
        point=30+random.randint(1,3)
        match point:
            case 31:
                ma=ma+1
                print("Human: Scissor","AI: Paper")
                print("Match:",ma,"Human Score:",hs, "AI Score:",cs)
                print("Human: win","AI:win")
                print("_________")
            case 32:
                ma=ma+1
                print("Human: Scissor","AI: Rock")
                print("Match:",ma,"Human Score:",hs, "AI Score:",cs)
                print("Human: lost","AI: win")
                print("________")
            case 33:
                ma=ma+1
                print("Human: Scissor","AI: Scissor")
                print("Match:",ma,"Human Score:",hs, "AI Score:",cs)
                print("Match Draw")
                print("_________")