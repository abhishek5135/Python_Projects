import random
import pywhatkit
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again plz....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def shape():
    #import turtle
    try:
        yuvi = turtle.Turtle()
        sc = turtle.Screen()
        c = ['red', 'green', 'pink', 'yellow', 'blue', 'black']
        a = len(c)
        for z in range(0, a):
            i = random.choice(c)
            yuvi.fillcolor(i)
            yuvi.begin_fill()
            yuvi.color(i)
            yuvi.circle(40)
            yuvi.forward(40)
            yuvi.end_fill()
    except Exception as e:
        print("Would not able to make shape plz try again!!!")
    return "None"


def websearch(query):
    try:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except Exception as e:
        # print(e)
        print("Say that again please...")
    return "None"


def whatsapp():
    import pywhatkit
    from datetime import datetime
    speak("When you want to send your message")
    speak("Instantly or Want to schedule")
    print("When you want to send your message:")
    print("instantly or Wnat to schedule:")
    contentt = takeCommand().lower()
    if 'instantly' in contentt:
        num = input(
            "Enter the Number to which you want to send amessage with country code:")
        speak("speak the Message:")
        message = takeCommand()
        print("Do you want to send this message yes or no")
        speak("Do you want to send this message yes or no")
        ask = takeCommand().lower()
        if 'yes' in ask:
            now = datetime.now()
            current_hour = int(now.strftime("%H"))
            min = now.strftime("%M")
            current_min = 1+int(min)
            pywhatkit.sendwhatmsg(num, message, current_hour, current_min)
        elif 'no' in ask:
            print("Message not send!!!")
            speak("Message not send")
    elif 'scheule' in contentt:
        num = input(
            "Enter the Number to which you want to send message with country code:")
        speak("speak the Message:")
        message = takeCommand()
        print("Do you want to send this message yes or no")
        speak("Do you want to send this message yes or no")
        ask = takeCommand().lower()
        if 'yes' in ask:
            num3 = int(input("Enter hours in 24 hour format"))
            num4 = int(input("Enter the minutes of hour"))
            pywhatkit.sendwhatmsg(num, message, num3, num4)
        elif 'no' in ask:
            print("Message not send!!!")
            speak("Message not send")
    else:
        print("Sorry did not get it")
        speak("Sorry did not get it")
    return "None"


def play(query):
    import pywhatkit
    try:
        pywhatkit.playonyt(query)
    except Exception as e:
        print("Would not open please try again...")
        speak("Would not open please try again")
    return "None"


def game():
    import time
    import random
    try:
        list = [1, 2]
        a = random.choice(list)
        if a == 1:
            print("*********welcome to the great snake water gun of history***********")
            speak("welcome to the great snake water gun of history")
            speak("Enter how any Turns you want to play")
            num = int(input("Enter how Turns you want to play "))
            player_1 = 0
            player_2 = 0
            listcomputer = ['snake', 'water', 'gun']
            computer = random.choice(listcomputer)
            num2 = 0
            while(num2 != num):
                print("snake", "water", "gun")
                speak("Player 1 Enter your choice from above ")
                players_inpu = input("Player 1 Enter your choice from above ")
                if players_inpu in listcomputer:
                    print(f"computer choice {computer}")
                    if(computer == 'snake' and players_inpu == 'water'):
                        player_2 += 1
                    elif (computer == 'gun' and players_inpu == 'water'):
                        player_1 += 1
                    elif(computer == 'water' and players_inpu == 'water'):
                        print("Turn draw")

                    elif(computer == 'gun' and players_inpu == 'snake'):
                        player_2 += 1
                    elif (computer == 'water' and players_inpu == 'snake'):
                        player_1 += 1
                    elif(computer == 'snake' and players_inpu == 'snake'):
                        print("Turn draw")

                    elif(computer == 'snake' and players_inpu == 'gun'):
                        player_1 += 1
                    elif (computer == 'water' and players_inpu == 'gun'):
                        player_2 += 1
                    elif(computer == 'gun' and players_inpu == 'gun'):
                        print("Turn draw")
                    num2 += 1
                else:
                    print("Enter the correct input!!!")

            if(player_1 > player_2):
                print("You are winner of This game ")
                speak("You are winner of This game ")
            elif (player_2 > player_1):
                print("You lose the game")
                print("Better luck next time")
                speak("You lose the game")
                speak("Better luck next time")
            else:
                print("Match tie")

        elif a == 2:
            import random
            import pygame
            import os

            pygame.mixer.init()
            pygame.init()

            # Colors
            white = (255, 255, 255)
            red = (255, 0, 0)
            black = (0, 0, 0)
            green = (0, 255, 0)
            blue = (0, 41, 255)

            # Creating window
            screen_width = 900
            screen_height = 600
            gameWindow = pygame.display.set_mode((screen_width, screen_height))
            bgimg = pygame.image.load("back1.jpg")
            bgimg = pygame.transform.scale(
                bgimg, (screen_width, screen_height)).convert_alpha()

            bgimg2 = pygame.image.load("back2.png")
            bgimg2 = pygame.transform.scale(
                bgimg2, (screen_width, screen_height)).convert_alpha()

            bgimg3 = pygame.image.load("back3.png")
            bgimg3 = pygame.transform.scale(
                bgimg3, (screen_width, screen_height)).convert_alpha()

            # Game Title
            pygame.display.set_caption("Snake game by MML")
            pygame.display.update()
            font = pygame.font.SysFont(None, 55)

            # Game specific variables

            def play(text, color, x, y):
                screen_text = font.render(text, True, color)
                gameWindow.blit(screen_text, [x, y])

            def plotsnake(gameWindow, color, snake_list, snake_size):
                for x, y in snake_list:
                    pygame.draw.rect(gameWindow, color, [
                                     x, y, snake_size, snake_size])

            def welcome():
                exit_game = False
                while not exit_game:
                    gameWindow.fill(white)
                    gameWindow.blit(bgimg2, (0, 0))
                    play("Welcome to snake game by MML", black, 170, 240)
                    play("Press space to Start the game", black, 190, 275)
                    play("Game control", black, 190, 400)
                    play("Right key to Start and to right", black, 50, 440)
                    play("Left key to take Left", black, 50, 480)
                    play("Down key to take Down", black, 50, 520)
                    play("Up key to take Up", black, 50, 560)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit_game = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                pygame.mixer.music.load("gamestart.mp3")
                                pygame.mixer.music.play()
                                game_loop()

                    pygame.display.update()

            # Game Loop

            def game_loop():
                pygame.mixer.music.load("gamemusic.mp3")
                pygame.mixer.music.play()
                exit_game = False
                game_over = False
                snake_x = 45
                snake_y = 55
                snake_size = 15
                food_size = 10
                fps = 60
                velocity_x = 0
                velocity_y = 0
                food_x = random.randint(20, screen_width / 1.5)
                food_y = random.randint(20, screen_height / 1.5)
                score = 0
                init_velocity = 5
                clock = pygame.time.Clock()
                snake_list = []
                snake_length = 1

                if (not os.path.exists("highscore.txt")):
                    with open("highscore.txt", "w") as f:
                        f.write("0")

                with open("highscore.txt", "r") as f:
                    hiscore = f.read()

                while not exit_game:
                    if game_over:
                        with open("highscore.txt", "w") as f:
                            f.write(str(hiscore))

                        gameWindow.fill(white)
                        gameWindow.blit(bgimg3, (0, 0))
                        play("Game over! Press Enter to continue", white, 130, 250)
                        play("Your Score:" + str(score), white, 310, 290)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    welcome()

                            if event.type == pygame.QUIT:
                                exit_game = True

                    else:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit_game = True

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                    velocity_x = init_velocity
                                    velocity_y = 0

                                if event.key == pygame.K_LEFT:
                                    velocity_x = - init_velocity
                                    velocity_y = 0

                                if event.key == pygame.K_UP:
                                    velocity_y = - init_velocity
                                    velocity_x = 0

                                if event.key == pygame.K_DOWN:
                                    velocity_y = init_velocity
                                    velocity_x = 0

                                if event.key == pygame.K_q:
                                    score += 10

                        snake_x = snake_x + velocity_x
                        snake_y = snake_y + velocity_y

                        if abs(snake_x - food_x) < 16 and abs(snake_y - food_y) < 16:
                            score += 10
                            food_x = random.randint(15, screen_width / 2)
                            food_y = random.randint(15, screen_height / 2)
                            snake_length += 5
                            if score > int(hiscore):
                                hiscore = score

                        gameWindow.fill(white)
                        gameWindow.blit(bgimg, (0, 0))
                        play("Score:" + str(score) + "Highscore:" +
                             str(hiscore), blue, 5, 15)
                        pygame.draw.rect(gameWindow, black, [
                            food_x, food_y, food_size, food_size])

                        head = []
                        head.append(snake_x)
                        head.append(snake_y)
                        snake_list.append(head)

                        if len(snake_list) > snake_length:
                            del snake_list[0]

                        if head in snake_list[:-1]:
                            pygame.mixer.music.load("gameover.mp3")
                            pygame.mixer.music.play()
                            game_over = True

                        if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                            pygame.mixer.music.load("gameover.mp3")
                            pygame.mixer.music.play()
                            game_over = True

                        plotsnake(gameWindow, red, snake_list, snake_size)
                    pygame.display.update()
                    clock.tick(fps)
                pygame.quit()
                quit()
            welcome()
            return "None"
    except Exception as e:
        print("Cannot able to open a game!!!!")
        speak("cannot able to open a game")
    return "None"


def love():
    print(
        '\n'.join
        ([
            ''.join
            ([
                (
                    'Love'[(x-y) % len('Love')]
                    if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0
                    else ' '
                ) for x in range(-30, 30)
            ])
            for y in range(30, -30, -1)
        ])
    )


def magic():
    import time
    import sys
    print("  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n  █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n  █░░║║║╠─║─║─║║║║║╠─░░█\n  █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
    Name = input("Enter your name: ")
    print("\nMAGIC IN")
    speak("magic in")
    print("3")
    speak("3")
    print("2")
    speak("2")
    print("1")
    speak("1")
    print("0")
    for n in Name:

        n = n.upper()
        if (n == "A"):
            print("    •••••••••••••••••••\n    •••••••••@•••••••••\n    •••••••@@•@@•••••••\n    •••••@@@•••@@@•••••\n    ••••@@@@@@@@@@@••••\n    •••@@@•••••••@@@•••\n    ••@@@•••••••••@@@••\n    •••••••••••••••••••\n")
        elif (n == "B"):
            print("    •••••••••••••••••••\n    ••••••@@@@@@•••••••\n    ••••••@@•••@@••••••\n    ••••••@@@@@@•••••••\n    ••••••@@•••@@••••••\n    ••••••@@@@@@•••••••\n    •••••••••••••••••••\n")
        elif (n == "C"):
            print("    •••••••••••••••••••\n    •••••••@@@@@@••••••\n    ••••••@@•••••@•••••\n    •••••@@••••••••••••\n    •••••@@••••••••••••\n    ••••••@@•••••@•••••\n    •••••••@@@@@@••••••\n    •••••••••••••••••••\n")
        elif (n == "D"):
            print("    •••••••••••••••••••\n    ••••@@@@@@@••••••••\n    ••••@@•••••@@••••••\n    ••••@@•••••••@@••••\n    ••••@@••••••••@@•••\n    ••••@@•••••••@@••••\n    ••••@@••••••@@•••••\n    ••••@@@@@@@@•••••••\n    •••••••••••••••••••\n")
        elif (n == "E"):
            print("    ••••••••••••••••••\n    •••••@@@@@@@@•••••\n    •••••@@•••••••••••\n    •••••@@@@@@•••••••\n    •••••@@•••••••••••\n    •••••@@@@@@@@•••••\n    ••••••••••••••••••\n")
        elif (n == "F"):
            print("    ••••••••••••••••••\n    •••••@@@@@@@@•••••\n    •••••@@•••••••••••\n    •••••@@@@@@•••••••\n    •••••@@•••••••••••\n    •••••@@•••••••••••\n    ••••••••••••••••••\n")
        elif (n == "G"):
            print("    ••••••••••••••••••\n    ••••••@@@@@@••••••\n    ••••@@••••••••••••\n    •••@@••••@@@@@••••\n    ••••@@•••••@@•••••\n    •••••@@@@@@•••••••\n    ••••••••••••••••••\n")
        elif (n == "H"):
            print("    •••••••••••••••••••\n    •••••@@•••••@@•••••\n    •••••@@•••••@@•••••\n    •••••@@•••••@@•••••\n    •••••@@@@@@@@@•••••\n    •••••@@•••••@@•••••\n    •••••@@•••••@@•••••\n    •••••@@•••••@@•••••\n    •••••••••••••••••••\n")
        elif (n == "I"):
            print("    ••••••••••••••••\n    ••••@@@@@@@@••••\n    •••••••@@•••••••\n    •••••••@@•••••••\n    •••••••@@•••••••\n    ••••@@@@@@@@••••\n    ••••••••••••••••\n")
        elif (n == "J"):
            print("    ••••••••••••••••\n    ••••@@@@@@@@••••\n    •••••••@@•••••••\n    •••••••@@•••••••\n    ••@@•••@@•••••••\n    ••••@@@@••••••••\n    ••••••••••••••••\n")
        elif (n == "K"):
            print("    ••••••••••••••\n    •••@@••••@@•••\n    •••@@•••@@••••\n    •••@@@@•••••••\n    •••@@•••@@••••\n    •••@@••••@@•••\n    ••••••••••••••\n")
        elif (n == "L"):
            print("    ••••••••••••••\n    •••@@•••••••••\n    •••@@•••••••••\n    •••@@•••••••••\n    •••@@•••••••••\n    •••@@@@@@@@•••\n    ••••••••••••••\n")
        elif (n == "M"):
            print("    •••••••••••••••••\n    ••@@@•••••••@@@••\n    ••@@•@•••••@•@@••\n    ••@@••@•••@••@@••\n    ••@@••••@••••@@••\n    ••@@•••••••••@@••\n    ••@@•••••••••@@••\n    •••••••••••••••••\n")
        elif (n == "N"):
            print("    ••••••••••••••••\n    ••@@@•••••••@@••\n    ••@@•@@•••••@@••\n    ••@@•••@@•••@@••\n    ••@@•••••@@•@@••\n    ••@@•••••••@@@••\n    ••••••••••••••••\n")
        elif (n == "O"):
            print("    ••••••••••••••\n    ••••@@@@@@••••\n    ••@@••••••@@••\n    •@@••••••••@@•\n    ••@@••••••@@••\n    ••••@@@@@@••••\n    ••••••••••••••\n")
        elif (n == "P"):
            print("    ••••••••••••••••\n    •••@@@@@@@@@••••\n    •••@@••••••@@•••\n    •••@@••••••@@•••\n    •••@@@@@@@@@••••\n    •••@@•••••••••••\n    •••@@•••••••••••\n    •••@@•••••••••••\n    ••••••••••••••••\n")
        elif (n == "Q"):
            print("    ••••••••••••••••\n    •••••@@@@@@•••••\n    •••@@••••••@@•••\n    ••@@••••@•••@@••\n    •••@@••••@•@@•••\n    ••••@@@@@@@@••••\n    ••••••••••••@•••\n    ••••••••••••••••\n")
        elif (n == "R"):
            print("    ••••••••••••••••\n    ••••@@@@@@@@••••\n    ••••@@•••••@@•••\n    ••••@@@@@@@@••••\n    ••••@@••••@@••••\n    ••••@@••••••@@••\n    ••••••••••••••••\n")
        elif (n == "S"):
            print("    ••••••••••••••\n    ••••@@@@@@••••\n    •••@@•••••••••\n    •••@@•••••••••\n    ••••@@@@@@••••\n    •••••••••@@•••\n    •••••••••@@•••\n    ••••@@@@@@••••\n    ••••••••••••••\n")
        elif (n == "T"):
            print("    ••••••••••••••••••\n    ••••@@@@@@@@@@••••\n    ••••@@@@@@@@@@••••\n    ••••••••@@••••••••\n    ••••••••@@••••••••\n    ••••••••@@••••••••\n    ••••••••@@••••••••\n    ••••••••••••••••••\n")
        elif (n == "U"):
            print("    •••••••••••••••••\n    •••@@•••••••@@•••\n    •••@@•••••••@@•••\n    •••@@•••••••@@•••\n    ••••@@•••••@@••••\n    •••••@@@@@@••••••\n    •••••••••••••••••\n")
        elif (n == "V"):
            print("    •••••••••••••••••••\n    •••@@•••••••••@@•••\n    ••••@@•••••••@@••••\n    •••••@@•••••@@•••••\n    ••••••@@••@@•••••••\n    ••••••••@@•••••••••\n    •••••••••••••••••••\n")
        elif (n == "W"):
            print("    •••••••••••••••••••••••••\n    ••@•••••••••@•••••••••@••\n    ••@@•••••••@@@•••••••@@••\n    •••@@•••••@@•@@•••••@@•••\n    ••••@@•••@@•••@@•••@@••••\n    •••••@@•@@•••••@@•@@•••••\n    ••••••@@@•••••••@@@••••••\n    •••••••@•••••••••@•••••••\n    •••••••••••••••••••••••••\n")
        elif (n == "X"):
            print("    •••••••••••••••••\n    ••••@@•••••@@••••\n    •••••@@•••@@•••••\n    •••••••@@@•••••••\n    ••••••••@••••••••\n    •••••••@@@•••••••\n    •••••@@•••@@•••••\n    ••••@@•••••@@••••\n    •••••••••••••••••\n")
        elif (n == "Y"):
            print("    ••••••••••••••••••\n    ••••@@••••••@@••••\n    •••••@@••••@@•••••\n    ••••••@@••@@••••••\n    ••••••••@@••••••••\n    ••••••••@@••••••••\n    ••••••••@@••••••••\n    ••••••••@@••••••••\n    ••••••••••••••••••\n")
        elif (n == "Z"):
            print("    ••••••••••••••••\n    •@@@@@@@@@@@••••\n    ••@@@@@@@@@@@•••\n    •••••••••@@@••••\n    ••••••••@@@•••••\n    •••••••@@@••••••\n    ••••••@@@•••••••\n    ••••@@@•••••••••\n    •••@@@@@@@@@@@••\n    ••@@@@@@@@@@@@@•\n    ••••••••••••••••\n")
        elif (n == " "):
            print("")

        else:
            sys.exit()
    return "None"


def covidchecker():
    import time
    re = 1
    while re:

    def ans():
        ansy = "yes", "Yes", "yEs", "yES", "YeS", "yeS", "1", "YES"
        ansn = "no", "No", "nO", "2", "NO"
        print("~"*45)
        name = input("Enter Your Name ")
        print("~"*45)
        print("Welcome "+name)
        print("")
        time.sleep(0.5)
        print("I'am Advance Coronavirus Program\nbuild with python")
        print("")
        time.sleep(0.5)
        live = input("Where are you living? ")
        time.sleep(0.5)
        print("")
        print("What is the number of infected \npeople in " + live+"?")
        print("")
        print("1 = Less than 1000\n2 = Above 1000\n3 = Higher than 10,000\n4 = Wide spread")
        case = input("Select Number : ")
        print("")
        if case == "1":
        print("You should wear a mask when going out\nkeep a distance with people\nand also wash your hands well\nafter touching surfaces")
        print("and,Do not touch your face\nuntil you wash your hands ")
        elif case == "2":
        print("Adhere to the health\nconditions to avoid infection\nto avoid the spread of the epidemic\nin a larger scale")
        print("And try not to go out to absolutely necessary")
        elif case == "3":
        print("Try to stay away from the elderly\ntake the necessary precautions and \ntreat everyone around you as infected so \nthat you can resist this pandemic")
        elif case == "4":
        print("Stay at home, and if any of the symptoms\nappear on you\nget a check-up as\nsoon as possible")
        else:
        print("Wrong Input")
        print("")
        time.sleep(1)
        print("Now, I will ask you some questions\nto know your condition")
        print("yes or no")
        print("")
        time.sleep(1)
        q1 = input("Do you suffer from a headache? ")
        time.sleep(0.5)
        q2 = input("Are you having a fever? ")
        time.sleep(0.5)
        q3 = input("Do you have a dry cough / sneeze? ")
        time.sleep(0.5)
        q4 = input("Do you have a sore throat? ")
        print("")
        print("If you find the results have completed at\nleast 30%, take a Covid 19 test")
        print("")
        time.sleep(1)
        q5 = input("Finally,Do you have all the \nsymptoms I mentioned earlier? ")
        print("")
        time.sleep(0.5)
        if q1 in ansy:
        print("Q1 : Result / Risk : 10%")
        elif q1 in ansn:
        print("Q1 : No Risk")
        else:
        print("Wrong Input")
        time.sleep(0.5)
        if q2 in ansy:
        print("Q2 : Result / Risk : 20%")
        elif q2 in ansn:
        print("Q2 : No Risk")
        else:
        print("Wrong Input")
        time.sleep(0.5)
        if q3 in ansy:
        print("Q3 : Result / Risk : 40%")
        elif q3 in ansn:
        print("Q3 : No Risk")
        else:
        print("Wrong Input")
        time.sleep(0.5)
        if q4 in ansy:
        print("Q4 : Result / Risk : 30%")
        elif q4 in ansn:
        print("Q4 : No Risk")
        else:
        print("Wrong Input")
        time.sleep(0.5)
        print("")
        if q5 in ansy:
        print("Go to the hospital as soon as\npossible for a Covid 19 test\nas per your entries")
        elif q5 in ansn:
        print("Q5 : Good")
        else:
        print("Wrong Input")
        print("")
        ans()
        re = int(input("Enter 1 to Restart Programe or 0 To Stop it "))


def dice():
    print("This is dice stimulator")
    x = "y"
    while x == "y":
    number = random.randint(1, 6)

    if number == 1:
        print("----------")
        print("|        |")
        print("|   o    |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| o   o  |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|   o    |")
        print("|   o    |")
        print("|   o    |")
        print("----------")
    if number == 4:
        print("----------")
        print("| o   o  |")
        print("|        |")
        print("| o   o  |")
        print("----------")

    if number == 5:
        print("----------")
        print("| o   o  |")
        print("|   o    |")
        print("| o   o  |")
        print("----------")

    if number == 6:
        print("----------")
        print("| o   o  |")
        print("| o   o  |")
        print("| o   o  |")
        print("----------")
    x = input("press y to roll again")


def internetspeed():
    import speedtest
    st = speedtest.Speedtest()
    print("Download speed")
    print(st.download(), "mbps")
    print("Upload speed")
    print(st.upload(), "mbps")
    servernames = []
    st.get_servers(servernames)
    print("Ping")
    print(st.results.ping, "ms")


def second_old():
    print(" what is your age ? ")
    age = input()
    print(" According to your age ::")
    print(" you are " + str(int(age) * 12) + (" months old. "))

    print(" you are " + str(int(age) * 12*31) + (" days old  "))

    print(" you are " + str(int(age) * 12*31*24) + (" hours old "))

    print(" you are " + str(int(age) * 12*31*24*60) + (" minutes old  "))

    print(" you are " + str(int(age)*12*31*24*60*60) + (" seconds old  "))

    print("how awesome it is when you got to know how many seconds you old are . ")
    print(" bye , and have a good day ☺ .")


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            websearch(query)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'whatsapp' in query:
            whatsapp()

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'play' in query:
            if 'game' in query:
                game()
            else:
                play(query)
        elif 'make a shape' in query:
            shape()
        elif 'none' in query:
            print("Try asking something......")
        elif 'calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        elif 'notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        elif 'wordpad' in query:
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
        elif 'browser' in query:
            subprocess.Popen(
                'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
        elif 'alarm' in query:
            pass
        elif 'do magic' in query:
            magic()
        elif 'old' in query:
            second_old()
        elif 'i love you' in query:
            love()
        elif 'speed test' in query:
            internetspeed()
        elif 'throw a dice' in query:
            dice()
        elif 'take my covid test' in query:
            covidchecker()
        else:
            import pywhatkit
            pywhatkit.search(query)
