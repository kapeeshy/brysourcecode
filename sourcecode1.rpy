# The script of the game goes in this file.
# Works with Ren'py, not Python.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Barry")
define y = Character("You")
define n = Character("Narrator")
define m = Character("???")
define w = Character("Warning")
define c = Character("Unkown Caller")
define d = Character("Train Driver")

image barry = "barry.png"
image bg train = "bg-train.jpg"
image bg intro = "bg-intro.jpg"
image bg train 2 = "bg-train2.png"
image bg train 3 = "bg-train3.png"
image bg train 4 = "bg-train4.png"
image bg train 5 = "bg-train5.png"
image bg bedroom = "bg-bedroom.jpg"
image bg street = "street.jpg"
image bg station = "bg-station.png"
image dinner 1 = "dinner1.png"
image dinner 2 = "dinner2.png"
image dinner 3 = "dinner3.png"
image dinner 4 = "dinner4.png"
image dinner 5 = "dinner5.png"
image dark room = "dark-room.png"

#Resize the background images to 1280 x 720

# The game starts here.

label start:

    scene bg intro

    w "Warning! This is a joke game made for fun, and"
    w"contains various cuss words that may not be suitable"
    w"for all ages. Proceed at your own risk and will."

    n "Once upon a time..."
    n"There was a man named Barry."
    n"On this specific day at this specific time,"
    n"Barry was going to find the love of his life."
    n"Will Barry be able to earn his love?"
    n"Find out in this shit show of a game!"

    scene bg train

    y "I am on the subway train."
    y"My stop is in about 30 minutes."

    scene bg train 2

    "You notice a beautiful man on the train next to you,"
    "and you begin to blush."
    y"Who is this man?"
    y"And why do I like him so much?!"
    y"I haven't even met him yet..."
    "Your eyes are fixtated on the man."
    "You try, but for some reason you cannot seem to take your eyes off him."

    scene bg intro
    "Time passes."
    "As you gaze at the man, you forget about everything else."
    "Before you even realize, you have missed your stop."

    scene bg train 2
    y"Oh shit!"
    "The man hears your outburst, and looks over at you."
    m"Um, is something wrong?"
    "As you start to panic, the man gets up out of his seat."

    scene bg train 3

    "He begins to walk toward you."

    scene bg train 4

    y"(What do I do?!?!)"

    scene bg train 5

    m"Hello!"
    y"(oh god oh god oh god)"
    y"Uh... Hi."
    m"You yelled earlier,"
    m"is something wrong?"
    y"Uh, its fine."
    m"Are you sure?"
    y"Uh, well..."
    y"I kinda missed my stop."
    m"Oh, I can take you to your home if you want."
    y"Really?"
    m"Yeah, its really no problem."
    y"I hope you don't mind me asking, but what is your name?"
    b"My name is Barry! Barry B. Benson!"
    y"Nice to meet you Barry."

    scene bg intro

    "You both step off the train, and he grabs your hand."
    y"(I begin to blush, but he does not seem to notice.)"

    scene bg street

    "You begin walking down the street."
    b"So where exactly is your house?"
    y"Uh, its a few streets down from here."
    b"Alrighty!"

    scene bg intro

    "Time passes."

    scene bg street

    b"So, what do you like to do?"
    "You explain your hobbies and interests to him."
    "He listens very carefully,"
    "as if he is evaluating every single word."

    scene bg intro

    "More time passes."

    scene bg street

    y"We are almost there, we are on my street."
    b"Alright, well it was very nice talking to you!"
    y"I can go from here, thanks."
    b"Alright, but before you go,"
    b"can I take you out to dinner tomorrow night?"
    y"..."
    y"Yes! Yes you can!"
    b"Great, I'll see you there!"
    y"Bye!"

    scene bg intro

    "You go to your house, and open the door."

    scene bg bedroom

    y"Ah, home sweet home!"
    "You look around your room."
    "It is the same as always."
    "This is the house you grew up in,"
    "although your parents no longer live here."

    scene bg intro

    "You go into your bed and close your eyes."
    "You fall asleep thinking of that man,"
    "Barry B. Benson."

    "(This would be a good time to save!)"

    scene bg bedroom

    "You wake up. You overslept again."
    "You get dressed, and ready for your date."
    y"I am almost ready..."
    y"Hopefully this goes well."

    scene bg street

    y"What a nice day it is."
    "The streets are very busy and filled with people."
    "You pass by lots of people having various conversations about diverse topics."

    scene bg intro

    "You step onto the train."

    scene bg train

    "You are getting very anxious, and can barely wait any longer."

    scene bg intro

    "You step off of the train."

    scene bg station

    y"Well, I have about 30 minutes."

    "You look around, and its as if nobody sees you."

    "People are having conversations and laughing, nothing out of"

    "the ordinary."

    y"..."

    scene bg intro

    "You begin to scroll through your phone."

    "You see strange comments on your personal posts."

    y"Huh...?"

    y"What is this?!"

    "The comments are by a user with no username."

    "What on earth could this mean?"

    "Suddenly, you receive a call from an unkown number."

    y"Uh... Hello?"
    c"Hello. Are you at the location?"
    y"Who is this?"
    c"(laughter)"
    b"Its me, Barry!"
    y"Uh, I am almost there, why?"
    b"So I assume you are going on the date?"
    b"This is your last chance to decide."
    "This seems very out of character for him."
    "What have you gotten yourself into?"
    b"So, what will it be?"

    #Put a choice here when you learn how to you nerrrd

    menu:
        "What will you do?"

        "Say yes.":
            y"..."
            y"Yes."
            b"Great. I will see you there!"
            y"Yeah..."

            scene bg station

            "He hangs up."
            "What just happened?"
            y"Well, I better get going then..."

            scene bg intro

            "You walk over to the spot you both agreed on."
            "Barry said that this was the place."
            "You walk into the restaurant."

            b"Over here!"

            scene dinner 1

            b"Welcome, please sit down."
            y"Uh, sure. Also,"
            y"what was that phone call about?"
            b"..."
            b"Don't worry about it. Sit down."

            "Barry's voice has a sense of aggression."
            "Was it something you said?"

            b"Are you gonna sit down or what?"

            menu:
                "What will you do?"

                "Sit down.":
                    y"Yeah, sorry."
                    "You reluctantly sit down."
                    y"So, what are we going to order?"
                    b"..."
                    y"Why are you not talking to me?"
                    y"Is something wrong?"
                    b"Yes, unfortunately. And I'm sorry."
                    y"Sorry for what?"

                    scene dinner 2

                    b"Now!"

                    scene dinner 3

                    "Suddenly a man runs up to you, holding a weapon behind his back."

                    menu:
                        "What will you do?"

                        "Run away.":

                            scene bg intro

                            "You quickly run away, as a gunshot goes off behind you."
                            "You run out of the restaurant, and attempt to board the train."

                            scene bg train

                            "You can see the man running towards the train, with the intent to board it."
                            "As you panic, you begin to run towards the drivers area to ask for help."

                            scene bg intro

                            y"Listen, you have got to help me!"
                            d"What is the problem?"
                            y"There is a man trying to kill me!"
                            y"Hes going to-"
                            "Before you can finish, a bullet enters the back of your skull."
                            "You have unlocked the murdered ending. (Ending 1/9)"
                            "Thanks for playing."


                        "Call for help.":

                            scene dinner 4

                            "You shout for help as the man draws his gun."
                            y"Someone please help me!"
                            "The man laughs as nobody even looks up."
                            y"There is a man with a gun and he-"

                            scene dinner 5

                            "You are shot in the stomach, and left to bleed out."

                            scene bg intro

                            "You have unlocked the murdered ending. (Ending 2/9)"
                            "Thanks for playing."

                        "Attack the man.":
                            scene dinner 4

                            "You run towards the man as he draws his gun."
                            "You try to grab the gun, but he pulls the trigger."

                            scene dinner 5

                            "The bullet enters your shoulderblade."

                            scene bg intro

                            "Unable to react, you fall to the floor."

                            m"Hahaha... Nice try."

                            "You have unlocked the sorrow ending. (Ending 3/9)"


                "Call for help.":
                    y"Someone help me!"

                    scene dinner 2

                    "Your outburst gathers attention."
                    "With a sense of guilt on his face, Barry looks at you."
                    b"Now! Get them!"

                    scene dinner 3

                    "Suddenly a man appears from seemingly nowhere and looks at you."

                    scene dinner 4

                    m"Nighty night... Hahahaha!"

                    scene dinner 5

                    "The man shoots you in the leg with a hidden weapon."

                    scene bg intro

                    "You fall and hit your head, knocking you unconcious."

                    "..."

                    "You wake up in a dark room."

                    scene dark room

                    b"Oh... You are awake..."
                    b"I-"
                    b"I'm sorry for setting you up!"
                    b"I didn't know they were gonna shoot, I swear."
                    b"Unfortunatly theres nothing I can do."
                    b"Sorry."

                    scene bg intro

                    "You have unlocked the kidnapped ending. (Ending 4/9)"
                    "Thanks for playing."



        "Say no.":
            y"..."
            y"No."
            b"Ahahahahah!"
            b"Ahahah..."
            b"Hah..."
            b"We will track you down."
            b"One hour. Hope you are fast."

            scene bg station

            "Barry hangs up."
            y"What the fuck was that?"
            y"What does it mean?"
            y"Shit..."

            scene bg intro

            menu:
                "What will you do?"

                "Go to your house":

                    "You take the train back, and run towards your house."
                    "You rush into your house and lock the doors and windows."
                    "You run up to your bedroom."

                    scene bg bedroom

                    "You panic. Your time is almost up."
                    "You hear a knock on your front door, followed by a loud crash."
                    y"They busted down the door?!"

                    menu:
                        "Where do you go?"

                        "Closet.":

                            scene bg intro

                            "You quickly go into the closet, but you feel something brush against your leg."
                            "Something else is in the closet."
                            y"AAAAAAH!"
                            "You get stabbed in your spine, and your body remains hidden in the closet."
                            "You have unlocked the forever lost ending. (Ending 5/9)"
                            "Thanks for playing."

                        "Bed.":

                            scene bg intro

                            "You slide under the bed, you can hear footsteps from downstairs."
                            "Suddenly, you hear the closet door open, and footsteps leaving the room."
                            y"(Whispers) Glad I did not go in there..."
                            "You hear voices, and suddenly three people bust down the door of your room."
                            "Suddenly, one of them look under the bed."
                            "Silently, they aim a gun at your face, and pull the trigger."
                            "You have unlocked the forever lost ending. (Ending 6/9)"
                            "Thanks for playing."

                        "Window.":

                            scene bg intro

                            "You run over to the window."
                            y"Think fast, think fast..."

                            menu:
                                "What do you do now?"

                                "Jump Out.":

                                    "You hit the window with your fist,"
                                    "and it breaks. Blood is on your hands."
                                    "You jump out as two men bust down the door."
                                    "You fall on your head and die."

                                    "You have unlocked the idiotic ending. (Ending 7/9)"
                                    "Thanks for playing."

                                "Open Window.":

                                    "You open the window, and go under your bed."
                                    "Suddenly, you hear the closet door open, and footsteps leaving the room."
                                    "You hear voices, and suddenly three people bust down the door of your room."
                                    m"Where did he go?!"
                                    m"Window."
                                    m"Damn."
                                    "The three leave your room. You get out from under the bed and walk to the window."
                                    "They walk away, defeated."
                                    "You have unlocked the true ending. (Ending 8/9)"
                                    "Thanks for playing."



                "Call for help":

                    scene bg station

                    "You look through your contacts, and dial the local police station."
                    "Suddenly, your cell service goes down."

                    scene bg intro

                    "A hand grabs your mouth from behind you, muffling your screams."
                    "You are slowly and painfully suffocated."
                    "You have unlocked the breath taking ending. (Ending 9/9)"
                    "Thanks for playing."
    return