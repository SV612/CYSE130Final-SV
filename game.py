import random
import math

BOLD = '\033[1m'
END = '\033[0m'
dialog = ""

inventory = []
player_stats = {"Health": 40, "Stamina": 10, "Strength": 5}

def main():
    print(BOLD + "-------------My Little Pony: Beyond The Last Problem-------------" + END) # Confirmed with Professor that Bolding is acceptable.
    print("NOTE: You may need to press the 'ENTER' key to go through the game and some dialog.\n")
    role = input("Please type 'Start' to start the game\n")
    game_story(role)

def game_story(game_choice):
    print(f"Your choice was: {game_choice}\n")
    if game_choice in ["Start", "start", "S", "s"]:
        print(BOLD + f"Your character is Twilight Sparkle!" + END)
        print(f"You have gained magical abilties and the Book of Magic!\n")
        add_to_inventory("Book of Magic")
    else:
        print("You did not type Start")   
    if game_choice in ["Start", "start", "S", "s"]:
        print()
        print("While exploring a cavern, Twilight stumbles on a golden encrusted door frame. As she stepped closer; the words enscribed on the frame began to glow. \nIn the blink of an eye she was transported to a faraway land!")
        print()
        print("Meet your crew!\n")
        mage = NPC("Sunburst", "Mage", "Hello Twilight: I hope to help you find new sources of magic!", "Staff of Knowledge")
        witch = NPC("Trixie", "Witch", "I Am The Great & Powerful Trixie; my magic skills are sure to disorient any foe! ", "Deception [Close up Magic]")
        disciple = NPC("Starlight", "Disciple", "I can't wait to see what there is to explore in this new land.", "Forcefield Spell")
        mage.talk()
        print()
        witch.talk()
        print()
        disciple.talk()
        print()

        counter = 0
        while counter == 0:
            print(f"You come across an stronghold! Do you want to explore it?\n")
            explore_stronghold = get_choice(input("Type (yes) to explore or (no) to travel past: "))
            if explore_stronghold in ["yes", "y", "YES", "Y", "YE", "ye"]:
                dialog = input("You explore the stronghold and see a demon attacking an old man!\n")
                dialog = input(f"Entering combat...\n\n")

                demon = Enemy("The Demon", "Demon Sword", "Stronghold Enemy", 20)
                turn_number = 0

                while demon.health > 0 and player_stats["Health"] > 0:
                    turn_number += 1
                    print(f"-----------Turn #{turn_number}------------")
                    print("The Demon's health:", demon.health)
                    print(f"Your Health: {player_stats['Health']}")
                    try: 
                        action = get_choice(input("Do you want to (Attack) or (Use Item)? "))
                    except Exception as error_message:
                        print(f"Error: {error_message}")
                        continue
                    if action in ["Attack", "attack" "atk", "a"]:
                        damage = random.randint(2, 4) + player_stats["Strength"]
                        demon.health -= damage
                        print(f"You dealt {damage} damage to the demon!")
                    elif action in ["Use Item", "Use", "Item", "use item", "use", "u"]:
                        if len(inventory) > 0:
                            print(f"Which item do you want to use?")
                            display_inventory()
                            item_choice = get_choice(input("Enter the name of the item you want to use: ")) # how to add diffrent stats for diffrent items
                            use_item(item_choice)
                            if item_choice in ["Book of Magic", "Book", "BMG", "Magic", "book of magic", "book", "b"]:
                                demon.health = 0
                                extra_amount = random.randint(2, 4)
                                player_stats["Strength"] += extra_amount
                                print(f"You used the Book of Magic to create a beam of pure light which obliterted the demon and gained {extra_amount} strength!")
                        else:
                            print("You have no items to use!")
                    else:
                        print("Invalid action. Please choose again.")
                    print("The Demon attacks you!\n")

                    if demon.health > 0:
                        enemy_damage = random.randint(2, 5)
                        player_stats["Health"] -= enemy_damage
                        print(f"The Demon attacks you for {enemy_damage} damage!")
                        print(f"Your Health is now {player_stats['Health']}")
                    
                    if player_stats["Health"] <= 0:
                        print("You have been defeated by The Demon. Game Over.")
                        print("The Demon: Your skills are no match for me!'")
                        return
                    if demon.health <= 0:
                        print("You have defeated the demon!")
                        print("The Demon: NOOOOOO! This can't be...'")
                        print()
                        print("The old man guestures you to come to him.")
                        print()
                        old_man_minigame1()
                        counter = 1
                        break
                



            else:
                dialog = input("You travel past the strong hold and continue your journey...")
                counter = 1
            
            dialog = input("After travelling for 5 days you reach a village\n")
            dialog = input("The village however looks rundown with no signs of life. \nBefore you can even question it, thick fog fills the air.\n")
            dialog = input("Sunburst: 'Twilight... I sense old magic here. Be cautious.\n")

            while True:
                dialog = input("Your party debates where in the village to explore next!\n")
                dialog = input("1) Trixie: Twilight follow me to the Town Hall, I can see a faint blue light in the distance.\n")
                dialog = input("2) Starlight: Twilight follow me to the sound of water, There are tracks that lead there.\n")
                
                forest_choice = get_choice(input("Choose 1 or 2: "))
                print()
                # Trixie Path
                if forest_choice == "1":
                        dialog = input("\nYou follow Trixie into the Town Hall\n")
                        dialog = input("A magical barrier appears, blocking your way.\n")
                        dialog = input("Trixie: 'A magical challenge! The GREAT and POWERFUL Trixie allows YOU to solve it.'\n")

                        dialog = input("A voice Echos\nSolve my riddle to pass.")
                        dialog = input("\nRiddle: 'I speak without a mouth and hear without ears. I have no body,")
                        dialog = input("but I come alive with wind. What am I?'")

                        while True:
                            riddle_answer = get_choice(input("Your answer: "))
                            
                            if riddle_answer in ["echo", "Echo", "an echo", "An echo", "An Echo", "AN ECHO"]:
                                dialog = input("\nThe barrier dissolves into light.")
                                dialog = input("My name is Vayu, I have heard of you recent exploits.\nI know you are a foreginer from this land, but it seems you have been summoned to uphold Dharma!\nUse my astra to defeat your foes.\n")
                                dialog = input("Vayu bestows you an astra: **Vayavyastra**!")
                                dialog = input("The Vayavyastra brings a gale capable of lifting armies off the ground.\n")
                                add_to_inventory("Vayavyastra")
                                break
                            else:
                                print("The voice rejects your answer. Try again!\n")
                        break        
                    # Starlight Path
                elif forest_choice == "2":
                    dialog = input("\nYou follow Starlight toward the sound of rushing water.")
                    dialog = input("Starlight: 'Trust me, Twilight. My gut is telling me this is the way'.")
                    dialog = input("\nYou reach a glowring river. You hear voices in the distance reciting verses in a language unbeknownst to you ")
                    dialog = input("A sign reads 'Godavari Nadi'")
                    dialog = input("Starlight: 'I've heard about this river before, it is said to heal those who drink from it.'") 
                    heal_amount = random.randint(3, 6)
                    player_stats['Health'] += heal_amount
                    print(f"You drink from the river and feel restored! +{heal_amount} Health.")
                    print(f"Your health is now {player_stats['Health']}.")

                    dialog = input("\nStarlight: 'See? Told you I knew a better path.'")
                    dialog = input("You regroup with your party on the other side of the forest.\n")
                    break

                else:
                    print("Invalid choice. Choose 1 or 2.\n")
            print("-------------------------------------------------------------")
            dialog = input("While travelling through out of the village you get ambushed!")
            dialog = input("King of APES: 'You dare enter my village without my consent?'\n'Prepare to be taught a lesson'")    
            print(f"Entering combat...\n\n")

            manager = Enemy("Svenug", "Manager Blast", "King of APES", 25)
            turn_number = 0

            while manager.health > 0 and player_stats["Health"] > 0:
                    turn_number += 1
                    print(f"-----------Turn #{turn_number}------------")
                    print("King of APES health:", manager.health)
                    print(f"Your Health: {player_stats['Health']}")
                    try: 
                        action = get_choice(input("Do you want to (Attack) or (Use Item)? "))
                    except Exception as error_message:
                        print(f"Error: {error_message}")
                        continue
                    if action in ["Attack", "attack", "atk", "a"]:
                        damage = random.randint(2, 5) + player_stats["Strength"]
                        manager.health -= damage
                        print(f"You dealt {damage} damage to the King of APES!")
                    elif action in ["Use Item", "Use", "Item", "use item", "use", "u"]:
                        if len(inventory) > 0:
                            print(f"Which item do you want to use?")
                            display_inventory()
                            item_choice = get_choice(input("Enter the name of the item you want to use: ")) 
                            use_item(item_choice)
                            if item_choice in ["Book of Magic", "Book", "BMG", "Magic", "book of magic", "b"]:
                                damage = random.randint(2, 4)
                                manager.health -= damage
                                print(f"You used the Book of Magic to create a beam of pure light which dealt slight damage to the King of APES!")
                            elif item_choice in ["Sailastra", "S", "s", "Saila", "saila"]:
                                manager.health = manager.health
                                print(f"You used the Sailastra has no effect on the King of APES!")    
                            elif item_choice in ["Vayavyastra", "V", "v", "Vaya", "vaya"]:
                                manager.health = 0
                                extra_amount = random.randint(2, 4)
                                player_stats["Stamina"] += extra_amount
                                print(f"You used the Vayavyastra to create a gust of wind that swept the King of APES away!")
                        else:
                            print("You have no items to use!")
                    else:
                        print("Invalid action. Please choose again.")
                        print("The King of APES attacks you!\n")
                    if manager.health > 0:
                        enemy_damage = random.randint(8, 15)
                        player_stats["Health"] -= enemy_damage
                        print(f"The King of APES attacks you for {enemy_damage} damage!")
                        print(f"Your Health is now {player_stats['Health']}")
                    if player_stats["Health"] <= 0:
                        print("You have been defeated by the King of APES. Game Over.")
                        print("King of APES: 'Be greatful you were able to duel with the great KING of APES!'")
                        return
                    if manager.health <= 0:
                        print("You have defeated the King of APES!") 
                        print("King of APES: 'You'll pay for this!!!'")
            print("-------------------------------------------------------------")
            dialog = input("Sunburst: 'That was a close one Twilight; we haven't been here long but it seems that everyone wants to attack us!\n")
            dialog = input("Starlight: 'At least we found some new magic that can help us fight against these new foes.\n")
            dialog = input("Twilight: 'I keep seeing those symbols that were flashing on the portal all over the places we have discovered so far.'\n")
            dialog = input("Trixie: 'You might just be seeing things, after all its not the first time you've fallen for illusions.\n")
            dialog = input("Twilight: 'Either way we need to keep moving.'\n")
            print("-------------------------------------------------------------")
            dialog = input("Your party makes it to a tree, however before you can take a closer look a voice bellows your name.\n")
            dialog = input("Supreme Leader of Manassas: 'Twilight Sparkle, you may have bested my siblings, but you wont be able to defeat me that easily\n")

            print(f"Entering combat...\n\n")

            soapy = Enemy("SoapySensation", "Manager Blast", "Supreme Leader of Manassas", 50)
            turn_number = 0

            print("Each turn, one ally can assist you:")
            print("Sunburst = +2 Strength (this turn only)")
            print("Trixie = Deal -5 damage to Doogerlow")
            print("Starlight = Heal +8 HP\n")

            while soapy.health > 0 and player_stats["Health"] > 0:
                    turn_number += 1
                    print(f"-----------Turn #{turn_number}------------")
                    print("Supreme Leader of Manassas' health:", soapy.health)
                    print(f"Your Health: {player_stats['Health']}")

                    print("\nChoose an ally for this turn:")
                    print("(Sunburst / Trixie / Starlight / None)")
                    npc = input("Ally: ")

                    temp_strength = 0

                    if npc in ["Sunburst", "sunburst", "Sun", "sun"]:
                        temp_strength = 2
                        print("Sunburst boosts your magic! (+2 Strength this turn)")

                    elif npc in ["Trixie", "trixie", "t", "Great and Powerful", "great and powerful"]:
                        soapy.health -= 5
                        print("Trixie: 'Behold my GREAT and POWERFUL hex!' (-5 Supreme Leader of Manassas health)")

                    elif npc in ["Starlight", "Star", "star", "starlight"]:
                        player_stats["Health"] += 8
                        print("Starlight restores your energy! (+8 HP)")

                    elif npc == "None":
                        print("You fight without assistance this turn.")

                    else:
                        print("Invalid ally — no one assists you this turn.")

                    try: 
                        action = get_choice(input("Do you want to (Attack) or (Use Item)? "))
                    except Exception as error_message:
                        print(f"Error: {error_message}")
                        continue
                    if action in ["Attack", "attack", "atk", "a"]:
                        damage = random.randint(2, 5) + player_stats["Strength"] + temp_strength
                        soapy.health -= damage
                        print(f"You dealt {damage} damage to the Supreme Leader of Manassas!")
                    elif action in ["Use Item", "Use", "Item", "use item", "use", "u"]:
                        if len(inventory) > 0:
                            print(f"Which item do you want to use?")
                            display_inventory()
                            item_choice = get_choice(input("Enter the name of the item you want to use: ")) 
                            use_item(item_choice)
                            if item_choice in ["Book of Magic", "Book", "BMG", "Magic", "book of magic", "b"]:
                                damage = random.randint(6, 8)
                                soapy.health -= damage
                                print(f"You used the Book of Magic to create a beam of pure light which dealt slight damage to the Supreme Leader of Manassas!")
                            elif item_choice in ["Sailastra", "S", "s", "Saila", "saila"]:
                                damage = random.randint(6, 10)
                                soapy.health -= damage
                                print(f"You used the Sailastra to create a gust of wind that dealt damage to the Supreme Leader of Manassas!")   
                            elif item_choice in ["Vayavyastra", "V", "v", "Vaya", "vaya"]:
                                damage = random.randint(10, 15)
                                soapy.health -= damage
                                print(f"You used the Vayavyastra to create a gust of wind that dealt damage to the Supreme Leader of Manassas!")
                        else:
                            print("You have no items to use!")
                    else:
                        print("Invalid action. Please choose again.")
                        print("The Supreme Leader of Manassas attacks you!\n")
                    if soapy.health > 0:
                        enemy_damage = random.randint(8, 15)
                        player_stats["Health"] -= enemy_damage
                        print(f"The Supreme Leader of Manassas attacks you for {enemy_damage} damage!")
                        print(f"Your Health is now {player_stats['Health']}")    
                    if player_stats["Health"] <= 0:
                        print("You have been defeated by the Supreme Leader of Manassas. Game Over.")
                        print("Supreme Leader of Manassas: 'Revenge is a dish best served cold")
                        return
                    if soapy.health <= 0:
                        print("You have defeated the Supreme Leader of Manassas!") 
                        print("Supreme Leader of Manassas: 'My master will make you pay twilight... this war predates you and will continue after you cease to exist.'")

            print("-------------------------------------------------------------")
            dialog = input("Sunburst: 'Twilight, The Tree. It's glowing!'")
            dialog = input("***A celestial being emerges from the side.***\n")
            dialog = input("Aranyani: 'Thank you warrior for defeating the asura; I shall grant you a boon.'\n")
            dialog = input("Aranyani: 'You can ask for a wish form the Kalpavṛkṣa tree.'\n")
            dialog = input("Aranyani: 'I know that you were forced to come here; if you would like you can wish to return home with no recollection of this world or its events.\n")
            dialog = input("Aranyani: 'However, in the short time you have been here you have learned about the Astras, defeated asuras (the devil race) and upheld dharma.\n")
            dialog = input("Aranyani: 'It seems you have been called here for a reason; and in order to uphold dharma you will need learn the mantra (incantation) for the Brahmastra\n")
            dialog = input(BOLD + "The Brahmastra is termed as a fiery weapon that creates a fierce fireball,[1] blazing up with terrible flames and countless horrendous thunder flashes. When discharged, all nature including trees, oceans, and animals tremble.\n" + END)

            while True:
                dialog = input("Choose your wish:")
                dialog = input("1) Return to Equestria")
                dialog = input("2) Gain access to the Brahmastra\n")

                wish_choice = get_choice(input("Enter 1 or 2: "))

                # Wish Option 1 — Return Home
                if wish_choice == "1":
                    dialog = input("\nAranyani: 'Very well, Twilight Sparkle. Your journey ends here.'\n")
                    dialog = input("A radiant light surrounds you as the Kalpavṛkṣa tree opens a portal.\n")
                    dialog = input("You step through… and awaken back in Equestria, safe at last.\n")
                    dialog = input("----------- GAME OVER -----------")
                    dialog = input("Neutral Ending")
                    return  # Ends the game_story() function immediately

                # Wish Option 2 — Brahmastra
                elif wish_choice == "2":
                    dialog = input("\nAranyani: 'A difficult and dangerous choice… but you have earned it.'\n")
                    dialog = input("Aranyani: Repeat after me: Kalpavṛkṣa, aham bramastrasya dnyanam praptum ichami\n")
                    dialog = input("Twilight: 'Kalpavṛkṣa, aham bramastrasya dnyanam praptum ichami'\n")
                    dialog = input("A radiant light surrounds the field, you feel that you have been transported to another plane.\n")
                    print("-------------------------------------------------------------")
                    dialog = input("Hooded Figure: 'Welcome Twilight Sparkle, I have been awaiting your arrival.'\n")
                    dialog = input("Twilight: 'Where am I?'\n")
                    dialog = input("Hooded Figure: 'You are everyhwere but nowhere, this is just a mental image your mind has created.'\n")
                    dialog = input("Twilight: 'What am I doing here?'\n")
                    dialog = input("Hooded Figure: 'Did you not ask for the knowledege to invoke the Brahmastra?'\n")
                    dialog = input("Twilight: 'Yes but how will I attain this knowledge?'\n")
                    dialog = input("Hooded Figure: 'I will teach you, but first you must realize what you are fighting for.'\n")
                    dialog = input("Hooded Figure: 'Centuries ago, there was a war between Dharma and Adharma. The Kauravas and the Pandavas who fought for the right to a kingdom.\n")
                    dialog = input("Hooded Figure: 'Even the virtious Pandavas who upheld dharma won, adharma had seeped throughot the world.'\n")
                    dialog = input("Hooded Figure: 'Our current Yugam (period) is said to be the worst where Adharma will overcome Dharma.'\n")
                    dialog = input("Hooded Figure: 'It seems you have been sent here to slow that process down.'\n")
                    dialog = input("Twilight: 'Who are you? How do you know all of this?'\n")
                    dialog = input("Hooded Figure: 'Its better to show you...'\n")
                    dialog = input("*****The hooded figures eyes glow, and you get transported to a flashback*****\n")
                    print("-------------------------------------------------------------")
                    dialog = input("Arjuna: 'You are surrounded Ashwatthama, surrender now, the kauravas are defeated. You will pay for killing our sons!")
                    dialog = input("Ashwatthama: 'NO! I will complete my revenge Pandavas, you may have killed my father and suyodhana, but I will cause something that will cause sorrow for your entire reign.\n")
                    dialog = input("Ashwathama: ***repeats incantation to invoke the Brahmastra***\n")
                    dialog = input("Krishna: 'O Partha (Arjuna), Use your Brahmastra to counter Ashwathama's\n")
                    dialog = input("Vyasa: 'Both of you retract your Astras! This will cause the end of the world!\n")
                    dialog = input("***Arjuna Withdraws His Astra**\n")
                    dialog = input("Arjuna: 'Ashwathama, withdraw your Astra!'\n")
                    dialog = input("Krishna: 'How can one master a weapon if he never learned to retract it?'\n")
                    dialog = input("***Ashwathama aims his astra at Uttara's womb (who carried the future heir of the Pandavas).\n")
                    dialog = input("***Krishna revives the stillborn child***\n")
                    dialog = input("Krishna: 'Foolish Ashwathama, your henious act requires an equally henious punishment!'\n")
                    dialog = input("Krishna: 'You will roam the earth as a tormented, immortal figure until the end of the Kali Yuga, unable to die or find peace.'\n")
                    print("-------------------------------------------------------------")
                    dialog = input("***You awake at the foot of the tree, confused of what you just saw***\n")
                    dialog = input("You have gained the **Brahmastra** — the most powerful astra of the devas!")
                    add_to_inventory("Brahmastra")
                    print("\nYour journey continues, now armed with astral power...\n")
                    dialog = input("\nAranyani: 'Warrior, eveything you have done so has been upholding dharma and dimisnishing adharma.\n")
                    dialog = input("\nAranyani: 'However, there is one obstacle remaining, you must travel to the Himalayas and defeat Doogerlow.\n")

                    
                    break  # continue the story after gaining the weapon

                else:
                    print("Invalid choice. Please enter 1 or 2.\n")

            dialog = input("Your party embarks on journey to the Himalayas.\n")
            dialog = input("After weeks of travelling you rest at a clearing.\n")
            player_stats['Health'] =+ 50
            print("-------------------------------------------------------------")
            dialog = input("Trixie: 'Everypony... you've got to see this.'\n")
            dialog = input("Trixie: 'I was practicing my magic when I stumbled upon these ruins.'\n")
            dialog = input("Twilight: 'Those are the same symbols I saw from earl--'\n")
            dialog = input("Doogerlow: 'Finally, you've come to the right place.;\n")
            dialog = input("Doogerlow: 'You may have defeated my generals, but you have no idea the obstacles I have faced.'\n")
            dialog = input("Doogerlow: 'This war has been fought way before your universe was created and way after you will all cease to exist.'\n")
            dialog = input("Doogerlow: 'I am suprised that they sent you... it goes to show how desprate the devas are.'\n")
            dialog = input("Doogerlow: 'Either way I've waited centuries, one more battle is nothing in comparison.'\n")
            print(f"Entering combat...\n\n")

            dooger = BossEnemy("Doogerlow", "Super Saiyan", "Final Boss", "Vue Blast", "random")
            turn_number = 0

            print("Each turn, one ally can assist you:")
            dialog = input("Sunburst = +10 Strength (this turn only)")
            dialog = input("Trixie = Deal -15 damage to Doogerlow")
            dialog = input("Starlight = Heal +20 HP\n")

            while dooger.health > 0 and player_stats["Health"] > 0:
                    turn_number += 1
                    print(f"-----------Turn #{turn_number}------------")
                    print("Doogerlow health:", dooger.health)
                    print(f"Your Health: {player_stats['Health']}")

                    print("\nChoose an ally for this turn:")
                    print("(Sunburst / Trixie / Starlight / None)")
                    npc = input("Ally: ")

                    temp_strength = 0

                    if npc in ["Sunburst", "sunburst", "Sun", "sun"]:
                        temp_strength = 10
                        print("Sunburst boosts your magic! (+10 Strength this turn)")

                    elif npc in ["Trixie", "trixie", "t", "Great and Powerful", "great and powerful"]:
                        dooger.health -= 15
                        print("Trixie: 'Behold my GREAT and POWERFUL hex!' (-15 Doogerlow health)")

                    elif npc in ["Starlight", "Star", "star", "starlight"]:
                        player_stats["Health"] += 20
                        print("Starlight restores your energy! (+20 HP)")

                    elif npc == "None":
                        print("You fight without assistance this turn.")

                    else:
                        print("Invalid ally — no one assists you this turn.")


                    try: 
                        action = get_choice(input("Do you want to (Attack) or (Use Item)? "))
                    except Exception as error_message:
                        print(f"Error: {error_message}")
                        continue
                    if action in ["Attack", "attack", "atk", "a"]:
                        damage = random.randint(10, 15) + player_stats["Strength"] + temp_strength
                        dooger.health -= damage
                        print(f"You dealt {damage} damage to the Doogerlow!")
                    elif action in ["Use Item", "Use", "Item", "use item", "use", "u"]:
                        if len(inventory) > 0:
                            print(f"Which item do you want to use?")
                            display_inventory()
                            item_choice = get_choice(input("Enter the name of the item you want to use: ")) 
                            use_item(item_choice)
                            if item_choice in ["Brahmastra", "Brahma", "brahma"]:
                                dooger.health = 0
                                print("You unleash the Brahmastra! ")
                                print("A cosmic explosion obliterates Doogerlow instantly!")
                               #break
                            elif item_choice in ["Book of Magic", "Book", "BMG", "Magic", "book of magic", "b"]:
                                damage = random.randint(2, 4)
                                dooger.health -= damage
                                print(f"You used the Book of Magic to create a beam of pure light which dealt slight damage to Doogerlow!")
                            elif item_choice in ["Sailastra", "S", "s", "Saila", "saila"]:
                                damage = random.randint(6, 10)
                                dooger.health -= damage
                                print(f"You used the Sailastra to create a gust of wind that dealt damage to Doogerlow!")   
                            elif item_choice in ["Vayavyastra", "V", "v", "Vaya", "vaya"]:
                                damage = random.randint(6, 10)
                                dooger.health -= damage
                                print(f"You used the Vayavyastra to create a gust of wind that dealt damage to Doogerlow!")
                        else:
                            print("You have no items to use!")
                    else:
                        print("Invalid action. Please choose again.")
                        print("Doogerlow attacks you!\n")
                    if dooger.health > 0:
                        enemy_damage = random.randint(15, 25) 

                        # Vue Blast every other turn 
                    if turn_number % 2 == 0:
                        vue_blast_damage = enemy_damage // 2
                        total_damage += vue_blast_damage
                        print(f"Doogerlow uses Vue Blast! (+{vue_blast_damage} damage)")

                        player_stats["Health"] -= enemy_damage
                        print(f"The Doogerlow attacks you for {enemy_damage} damage!")
                        print(f"Your Health is now {player_stats['Health']}")    

                    if player_stats["Health"] <= 0:
                        print("You have been defeated by Doogerlow. Game Over.")
                        print("Doogerlow: 'Adharma will always win. I finally have enacted my revenge on the pandavas.'")
                        break
                    
                    if dooger.health <= 0:
                        print("You have defeated Doogerlow!") 
                        print("Doogerlow: 'Adharma always comes back, you may have defeated me this time... but be wary, other asuras will be on the hunt for you now.'\n")
                    
                    print("-------------------------------------------------------------")
                    dialog = input("From the ashes of Doogerlow, a ancient temple rises entirley made of gold\n")
                    dialog = input("Sunburst: 'Twilight… I feel an immense power inside. I think ... it's calling your name!\n")
                    dialog = input("Twilight: 'Sunburst, I hear it too, but I am conflicted on what we should do.' 'What do you all think I should do?'\n")

                    while True:
                        print("Who's advice do you wish to follow :")
                        dialog = input("1) Starlight: 'Twilight, we need to see this through Investigate the temple'")
                        dialog = input("2) Trixie: 'Twilight, I think you've accomplished your mission we should find a way home and walk away from the temple'.") #maybe change later

                        forest_choice = get_choice(input("Choose 1 or 2: "))
                        print()
                            # Starlight Path
                        if forest_choice == "1":
                                    dialog = input("\nTwilight: 'I need to know why it is calling my name.'")
                                    dialog = input("'You see a dog at the side of the entrance.'")

                                    has_magic_book = "Book of Magic" in inventory
                                    has_sailastra = "Sailastra" in inventory
                                    has_vayavyastra = "Vayavyastra" in inventory
                                    has_brahma = "Brahmastra" in inventory

                                    if has_magic_book and has_sailastra and has_vayavyastra and has_brahma:
                                        dialog = input("A beam of radiant light floods the chamber.\n")
                                        dialog = input("The dog shapeshifts into a man.\n")
                                        dialog = input("Dharmaraja: 'I have been following you very closely, Twilight Sparkle.'\n")
                                        print("Dharmaraja: 'I have heard of your tales in Equestria, and knew you would be the right choice to uphold dharma in this realm'\n")
                                        dialog = input("Dharmaraja: 'Altough your mission in equestira may be complete; you must uphold dharma in all the realms.'\n")
                                        dialog = input("Dharmaraja: 'Take this Navaratna (Nine-Jeweled) Necklace.' 'It is quite similar to you elements of harmony'\n")
                                        dialog = input("Dharmaraja: 'You will need to find others who uphold Dharma throught the realms to prepare for your final battle'\n")
                                        dialog = input("Dharmaraja: 'Good luck Twilight, dharma is counting on you!'\n")
                                        dialog = input(BOLD + "Twilight Sparkle has become the new weilder of the Navaratna Necklace, protector of all realms." + END)
                                        dialog = input("Dharmaraja: 'It is time to send you home warrior, you will need your rest.'\n")
                                        dialog = input("The entire room goes white.\n")
                                        print("-------------------------------------------------------------")
                                        dialog = input("Applejack: 'Twilight, Twilight, TWILIGHT!!!'\n")
                                        dialog = input("Your eyes slowly open...\n")
                                        dialog = input("Twilight: 'AJ!' 'What are you doing here?'\n")
                                        dialog = input("Applejack: 'Uhh... This is Sweet Apple Acres, what would'nt I be doing here?\n")
                                        dialog = input("Twilight: 'Woah!' 'Wait where is everypony else?'\n")
                                        dialog = input("Applejack: 'You mean Sunburst, Trixie and Starlight, no one has seen you 4 for weeks!\n")
                                        dialog = input("Twilight: 'If they are not here... then that means...'\n")
                                        dialog = input("Twilight: 'AJ, we need to hold an emergency meeting at the castle.'\n")
                                        dialog = input("-----------------------Some Time Later--------------------------")
                                        dialog = input("Twilight: 'I'm glad you all took your time to come here, I know we have all moved on... but I need you help.\n")
                                        dialog = input("Rarity: 'Anything for you darling'\n")
                                        dialog = input("Rainbow Dash: 'I am down to kick some butt any time!'\n")
                                        dialog = input("Fluttershy: 'I hope we meet new creatures!'\n")
                                        dialog = input("Pinkie-Pie: 'Awwww.. I was really hoping for a party'\n")
                                        dialog = input("Twilight: 'Pinkie, I promise ill throw a big party if we complete this mission.\n")
                                        dialog = input("Twilight: 'Time is of the essence, we need to find Sunburst, Trixie and Starlight. \n")
                                        dialog = input("The Mane 5: We won't let you down Twilight!\n")
                                        print("----------- GAME OVER -----------")
                                        print("\nTo be continued... (Hero Ending)")
                                        quit()

                                    else:
                                        twilight_dream_ending()
                                        break

                        elif forest_choice == "2":
                            twilight_dream_ending()
                            break
                                            

        

def get_choice(user_input):
    print("Getting your choice...")
    return str(user_input)

def add_to_inventory(item):
    print(f"{item} was added to your inventory!")
    inventory.append(item)

def display_inventory():
    global inventory
    print("Inventory: \n", inventory)

def twilight_dream_ending():
                                            print("The entire room goes white.")
                                            dialog = input("Twilight: 'HUH?, 'Was that just a dream?', 'Where is everybody?'\n")
                                            dialog = input("Spike: 'You're awake! 'We were getting really worried about you, It looks like you came down with a bad case of the flu.\n")
                                            dialog = input("Twilight: 'Spike, it felt so real, I went to a far away land, defeated villans collected astras...'\n")
                                            dialog = input("Spike: 'It may be cause you were reading this book the night before: 'The Mahabharata: The battle between Dharma and Adharma'\n")
                                            dialog = input("Twilight: 'I don't remeber ever having this book.' 'Spike you know how I never misplace my precious books!'\n")
                                            dialog = input("Spike: 'I must have gave you to much cough medicine.' 'Heh-heh'\n")
                                            dialog = input("Twilight: 'Spike, I know I am not going CRAZY!' 'I just need to get out of bed and do more research about this.'\n")
                                            dialog = input("Spike: 'Woah there!' 'You still need some bed-rest, doctors orders.' 'Plus we can catch up on my favorite show now'\n")
                                            dialog = input("Twilight: Ugh....")
                                            dialog = input("While looking out the window you see the dog from the temple out on the streets.\n")
                                            dialog = input("Dharmaraja: 'I have been following you very closely, Twilight Sparkle.'\n")
                                            dialog = input("Dharmaraja: 'I have heard of your tales in Equestria, and knew you would be the right choice to uphold dharma in my realm'\n")
                                            dialog = input("Dharmaraja: 'However you may require more time learning about the astras in order for you to defeat adharma.'\n")
                                            dialog = input("Twilight: 'I promise, I will research as much as I can, but I don't know where to start.\n")
                                            dialog = input("Dharmaraja: 'Watch the show witch Spike, there is more to it then it may seem at first glance.'\n")
                                            dialog = input("As you turn to the TV you see the screen changing, and those same symbols from before appear.\n")
                                            dialog = input("However, you are miraculously able to read the symbols which translate to 'Kurukshetra'.\n")
                                            print("----------- GAME OVER -----------")
                                            print("\nLot to learn Ending")

class Enemy:
    def __init__(self, name, weapon, enemy_type, health="random"):
        self.name = name
        self.weapon = weapon
        self.enemy_type = type
        
        # RANDOM HEALTH
        if health == "random":
            self.health = random.randint(100, 150)

        # HEALTH RANGE (TUPLE) ask prof
        elif type(health) == tuple:
            self.health = random.randint(health[0], health[1])

        # FIXED HEALTH
        else:
            self.health = health

    def enemy_stat(self):
        return f"\nEnemy name: {self.name}\nEnemy weapon: {self.weapon}\nEnemy type: {self.type}\n"    

class BossEnemy(Enemy):
    def __init__(self, name, weapon, enemy_type, superpower, health):
        self.superpower = superpower
        super().__init__(name, weapon, enemy_type, health)
    
    def boss_power(self): 
        return f"\nBoss uses {self.superpower} to do damage to you!\nYou take *** damage..."


class NPC:
    def __init__(self, name, job, dialogue, weaponOrTool):
        self.name = name
        self.job = job
        self.dialogue = dialogue
        self.weapon = weaponOrTool
        
    def talk(self):
        print(f"{self.name}, ({self.job}): {self.dialogue}")


def old_man_minigame1():
    while True:
         
        dialog = input("\nThe old man smiles at you.\n")
        dialog = input("Old Man: 'Thank you for saving me, young one. You seem to be a skilled warrior.\n")
        dialog = input("Old Man: 'I have seen many warriors like you throughout the ages, you reminde me of my younger self\n")
        dialog = input("Old Man: 'Answer my questions, and I shall grant you the knowledge to call an Astra (weapon) in battle. The same ones that were used in the Kurukshetra'\n")

        # Question and choices
        print("Question: What is the 3rd Melakarta raga?")
        print("A) Gānamūrti")
        print("B) Kanakāngi")
        print("C) Hanumatodi")
        print("D) Māyāmāḻavagowla")

        answer = get_choice(input("Your answer (A, B, C, or D): "))
        
        correct_list = ["a", "ganamurti", "gana", "Gana", "A", "Ganamurti"]
        
        found_correct = False
        for x in correct_list:
            if answer == x:
                found_correct = True
                break # exits loop when found correct

        if found_correct:
            print("\nOld Man: 'Correct! You truly possess wisdom.'")
            dialog = input("He grants you an incantation to summon the Sailastra (it can help you expell heavy winds (hurricanes, ect)!")
            add_to_inventory("Sailastra")
            print()
            break # exit entire mini game
        else:
            print("\nOld Man: 'Incorrect. Wisdom is earned slowly… but you will learn in time.'") 


def use_item(item):
    print(f"Your item being used: {item}")
main()

