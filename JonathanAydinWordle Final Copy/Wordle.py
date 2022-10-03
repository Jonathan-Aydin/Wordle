from graphics import *
import random
from time import gmtime, strftime
#from playsound import playsound
#from pydub import AudioSegment
#from pydub.playback import play





#import simpleaudio as sa
#from simpleaudio.shiny import simpleaudio as sa

##scoring system to implemet: (1,000,000 - 142857.142857*guesses)/seconds

def quicksort(array):
     # If the input array contains fewer than two elements,
     # then return it as the result of the function
    if len(array) < 2:
         return array
 
    low, same, high = [], [], []
    # Select your `pivot` element randomly
    pivot = array[random.randrange( len(array) - 1)]

    for item in array:
        #print(float(item[0:item.index(";")-1]))
        #print(float(pivot[0:pivot.index(";")-1]))
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if float(item[0:item.index("\<by>/")-1]) < float(pivot[0:pivot.index("\<by>/")-1]):
            low.append(item)
        elif float(item[0:item.index("\<by>/")-1]) ==  float(pivot[0:pivot.index("\<by>/")-1]):
            same.append(item)
        elif float(item[0:item.index("\<by>/")-1]) > float(pivot[0:pivot.index("\<by>/")-1]):
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)
#import sys
#sys.path.append('/Users/M.Boy/opt/anaconda3/lib/python3.8/site-packages/keyboard/__init__.py') 
#from pynput import keyboard

##idea make a text file and print to it how many guesses they did it in and the date and the score
## will eb based off number of guesses until answer, number of attempts, and time?

window = GraphWin("Wordle", 800  ,975)
window.setBackground((color_rgb(30,30,30)))

#sa.LeftRightCheck.run()


start = Text(Point(400,475),"Initializing...")
start.setTextColor("white")
start.setFace('courier')
start.setStyle("bold")
start.setSize(36)
start.draw(window)

## THIS IS WHERE READ FILE WILL EXIST
with open ("/Users/M.Boy/Desktop/Python/JonathanAydinWordle Final Copy/allowed-guesses.txt", 'r') as file:
    allowedGuesses = []
    for readline in file: 
            line_strip = readline.strip()
           # newline_break += line_strip
            allowedGuesses.append(line_strip)
    #print(allowedGuesses)


with open ("/Users/M.Boy/Desktop/Python/JonathanAydinWordle Final Copy/answers.txt", 'r') as file:
    answers = []
    for readline in file: 
            line_strip = readline.strip()
           
            answers.append(line_strip)
    #print(answers)
answer= answers[random.randrange(2314)]
#print(answer)

#answer = "forgo"




letters = 'qwertyuiop\nasdfghjkl\nzxcvbnm'
#print(letters)
#print("\n\n\n")


start.undraw()

bob = Text(Point(400,25), "Utterance-le")
bob.setFace('courier')
bob.setStyle("bold")
bob.setSize(36)
bob.setTextColor("white")
bob.draw(window)

timer = Text(Point(675,25), "")
timer.setFace('courier')
timer.setStyle("bold")
timer.setSize(18)
timer.setTextColor(color_rgb(84, 227, 84))
timer.draw(window)


lin = Line(Point(100,50), Point(700,50))
lin.setOutline(color_rgb(101,101,101))
lin.draw(window)

#the following code is for generating boxes
sideGap = 111.5
startx = sideGap ;
starty = 75;
dimens = 110

square = []

rows, cols = (6, 5)

for x in range(6):
    col = []
    for z in range(5):
        col.append( (Rectangle( Point(startx,starty), Point(dimens + startx, dimens + starty)) ) )
        col[z].setOutline(color_rgb(81,81,81))
        col[z].draw(window)

        
        startx = startx + 6.75 +dimens
    square.append(col)
    startx = sideGap
    starty = starty + 6.75 + dimens

lin = Line( Point(100,793.75), Point(700,793.75))
lin.setOutline(color_rgb(101,101,101))
lin.draw(window)

enter = Entry( Point(400, 843.75 ), 7)
enter.setFill(color_rgb(81,81,81))
#enter.setText("courier")
enter.setStyle("bold")
enter.setSize(36)
enter.draw(window)

#for x in range(0,3)
lettext = Text (Point(150,863.75), letters)
lettext.setFace('courier')
lettext.setStyle("bold")
lettext.setSize(36)
lettext.setTextColor(color_rgb(84, 227, 84))
lettext.draw(window)

win = Text(Point(400,951.875), "Congratulations! You beat Utterance-le!")
win.setFace('courier')
win.setStyle("bold")
win.setSize(32)
win.setTextColor(color_rgb(84, 227, 84))

lose = Text(Point(400,925.875), "RATS! Try again next time! \n Answer was: " + answer)
lose.setFace('courier')
lose.setStyle("bold")
lose.setSize(32)
lose.setTextColor("red")

#don't draw until game is won
#win.draw(window)



x1 = 600
y1 = 843.75
x2 = 700
y2 = 893.75

button = Rectangle(Point(x1, y1), Point(x2,y2))
button.setFill(color_rgb(81,81,81))
button.draw(window)

tbut = Text(Point( ( ( x1 + x2) / 2) , (( y1 + y2) / 2)), "Enter")
tbut.setFace('courier')
tbut.setStyle("bold")
tbut.setSize(18)
tbut.setTextColor(color_rgb(84, 227, 84))
tbut.draw(window)


guesslist = []
countguess = 0
track = 0
faults = 0

starttime = time.time()



#enter.setText(answer)

while True:

    bob = window.checkMouse()
    bob2 = window.checkKey()
    timer.setText("Time Elapsed: " + str((round((time.time() - starttime), 1))))
    window.update()
    
    
    if( (bob != None) or (bob2 == "Return")):
        
        if((bob2 == "Return") or (x1 < bob.getX() and x2> bob.getX() and y1 < bob.getY() and y2 > bob.getY())  ):
            #print("works")
            guess = enter.getText()
            guess = guess.lower()
            guesstime = (round((time.time() - starttime), 4))
            
            if(len(guess) == 5 and (guess in allowedGuesses)):
                #print(guess)

                ansOccurences = []
                ansLetterIndex = []
                for i in range (0,5):
                
                        ansOccurences.insert(i, 0);
                        ansLetterIndex.insert(i, []);
                        
                        for j in range (0,5):
                        
                                if(answer[i:i+1]==answer[j:j+1]):
                                
                                        ansOccurences[i] = ansOccurences[i] + 1
                                
                                if(guess[i:i+1].lower()==answer[j:j+1].lower()):
                                
                                        ansLetterIndex[i].append(j)
                                
                
                output = []
                #print("ansLetterIndex is: ")
                #print(ansLetterIndex)
                for i in range(0,5):
                
                        added = False
                        if(guess[i:i+1].lower()==answer[i:i+1]):
                        
                                output.insert(i,"green")
                                added = True
                                for j in range(0,len(ansLetterIndex[i])):
                                
                                        ansOccurences[ansLetterIndex[i][j]] = ansOccurences[ansLetterIndex[i][j]] -1;
                                
                        
                        if(not added):
                        
                                #outer:
                                for j in range (0,5):
                                
                                        if(guess[i:i+1].lower()==answer[j:j+1]):
                                        
                                                output.insert(i, "yellow");
                                                added = True;
                                                break 
                                        
                                
                        
                        if(not added):
                        
                                output.insert(i , "grey")
                        
                
                for i in range(0,5):
                
                        if(output[i]=="yellow"):
                        
                                if(ansOccurences[ansLetterIndex[i][0]]==0):
                                
                                        output.pop(i)
                                        output.insert(i,"grey")
                                
                                else:
                                
                                        for j in range (0,len(ansLetterIndex[i])):
                                        
                                                ansOccurences[ansLetterIndex[i][j]] = ansOccurences[ansLetterIndex[i][j]] -1;
                                        
                                
                        
                
                
                
                
                for x in guess:
                    guesslist.append(x)
                #print( guesslist)

                ans2 = answer
                
                ij = -1
                for y in guess:
                    ij = ij + 1
                    
                    tguess = Text(Point(166.5 + track*116.75, 130 + 116.75*countguess ), y.upper())
                    tguess.setFace('courier')
                    tguess.setStyle("bold")
                    tguess.setSize(36)
                    tguess.setTextColor("white")
                    tguess.draw(window)

                    

                    if(output[ij] == "green"):
                            square[countguess][track].setFill("green")
                    elif(output[ij] == 'yellow'):
                            square[countguess][track].setFill(color_rgb(255,205,0))
                    else:
                       if y in letters:
                            letters = letters.replace(y, "")
                            
                       lettext.undraw()
                       lettext.setText(letters)
                       lettext.draw(window)
                       window.update()



                    
                    
                    
                    track = track + 1
                    ans2 = ans2.replace(y,"",1)
                    #print("ans2: " + ans2)
                    
                    
                    time.sleep(0.5)
                track = 0
                countguess = countguess+ 1
                guesslist = []
                enter.setText("")
              

                #print(letters)

                if(guess == answer):
                    finaltime = guesstime
                    break
                if(countguess==6):
                    break

            
            else:
                faults = faults + 1
                enter.setFill("red")
                window.update()
                time.sleep(0.2)
                enter.setFill(color_rgb(81,81,81))
                
            #print("Available letters include: " + letters)
           
                


lettext.undraw()
if(guess == answer):
        #print(str(finaltime) + ' guesses = ' + str(countguess) + ' faults = ' + str(faults))
        finalscore = round((1000000 -  142857*(countguess))/( finaltime + 0.5*faults),4)
        #print(finalscore)
        
        win.draw(window)
        
        scoreboard = GraphWin("Winner's Sirkle", 600  ,850)
        scoreboard.setBackground((color_rgb(135,206,235)))
        

        texte = Text(Point(300, 250), "Wiener! Please Enter Your Name: ")
        texte.setFill(color_rgb(32,42,64))
        texte.setFace("courier")
        texte.setStyle("bold")
        texte.setSize(28)
        texte.draw(scoreboard)
        
        enter = Entry( Point(300, 385 ), 10)
        enter.setFill(color_rgb(32,42,64))
        
        enter.setTextColor("white")
        enter.setStyle("bold")
        enter.setSize(36)
        enter.draw(scoreboard)

        texte2 = Text(Point(300, 450), "Name must be less than 18 characters!")
        texte2.setFill("red")
        texte2.setFace("courier")
        texte2.setStyle("bold")
        texte2.setSize(16)

        
        while(True):
            enter.setFill(color_rgb(32,42,64))
            joe = scoreboard.getKey()
            while(joe != "Return"):
                    joe = scoreboard.getKey()
            
            namer = enter.getText()
            if(len(namer) >17):
                enter.setFill("red")

                
                texte2.draw(scoreboard)
                enter.setText("")
        
            else:
                break
            
            
        texte.undraw()
        texte2.undraw()
        enter.undraw()

        #playsound("song.m4a")
        
        os.environ['TZ'] = 'PST+08EDT,M4.1.0,M10.5.0'
        time.tzset()


        #print(str(finalscore) + ' by ' + namer + ' answered: "' + answer + '" in ' + str(countguess) + ' guesses after ' + str(finaltime) + ' seconds on ' + str(time.strftime('%a, %b %d %Y at %X %Z')) + '\n')
        with open("/Users/M.Boy/Desktop/Python/JonathanAydinWordle/scores.txt", 'a') as f:
            joe = str(finalscore) + '\<by>/ {\p}' + namer + ' answered: {\p}"' + answer + '" in <^!^>' + str(countguess) + '<^?^> guesses {\p}after ' + str(finaltime) + ' seconds {\p}on ' + str(time.strftime('%a, %b %d %Y {\p}at %X %Z')) + '\n'
            f.write(joe)

        bob = str(finalscore) + '\<by>/ {\p}' + namer + ' answered: {\p}"' + answer + '" in <^!^>' + str(countguess) + '<^?^> guesses {\p}after ' + str(finaltime) + ' seconds {\p}on ' + str(time.strftime('%a, %b %d %Y {\p}at %X %Z'))
        with open ("/Users/M.Boy/Desktop/Python/JonathanAydinWordle/scores.txt", 'r') as file:
            scorelist = []
            for readline in file: 
                    line_strip = readline.strip()
           # newline_break += line_strip
                    scorelist.append(line_strip)
            #print(scorelist)
        
        scorelist2 = []
        for z in scorelist:
            
            if(int(z[z.index("<^!^>") +5 : z.index("<^?^>") ]) == countguess):
                scorelist2.append(z)
                #print(z)
        
        scorelist = quicksort(scorelist)
        scorelist2 = quicksort(scorelist2)
        
        #print(scorelist2)        
        #print(scorelist)
        
        scoreboard2 = GraphWin("André's Dragons", 600  ,850)
        scoreboard2.setBackground((color_rgb(157,157,252)))

        midT2 = Text(Point(300,50), "Scoreboard of " +str(countguess) + " Guesses")
        midT2.setFace('courier')
        midT2.setStyle("bold")
        midT2.setSize(36)
        #midT.setOutline(color_rgb(135,206,235))
        midT2.setTextColor(color_rgb(255,215,0))
        midT2.draw(scoreboard2)

        
        midT = Text(Point(300,50), "Scoreboard of the Elite")
        midT.setFace('courier')
        midT.setStyle("bold")
        midT.setSize(36)
        #midT.setOutline(color_rgb(135,206,235))
        midT.setTextColor(color_rgb(255,215,0))
        midT.draw(scoreboard)

        placer = Text(Point(300,115), "You scored: " + str(finalscore) + " points and ranked: " + str(len(scorelist) - scorelist.index(bob)) + "th!")
        placer.setFace("courier")
        placer.setStyle("bold")
        placer.setSize(20)
        placer.setTextColor("red")
        placer.draw(scoreboard)

        placer2 = Text(Point(300,115), "You scored: " + str(finalscore) + " points and ranked: " + str(len(scorelist) - scorelist.index(bob)) + "th \n in the " + str(countguess) + " guesses category!")
        placer2.setFace("courier")
        placer2.setStyle("bold")
        placer2.setSize(20)
        placer2.setTextColor("red")
        placer2.draw(scoreboard2)
        
        lin = Line(Point(100,75), Point(500,75))
        lin.setOutline(color_rgb(255,215,0))
        lin.draw(scoreboard)

        lin2 = Line(Point(100,75), Point(500,75))
        lin2.setOutline(color_rgb(255,215,0))
        lin2.draw(scoreboard2)

        vertline = Line(Point(300, 150), Point(300,775))
        vertline.setWidth(4)
        vertline.setFill(color_rgb(32,42,68))
        vertline.draw(scoreboard)

        vertline2 = Line(Point(300, 150), Point(300,775))
        vertline2.setWidth(4)
        vertline2.setFill(color_rgb(32,42,68))
        vertline2.draw(scoreboard2)

        for x in range(1,3):
                for c in range(1,6):

                        if(len(scorelist)-c-(x-1)*5 <0):
                                break
                        
                        num = Text(Point(25 + (315*(x-1)),175 + 130*(c-1) ), str(c + (x-1)*5) + '.' )
                        num.setFace("courier")
                        num.setStyle("bold")
                        num.setSize(36)
                        num.setTextColor(color_rgb(32,42,68))
                        num.draw(scoreboard)

                        if(x==1 and c<=4):
                            horizline = Line(Point(50,285 + 130*(c-1)), Point(550, 285 + 130*(c-1)))
                            horizline.setWidth(3)
                            horizline.setFill(color_rgb(32,42,68))
                            horizline.draw(scoreboard)
                        
                                
                        
                        string = str(scorelist[len(scorelist)-c-(x-1)*5]).replace("{\p}", "\n")
                        string = string.replace("\<by>/", " points")
                        string = string.replace("<^!^>", "")
                        string = string.replace("<^?^>", "")
                                                
                        label = Text(Point(160 + (300*(x-1)),220 + 130*(c-1) ), string)
                        label.setFace("courier")

                        label.setSize(18)

                        label.draw(scoreboard)

                        if(c+(x-1)*5 == 1 or c+(x-1)*5 == 2 or c+(x-1)*5 == 3 ):
                            num.setTextColor(color_rgb(255,215,0))

        for x in range(1,3):
            for c in range(1,6):

                    if(len(scorelist2)-c-(x-1)*5 <0):
                            break
                    
                    num2 = Text(Point(25 + (315*(x-1)),175 + 130*(c-1) ), str(c + (x-1)*5) + '.' )
                    num2.setFace("courier")
                    num2.setStyle("bold")
                    num2.setSize(36)
                    num2.setTextColor(color_rgb(32,42,68))
                    num2.draw(scoreboard2)

                    if(x==1 and c<=4):
                        horizline2 = Line(Point(50,285 + 130*(c-1)), Point(550, 285 + 130*(c-1)))
                        horizline2.setWidth(3)
                        horizline2.setFill(color_rgb(32,42,68))
                        horizline2.draw(scoreboard2)
                    
                            
                    string = str(scorelist2[len(scorelist2)-c-(x-1)*5]).replace("{\p}", "\n")
                    string = string.replace("\<by>/", " points")
                    string = string.replace("<^!^>", "")
                    string = string.replace("<^?^>", "")
                    
                                        
                    label2 = Text(Point(160 + (300*(x-1)),220 + 130*(c-1) ), string)
                    label2.setFace("courier")
                    label2.setSize(18)
                    label2.draw(scoreboard2)

                    if(c+(x-1)*5 == 1 or c+(x-1)*5 == 2 or c+(x-1)*5 == 3 ):
                        num2.setTextColor(color_rgb(255,215,0))


                       
else:
    lose.draw(window)
window.getKey()
    


