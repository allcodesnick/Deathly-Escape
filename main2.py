character_name = input("Enter your characters name: ")


def intro():
    print("Your character's name is: " + character_name)
    print("***********     Story   ***********")
    print(character_name + " was convicted of murder and sentenced to the death penalty.")
    print("Now " + character_name + " is fighting for his life.")
    print("Your choices will dictate how " + character_name + " escapes your characters impending doom.")
    print("Note that every decison you make leads you down a different path.")
    print("There is only one right path.")
    print("**********CHOOSE WISELY!!!**********")


intro()


def end():
    print("***********     Game Over   ***********")
    print(character_name + " has done it and avoided death!!!")
    print("***********     Game Over   ***********")
    exit()


def dirty_lawyer_CPI():
    a = "Help"
    b = "Dont Help"
    while True:
        choice = input("Now that you spent that money on the PI lets put him to work. The Private investigator found little evidence to get the lawyer to work for you, but it works. Now will you get the private investigator to help on your case? (A) Help or (B) Dont Help: ")
        if choice == "a":
            print("You chose for the cheap private investigator to help and he ruined your case!!")
            print("=============GAMEOVER==========")
            exit()
            break
        elif choice == "b":
            print("You chose for him not to help which is a good thing. lets try and hire an expensive lawyer.")
            dirty_lawyer_EPI()
            break
        else:
            print("Not an option")


def dirty_lawyer_EPI():
    a = "Investigate Case"
    b = "Do Nothing"
    while True:
        choice = input(
            "Now that you spent all that money the PI has investigated and found enough evidence to get the lawyer to work for you. Will you also get the PI to investigate your case or not? (A) Investigate Case or (B) Do Nothing: ")
        if choice == "a":
            print(
                "*******The PI and Lawyer working together have found an error in your case enough to get you free!!! Youve done it!!*******")
            end()
            break
        elif choice == "b":
            print("You chose to did nothing!! Your lawyer wasnt enough.")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("Not an option")


def dirty_lawyer_PI():
    a = "Expensive PI"
    b = "Cheap PI"
    while True:
        choice = input(
            "You want to hire a PI(private investigator) but its gonna cost you! Do you wanna pay for the Expensive Private investigator or a Cheap Private investigator? (A) Expensive PI or (B) Cheap PI: ")
        if choice == "a":
            print("You chose the Expensive Private investigator route.")
            dirty_lawyer_EPI()
            break
        elif choice == "b":
            print("You chose the Cheap Private investigator route.")
            dirty_lawyer_CPI()
            break
        else:
            print("Not an option")


def innocent_lawyer_fake_photo_friend():
    a = "Expose the Judge"
    b = "Threaten the Judge"
    while True:
        choice = input("The Lawyer finds an error with the Judge. The judge threatened the jury!! What now? (A)Expose the Judge or (B)Threaten the Judge: ")
        if choice == "a":
            print("You chose to expose the Judge and the state has chosen to look over your case and they found you and plenty of others innocent. Your a free man!!!!")
            end()
            break
        elif choice == "b":
            print("You chose to threaten the Judge but the judge speed up your excution. You die!!")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("Not an option")


def innocent_lawyer_fake_photo():
    a = "Friend"
    b = "Stranger"
    while True:
        choice = input("Who do we get to slip something in his drink? (A) Friend or (B) Stranger: ")
        if choice == "a":
            print("You chose your friend. Your friend was successful. She faked a picture of the good lawyer kissing her. You threaten to show his wife and he takes your case.")
            innocent_lawyer_fake_photo_friend()
            break
        elif choice == "b":
            print(
                "You chose the stranger but the stranger got caught and snitched on you! They move up youe execution date. You died!!")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("Not an option")


def innocent_lawyer_stripper_confront():
    a = "Tell"
    b = "Death Sentence"
    while True:
        choice = input(
            "You find out this lawyer has a wife and is pregnant. The innocent lawyer has a heart attack due to stress and dies. What now? (A) Tell the wife it was your fault or (B) take the death sentence cause of your guilt: ")
        if choice == "a":
            print("You told him her and she goes to the authorities. They pushed up your execution date! You die!!")
            print("=============GAMEOVER==========")
            exit()
            break
        elif choice == "b":
            print("You die!!")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("Not an option")


def innocent_lawyer_stripper():
    a = "Tell"
    b = "Confront"
    while True:
        choice = input("Lucky for you shes pretty cheap? Now what do you want her to do?(A) Tell the lawyer of your plans or (B) Make stripper confront him and threaten him: ")
        if choice == "a":
            print("You told him of your plans and he snitched on your. They pushed up your execution date! You die!!")
            print("=============GAMEOVER==========")
            exit()
            break
        elif choice == "b":
            print("You chose the Make the stripper confront him. Hes gonna take your case!! You an evil one " + character_name + ".")
            innocent_lawyer_stripper_confront()
            break
        else:
            print("Not an option")


def blackmail_dirty_lawyer():
    a = "Hire P.I"
    b = "Threaten"
    while True:
        choice = input("Now that Youve choose the dirty lawyer ow are you gonna do it?\n(A) Hire private investigatior or (B) Threaten to expose: ")
        if choice == "a":
            print("You chose the Hire P.I. Good lets get our hands dirty")
            dirty_lawyer_PI()
            break
        elif choice == "b":
            print("You chose to threaten him. Sorry I dont think thats gonna work.")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("Not an option")


def blackmail_innocent_lawyer():
    a = "Hire a stripper"
    b = "Fake a photo"
    while True:
        choice = input("Wow! Anything it takes to clear your name huh? how you gonna do it?(A) Hire a stripper to lie or (B) Fake a photo: ")
        if choice == "a":
            print("WOAAh!! Do you know any strippers?! lets see what I can do.")
            innocent_lawyer_stripper()
            break
        elif choice == "b":
            print("So were gonna fake a photo huh? We'll pay someone to slip something in his drink\nand take a picture with her the threaten to show his wife.")
            innocent_lawyer_fake_photo()
            break
        else:
            print("Not an option")


def blackmail_path():
    a = "Prove"
    b = "Blackmail"
    while True:
        choice = input("Unfortunatly for some loser You have to blackmail one of these lawyers to help with your case.\nWe have 2 unlucky candidates. I know you picked the innocent route but life gives you lemons, make apple juice.\nThe Innocent Lawyer who is a family man with no dirty past.\nor The Dirty lawyer with a dirty secret.\nWhich one do you choose? (A) Innocent Lawer or (B) Dirty lawyer: ")
        a = "Innocent Lawyer"
        b = "Dirty Lawyer"
        if choice == "a":
            print("You chose the \"Innocent Lawer\" route.")
            blackmail_innocent_lawyer()
            break
        elif choice == "b":
            print("You chose the \"Dirty lawyer\" route.")
            blackmail_dirty_lawyer()
            break
        else:
            print("Not an option")


def legal_blackmail_prove():
    a = "Prove"
    b = "Blackmail"
    while True:
        choice = input("Wow so your arent as evil as the rest. Now lets see what path you choose between these two *evil laugh*(A) Prove or (B) blackmail: ")
        if choice == "a":
            print("You chose the \"Prove your innocence\" route.")
            prove_innocence()
            break
        elif choice == "b":
            print("You chose the \"blackmail\" route.")
            blackmail_path()
            break
        else:
            print("Not an option")


def final():
    a = " light"
    b = " look for spot "
    while True:
        choice = input(" yess after hard work 4 days straight with only 2 hours of sleep you made it but you are in 3rd floor of the building (A) just jump (B) try to slowly go down by holding the bricks ")
        if choice == "a":
            print(" wait until the midnight and squeze your self from the hole which you just made ")
            print("  yess put your legs in there first and just jump")
            print(" !!!!!!!!!! and yesss you are alive but one of your legs seems like broken !!!! ")
            print(" anyways you are free be patient and walk fast as much as you can ")
            end()
            break
        elif choice == "b":
            print("you were half way there but you leg slipped and you end up dead outside of the building!!!!!!!!!!")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("not an option")


def room2():
    a = " dig2"
    b = " rest2"
    while True:
        choice = input(" good news you have way there yess its been a month and you have been digging at nigth and sleeping at noon but you want to speed up? (A) keep it as it is (B)speed up: ")
        if choice == "b":
            print(" yess lets dig 14 HOURS A DAY")
            final()
            break
        elif choice == "a":
            print(
                " (after a week) other prisoners are talking about that securities will check every single room because doctor told them that he missing a sharp tool!!!!! ")
            print("SECURITY lets start from here")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("not an option")


def half():
    a = " dig"
    b = " rest"
    while True:
        choice = input(
            " you have been digging with a scissors for days now and you got 5 inches already would you like to sleep because? *(A) get a rest and sleep (B) keep digging lets do it faster: ")
        if choice == "a":
            print(" well yea you need this nap ")
            room2()
            break
        elif choice == "b":
            print(" you got sick again because you havent sleep for days ")
            print("now security coming to check up ")
            print(" he saw everthing !!! ")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("not an option")


def room():
    a = " bed"
    b = " toilet"
    while True:
        choice = input(
            " so you made it congrants now you can start digging but where think twice!!!! (A) behind the toilet (B) behind the bed: ")
        if choice == "b":
            print(" cool so start to dig usinig you scissors ")
            half()
            break
        elif choice == "a":
            print("well you cant because you will get sick from the smell use your brain!!!!")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("not an option")


def checkup():
    a = " act normal"
    b = " tell them you in hurry"
    while True:
        choice = input(" you got the scissors in your pants but there is another problem that you need to face.. security check up!!!!!!!!!! (A)act normal (B) tell them you are in hurry:  ")
        if choice == "a":
            print(" hey sir you must be tired yea SECURITY yea a little bit ")
            print(" checking in progress")
            print(" okay you good to go ")
            room()
            break
        elif choice == "b":
            print(" hey sir can you check me up really quick because i gotta go to the bathroom ")
            print(" ohh okay come here are you hiding something")
            print(" absolutely not ")
            print(" Cool checking in progress ")
            print(" what is this a scissors !!!!!!! ")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("not an option")


def emergancy():
    a = " tell a lie "
    b = " get a deal with doctor"
    while True:
        choice = input("yesss you made it to the emergancy room. now you have to distract the doctor somehow.  (A) tell doctor that security is waiting (B) get a deal with doctor: ")
        if choice == "a":
            print(" 'doctor' what are u talking about why is he calling me 'i dont know DR but he told me to tell you that he is waiting ' ")
            print(" doctor walked out from the room quick get something useful to dig ")
            print(" doctor's scissors yes  it will work quickly hide it some where in your pants ")
            print(" DOCTOR well he wasnt calling me maybe be you are thinking of something")
            print(" no doctor im not planing anything its just this pain making me go crazy please help me ")
            print(" doctor helping ")
            checkup()
            break
        elif choice == "b":
            print(" okay so you trying to escape from here alrigth okay ")
            print(" hello Yes can i have a backup to emergancy room!!!!!!")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("not an option")


def hand():
    a = "breaking it"
    b = "giving up"
    while True:
        choice = input("you want to see the doctor and you want to go there by breaking your hand are you still want to do that  (A) giving up its all over (B) yes im breaking my hand: ")
        if choice == "b":
            print(" punching The wall with  max  power ohh my god the pain is real ")
            emergancy()
            break
        elif choice == "a":
            print("well just like that okay its your choices")
            print("are you sure??????? well bye ")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("not an option")


def pretending():
    a = " hard task "
    b = " dont get cought "
    while True:
        choice = input(" its hard very hard to go to the doctor because securities will check if you are really hurt but its your choice (A) pretend that you are sick (B) stay and make a better plan: ")
        if choice == "a":
            print("WOW now you will get checked by securities  / " " 'security' hey so you are sick come closer whispiring TRY SOMETHING BETTER and he punched you in a face ")
            print("=============GAMEOVER==========")
            exit()
            break
        elif choice == "b":
            print(" only thing you can do is break your hand by punching the wall yess it hurts but you have to try")
            hand()
            break
        else:
            print(" not an option ")


def doctor_office():
    a = "break your hand"
    b = "pretend to be sick"
    while True:
        choice = input(" to ask for help you need to be hurt you have two choices (A) break your hands by punching the wall or (B) pretend to be sick:")
        if choice == "a":
            print(" yes its not easy and yess it hurts but you want to escape or not?????? ")
            hand()
            break
        elif choice == "b":
            print(" doctor will know that you are pretending, and before doctor security will check you as well but you can try ")
            pretending()
            break
        else:
            print("Not an option.")


def kitchen():
    a = " get that big knife "
    b = " small knife "
    while True:
        choice = input(" you made it now look for something useful to dig (A) big knife  (B) look for something else: ")
        if choice == "a":
            print(" this knife is HUGE how you planning to hide it ")
            print(" security saw you with the big knife on your hand he shoot you to your leg ")
            print("they are taking you to the emergancy room and punishment is waiting for you after recovery")
            emergancy()
            break
        elif choice == "b":
            print(" COOKER hey what are you doing here!!! ")
            print(" presses the red button to call backup!!!!")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("not an option")


def Distract_security():
    a = "start a fight"
    b = " get help from your friend "
    while True:
        choice = input("you chose to distract security guards now you have two choices (A) start a fight between people or (B) get help from your friend : ")
        if choice == "a":
            print(" yoo iron he said your pussy cat " '"Iron said what who"' '"here this guy"' '"come over here"' "fight started")
            kitchen()
            break
        elif choice == "b":
            print("your friend has snitched you and they gave him a year less as a award")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("Not an option")


def sneak_into():

    a = "cerefully "
    b = " deal with chief"
    while True:
        choice = input("you chose to sneak into the kitchen to get a knife you have two choices (A) go to the kitchen during lunch (B) try to get a deal with chief ")
        if choice == "a":
            print(" security guards all over the place you need to distract them: ")
            Distract_security()
            break
        elif choice == "b":
            print("chief has been snitched you now you are in big trouble")
            print("=============GAMEOVER==========")
            exit()
            break
        else:
            print("Not an option")


def long_dig():
    a = "tired"
    b = " spoon is weak"
    while True:
        choice = input("you have been digging for weeks but you only digged 5 inches do you want to change things around? (A) keep digging (B) try to get a knife: ")
        if choice == "a":
            print("its been a month and you only got 7 inches ")
            print(" you are so tired ")
            print("you couldnt handle it your hands just cant continue and your brain is tired as well ")
            print("=============GAMEOVER==========")
            exit()
            break
        elif choice == "b":
            print(" getting a knife is hard but there is possible chances")
            dig_using_knife()
            break
        else:
            print("not an option")


def short_dig():
    a = "smelling very bad"
    b = " spoon is weak"
    while True:
        choice = input(" you have been digging for days but no results and your spoon is so weak what you want to do (A) keep digging with patients (B) try to get a knife :")
        if choice == "a":
            print(" the smell from the toilet got you so sick now you have to see the doctor ")
            emergancy()
            break
        elif choice == "b":
            print(" getting a knife a hard task but you can try it ")
            dig_using_knife()
            break
        else:
            print("not an option")


def spoon():
    a = "dig back of the toilet"
    b = "dig back of the bed"
    while True:
        choice = input("you got the spoon with you and you are in your room ready to dig but where remember which side of the room takes you outside of the building (A) dig behind bed (B) dig behind toilet: ")
        if choice == "a":
            print(" make sure that it takes you outside and becareful dont let anyone see")
            long_dig()
            break
        elif choice == "b":
            print(" good choice but it takes a lot work and patient because of a smell good luck: ")
            short_dig()
            break
        else:
            print("not an option")


def dig_using_spoon():
    a = "spoon"
    b = "there is no other way "
    while True:
        choice = input(
            " you chose dig using a spoon now you have two options (A) lunch spoon or (B) there is no other way: ")
        if choice == "a":
            print("Dont forget to hide your spoon after luch")
            spoon()
            break
        elif choice == "b":
            print("no other way just hide your spoon after lunch")
            spoon()
            break
        else:
            print("Not an option")


def dig_using_knife():
    while True:
        a = " doctors office "
        b = "sneak in to the kithen"
        choice = input(
            "you chose to use knife to dig out. You have two choices (A) from doctor's room (B) from the kitchen: ")
        if choice == "a":
            print(" you need to be hurt to ask doctor for help")
            doctor_office()
            break
        elif choice == "b":
            print(" sneak into the kitchen after lunch")
            sneak_into()
            break
        else:
            print("Not an option")


def dig_your_way_out():
    while True:
        a = " dig using a spoon"
        b = "dig using a knife"
        choice = input("you chose to dig your way out now you have two choices (A)do you want to use spoon or (B) do you want to use knife: ")
        if choice == "a":
            print(" it takes very long but works,")
            dig_using_spoon()
            break
        elif choice == "b":
            print(" its very hard to get a knife in prison but there is one way!!!: ")
            dig_using_knife()
            break
        else:
            print("Not an option")


def illegal_dig_escape():
    a = "Dig"
    b = "Escape"
    while True:
        choice = input("what path do you choose?(A) Dig Your way out or (B) Escape: ")
        if choice == "a":
            print("You chose the \"Dig Your way out\" route.")
            dig_your_way_out()
            break
        elif choice == "b":
            print("You chose the \"Escape\" route.")
            kill_knock()
            break
        else:
            print("Not an option")


def legal_illegal():
    a = "legal"
    b = "illegal"
    while True:
        choice = input("what path do you choose?(A) legal or (B) illegal: ")
        if choice == "a":
            legal_blackmail_prove()
            break
        elif choice == "b":
            illegal_dig_escape()
            break
        else:
            print("Not an option")


def prove_innocence():

    print("The odds are stacked against you in this case but theres still hope. You must gather evidence from the crime scene to free yourself. Some DNA was left at the crime scene by the killer but its not 100% traceable as it needs to be tested. Also the janitor was working at the office that night, he might have some clues to who committed the murder. The choice is up to you: (A) check for DNA or (B) question the janitor, what will it be?")
    a = "Test for DNA"
    b = "Question the Janitor"
    while True:
        choice = input()
        if choice == "a":
            print(
                "Testing for DNA is a good decision. " + character_name + " travels back to the crime scene with a forensics team to scan the office for DNA. On his way into the office he finds that the door is locked. Theres a lockpad on the door to the office thats prevents " + character_name + " from entering. Luke must get in to be one step closer to finding the killer. How should he approach this? (A)Break the door down or (B)figure out the pin number?")
            break_pin()
            break
        elif choice == "b":
            print(
                "The janitor would know whos been on this floor, pressure him! " + character_name + " finds the janitor and begins to do his own investigation on him. The janitor has no real solid information but he did mention that wife of the boss named Lisa went into the office around the time the cameras went out. (A) Find Lisa or (B) pressure the janitor more?")
            Lisa_janitor()
            break
        else:
            print("Not an option")
            break


def break_pin():
    a = "Break Down the Door"
    b = "Figure Out the Pin"
    while True:
        choice = input()
        if choice == "a":
            print("Loud and careless, that will never work against a reinforced door. Choose another option!")
            break
        elif choice == "b":
            print("Someone has to know the pin... but who? The janitor seems suspicious, lets question him. The janitor would know whos been on this floor, pressure him! Luke finds the janitor and begins to do his own investigation on him. The janitor has no real solid information but he did mention that the wife of the boss named Lisa went into the office around the time the cameras went out.(A) Find Lisa or (B) pressure the janitor more?")
            Lisa_janitor()
            break
        else:
            print("Not an option")


def Lisa_janitor():
    a = "Find Lisa"
    b = "Question the Janitor more"
    while True:
        choice = input()
        if choice == "a":
            print("Why might Lisa possibly be at the office when the murder happened?... This is getting interesting!")
            getting_pin()
            break
        elif choice == "b":
            print("After more questioning Luke found himself with no solid evidence. Luke decides to leave the janitor alone after not getting much from him. Choose another option!")
            break
        else:
            print("Not an option")


def getting_pin():
    print("Word around the office is that Lisa was having an affair with a fellow coworker. She visited the boss only on Tuesdays and Thursdays after 5pm when everybody at the office was gone.")
    print("Lisa is a very stubborn person so convincing her to give us the pin number is going to be a struggle. " + character_name + " visits Lisa at her home in the upper class neighborhood of Orange County, California.")
    print("Upon approaching the gate a car was leaving that " + character_name + " recognized. An idea came forth! Lisa was suprised to see me and acted nervous...")
    print("Hello Lisa! Was that John? *Lisa became even more nervous* Look... I know you are covering up for him so give me the pin number or else you'll be going down with him! With a loss of words Lisa hands " + character_name + " a paper with the pin number.")
    print("While " + character_name + " and the forensics team were on their way back to the office to enter the pin, their car starts to make a flapping sound. They got a flat tire... Fixing the flat tire would take 15 minutes to do but they would have to go to the store to get some tools. Calling the office to send a worker to pick them up would take 45 minutes but will be free since its on the office. The sooner we get back to the office, the closer " + character_name + " is to proving their innocence. What will it be? (A) Fix the flat tire or (B) Call the office for a pickup?")
    a = "Fix the flat tire"
    b = "Call the office for a pickup"
    while True:
        choice = input()
        if choice == "a":
            print("Not afraid to get your hands dirty I see!")
            fix_flat()
        elif choice == "b":
            print("Really?... I guess not all of us is meant to be a handy man...")
            call_office()
        else:
            print("Not an option")
            break


def fix_flat():
    print("After struggling with fixing the car a oncoming truck swerves off the road and hits you and your team head on.")
    print("=============GAMEOVER==========")


def call_office():
    print("45 Minutes Later...")
    print("The companys car pulls up and everyone heads back to the office.")
    print("Once back at the office" + character_name + "enters in the pin and the doors lock clicks! Theyre in.")
    print("The whole team searches the office up and down for any clues relating to this murder. After searching for a whole hour the team gets frustrated as they have no real leads.")
    print("Just when everyone was about to give up a member of the forensics team trips over a stuck up nail in the hardwood floor. The tea mfinds this very odd and soon realizes this was done on purpose.")
    print("Taking up the floor is theyre next move." + character_name + " calls a buddy and within 30 minutes the hardwood floor is out and there is a trap door! Inside the trap door" + character_name + "finds a note.")
    print("The note reads: meet me at the pier on Saturday to find out the truth. Meeting with this person could be very dangerous as they are potientally the murderer. What will you do? Meet the mysterious person (A) or Ignore the note (B)")
    a = "Meet the mysterious person"
    b = "Ignore the note"
    while True:
        choice = input()
        if choice == "a":
            print("Smart decision! This could be our only hope.")
            meet_person()
        elif choice == "b":
            print("The team continues searching and find no other clues. A week later your court date comes and with no solid information you cannot prove your innocence.")
            print("You are found guilty on all charges and are sentenced to death by the electric chair...")
            print("After struggling with fixing the car a oncoming truck swerves off the road and hits you and your team head on.")
            print("=============GAMEOVER==========")


def meet_person():
    print("Two days passes by and Saturday is here. Judgement day is on Wenesday and your running out of time. Time to start making some moves.")
    print("You arrive at the pier at the designated time and you see a man in a black cloak sitting by himself. To your suprise you see the Janitor!!! At this point your fuming and want to beat his a** but part of you wants to keep your cool.")
    print("What will it be? Drop this motherfuc*er (A) or Keep your cool (B)")
    a = "Drop this motherfuc*er"
    b = "Keep your cool"
    while True:
        choice = input()
        if choice == "a":
            print("You take out your glock and smoke this fool as fast as Thanos snapped his fingers and wiped out half the population. Doing this obviously didnt help your case in the end.")
            print("Judgement days arrives and it turns out that you were found to be framed in the murder of your boss. This didnt matter though as you did commit 1st degree murder...")
            print("You are sent to death by hanging")
            print("You should have kept your cool bro lmao")
            print("=============GAMEOVER==========")
        elif choice == "b":
            print("Lets see what this fool has to say.")
            keep_cool()
        else:
            print("Not an option")
            break


def keep_cool():
    print("The janitor starts to give his story. He explains to you that he was the one who purposely cut the cameras out. You have enough information to buid your case and prove your innocence in court but you get this weird feeling in your gut.")
    print("Why whould the killer turn himself in so easily? Is this a cover up for the real murderer? Your court date is coming up fast and you need to make a decision! Bring the janitor in as the killer (A) or find out more information (B)")
    a = "Bring the janitor in as the killer"
    b = "find out more information"
    while True:
        choice = input()
        if choice == "a":
            print("You go to court with the janitor and try to prove your innocence. Even with the audio recording you had secretly taken of the janitor confessing to cutting the cameras off you still dont have enough solid information.")
            print("Despite your best efforts you are still given the death penatly.")
            print("=============GAMEOVER==========")

        elif choice == "b":
            print("You go back to the office and put together small pieces of information to help your case. Judgement day arrives and you walk into the court room with confidence.")
            print("You use the audio recording of the janitor to prove him guilty of being involed with the murder but he isnt the murder. The real murderer was a member of the forensics team you hired! His name is John.")
            print("John was playing a role on the forensics team to try and steer you into thinking it was the janitor. John forgot to cover up his tracks though.")
            print("John didnt realize that he left his phone in the car on the way back to the office." + character_name + "finds this and has all the phone call conversations between John and the janitor and their plan.")
            print("John stumbled onto to floor in disbelief, he though nobody would ever find out. After presenting this information you were found not guilty! The janitor went to jail on a charge of tampering with evidence of a murder.")
            print("The janitor was found guilty and sentened to life in jail without the chance of parole.")
            print("Congratulations! You did it! You go home to your friends and family and live the rest of your life stress free.")
            print("THE END")
            exit()


def kill_knock():
    print("After 10 minutes of talking to Wutang,a nerd " + character_name + " saved from getting violated in the shower, wants to help him. " + character_name + " goes up to Haward to talk about the plans for escape. \n So far Haward built DIY high tech heat gun called a melter wherein the heat gun, can turn its output of energy to lava/ hot air, and fireball so it can melt through iron, metal or even human flash in mere seconds. \n The most unexpected thing happened. Haward didn’t want to escape prison, he likes it here but he will Luke escape which is why Haward bult the device.")
    print("Its 1pm at night in prison. Its drizzing outside, and the guards are feeling sleepy. So this was a perfect opportunity for Luke to escape.")
    print(character_name + " sees a guard drunk near a wall facing the other side of " + character_name + "'s cell. He is barely concious.")
    print("So," + character_name + " melts part of the cell bar with his melter and prepares to attack the guard")
    print("Choose whether" + character_name + " should kill the guard by spraying a large amount of the substance of the melter at the guard or sneak behind the guard and choke him unconcious. So kill or knock")
    a = "Kill"
    b = "Knock"
    choice = input("What is option do you choose? (A)Kill the guard by spraying a large amount of the substance of the melter at the guard or (B)sneak behind the guard and choke him unconcious to knock him out. ")
    if choice == "a":
        print("The sound of the skull melting alerts a nearby guard and blood is from the skull is melted with skin is all over the floor. The guard arrives at the scene and you have no way of hiding the messy body so the guard rings the alarm. \n The SWAT team comes in arrests " + character_name)
        print("=============GAMEOVER==========")
        exit()
    elif choice == "b":
        print("You chose knock route")
        print(character_name + "The guard is unconcious. " + character_name + " sees desk on the side of him. You hide the body behind the desk and rush to next place down the hallway.")
        doorred_doorblue()
    else:
        print("Not an option")


def doorred_doorblue():
    print(character_name + " starts speed walking with low sound through the hallway until you see two different doors one colored blue and the other colored red with no labels. ")
    a = "red door"
    b = "blue door"
    while True:
        choice = input("What option do you choose? (A)Pick door red or (B) Pick door blue")
        if choice == "a":
            print(character_name + " noticed the red door is locked. But just in time he remembered he still had the melter so he shot it in the door handle and it started melting. \n After 20 seconds has passed the door was wide open and Luke sees the outside world with a gate blocking it. \n So he shoots the melter at the gate and it forms a hole big enough for " + character_name + " to escape. Now " + character_name + "is finally free!! ")
            print("Your character escaped therefor you win the game!!!!")
            break
        elif choice == "b":
            print("Blue door leads to midnight closed hours kiitchen. Theres only 2 gurads guarding it with powerful rifle and a shotgun. \n So one hit from them and" + character_name + "will die. So he analyzes the situation while hiding behind the kichen desk. " + character_name + " found a great idea. " + character_name + "can either take the kichen knife and fling it at one of the guards and shoot the next guard in the head while distracted by knife in his partners chest. \n Or you can throw a spoon in a distance to distract both guards to look at the direction of spoon. Then shoot both guards fast, one after the other to go past the next door in the kichen ")
            spoondistract_knifedistract()
        else:
            print("Not an option")


def spoondistract_knifedistract():
    a = "spoon"
    b = "knife"
    while True:
        choice = input("What option do you choose? (A)Use a spoon or (B) Use a knife ")
        if choice == "a":
            print(character_name + " threw a spoon from top of the cabinet on the side of one of the guards. The trejictory of the spoon did land near the guard but ended up sliding towards a oven. The sound of the spoon starled the guards.")
            print("But because the spoon landed near the oven which was a bit farther than what was hoped to have landed. So one of the guards said that he will check it out. While the other one stayed in the same position.")
            print("Well this created an unwarrented issue. Now the guards split but the plan was for both guards to go to the direction of the spoon so" + character_name + "could kill them both at once. Well now the only other solution plan a) is to kill the guard near the oven by spearing him into the oven and use his dead body quickly as shield from the shotgun blast that will probably come from the other guard firing at" + character_name + " when noticing the attack.")
            print("Or plan b) use youself as distraction by going up to them by saying that you surrender and when and if they try to cuff you,so in that opportunity you use your shaving blade you had in your pocket and slice one of the guards neck and punch the other guard in the balls. While the guard is down, use the melter gun to shoot him.")
            spearing_selfdistraction()
        elif choice == "b":
            print(character_name + " chose to use the knife and threw it at the guard on the left on his head. In that few seconds while the other guard was very surprised and wasnt sure what to make of the situation.")
            print(character_name + " uses that few seconds of opportunity to blast the head off with the 2nd part of the melter gun called called heat blast since the melter would take longer as the guard has a protective helmet.")
            print(character_name + " moves past the the bodies and was about to open the door. At that point " + character_name + " notices a small ventilation pathway that leads to the outside world.")
            print(character_name + " enters the ventalation system and goes to the outside world.")
            print("You win the game!!!!")
            end()
            break
        else:
            print("Not an option")


def spearing_selfdistraction():
    a = "spearing"
    b = "selfdistraction"
    while True:
        choice = input("What option do you choose? (A) Spear tackle the guard to the oven and use the melter to attack the other guy. \n (B) Pretend to stop, and let" + character_name + "be cought and then when the guards start to cuff" + character_name + "you bring out your shaving blade and kill both guards: ")
        if choice == "a":
            print(character_name + " spears tackles towards the guard facing oven and baaaaamm!! The guards face hits the hot oven with fire spursing out and the guard screams with tremendous pain. \n The other guard hears the scream and without a moments notice booom, the guard fires the shotgun at" + character_name + ". ")
            print(character_name + " dies immediately and game is over. ")
            print("=============GAMEOVER==========")

            exit()
            break
        elif choice == "b":
            print(character_name + " uses it self as distraction and gets on the ground and pleas about giving up. So both guard approaches " + character_name + " and gets killed immideately as planned.")
            print(character_name + " starts walking past the kichen and sees another door but this time lots of iron bars.")
            print("All that can be heard is the grawling from a distance. He really do want to get out of prison and realizes he does have a powerful weapon so theres nothing to be afraid off.")
            print("So," + character_name + " opens the door and as " + character_name + " approches more there were notcibly lots of red eyes and smell of saliva. The grawling gets louder and baaammm!! \n Out of nowhere a dog attacks " + character_name + " and you shoot the dog. But now more are approaching")
            fight_flee()
        else:
            print("Not an Option")


def fight_flee():
    a = "fight"
    b = "flee"
    while True:
        choice = input("What option do you choose? (A)Fight all the dogs in the room or (B)Run away from the room and start going back to the kichen.")
        if choice == "a":
            print(character_name + "starts shooting all around the room with the lava melting part of the gun, but the dogs were overwhlming. \n So many kept coming attacking from all direction. After 5 minutes of battle" + character_name + " gets tired and in the moment of tiredness, two huge bull dogs appear and rips " + character_name + " to shreds")
            print(character_name + "dies :( Therefore")
            print("=============GAMEOVER==========")
            exit()
            break
        elif choice == "b":
            print(character_name + "starts running for his life but sadly the mistake" + character_name + "made was not hiding the bodies before and now theres a swarm of gaurds and they notice" + character_name + "running.")
            print("The guards got startled and started shooting at" + character_name + "and all those various bullets hit" + character_name + "severely. His body got disesembered by all the bullets and dies immedietly.")
            print("=============GAMEOVER==========")
            exit()
            break


def main():
    legal_illegal()


main()
