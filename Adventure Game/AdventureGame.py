class AdventureGame:

    def __init__(self):
        self.chooseScenario()

    def chooseScenario(self):

        print("\n-----------------------------")
        print("Welcome to the Adventure Game")
        print("-----------------------------\n")
        userName = str(input("Please enter your name for the game: "))
        print("")

        print("Choose your adventure:")
        print("1. Enchanted Forest")
        print("2. Castle Escape")
        print("3. Space Mission")

        print("")
        
        while True:
            try:
                choice = int(input("Please select your adventure: "))
                match choice:
                    case 1:
                        self.forestStart(userName)
                    case 2:
                        self.castleStart(userName)
                    case 3:
                        self.spaceStart(userName)
                    case _:
                        print("Error: Please choose from option 1 to 3.")
                        continue
                    
                break
            
            except:
                print("Error: Please add integer and select from 1 to 3.")

    def forestStart(self,userName):
        print("\n----------------------------------------------------------------------------------------")
        print(f"Hi, {userName} ,Welcome to the story of Enchanted Forest")
        print("You enter a mysterious forest with glowing trees and the sound of whispering wind." 
        "\nYou are walking through the forest and reach a point where the path splits." 
        "\n\nNow yo have two options to choose:" 
        "\n1. Follow a Glowing path" 
        "\n2. Follow a Dark Trail")

        while True:
            try:
                userInput = int(input("Please select which path you want to go? (1 or 2): "))
                match userInput:
                    case 1:
                        print("\nYou follow the glowing path and encounter a wise old elf.")
                        print("He offers to guide you through the forest.")

                        print("\n1. Trust the elf")
                        print("2. Run away from the elf")

                        while True:
                            inputElf = int(input("Please select which path you want to go? (1 or 2): "))

                            match inputElf:
                                case 1:
                                    print("\nThe elf smiles and hands you a magical stone.")
                                    print("It glows brightly and teleports you to safety.")
                                    print("🎉 Congratulations, you WIN the Enchanted Forest adventure!")
                                
                                case 2:
                                    print("\nYou run blindly into the woods and fall into a hidden pit.")
                                    print("You’re trapped with no way out.")
                                    print("💀 You LOST the Enchanted Forest adventure.")
                                
                                case _:
                                    print("\nInvalid choice. The forest spirits get confused and whisk you away.")
                                    print("💀 You LOST due to indecision.")

                            break
                    
                    case 2:
                        print("\nYou bravely step into the dark trail.")
                        print("Suddenly, shadow wolves leap out from the bushes and surround you.")
                        print("💀 You LOST the Enchanted Forest adventure.")

                    case _:
                        print("Error: Please choose from option 1 or 2.")
                        continue
                break
                        
            except:
                print("Error: Please choose from option 1 or 2.")
                continue

    def castleStart(self,userName):
        print("\n----------------------------------------------------------------------------------------")
        print(f"Hi {userName}, Welcome to the story of Castle Escape")
        print("You wake up in a dimly lit dungeon inside a medieval castle."
            "\nChains rattle, and distant screams echo through the stone walls."
            "\nYou see a rusty door slightly open and a narrow hole in the wall.")

        print("\nNow you have two options to choose:"
            "\n1. Sneak through the hole in the wall"
            "\n2. Push open the rusty door")

        while True:
            try:
                userInput = int(input("Please select your escape route (1 or 2): "))
                match userInput:
                    case 1:
                        print("\nYou crawl through the narrow hole and find yourself in the castle's armory.")
                        print("A friendly guard sleeping nearby stirs as you enter.")

                        print("\n1. Try to tiptoe past him")
                        print("2. Wake him and ask for help")

                        while True:
                            try:
                                inputGuard = int(input("What will you do? (1 or 2): "))
                                match inputGuard:
                                    case 1:
                                        print("\nAs you sneak past, your foot knocks over a sword.")
                                        print("The guard wakes up and catches you immediately.")
                                        print("💀 You LOST the Castle Escape adventure.")
                                        break
                                    case 2:
                                        print("\nThe guard wakes with a start but listens to your plea.")
                                        print("He remembers your kindness from before and helps you escape through a secret passage.")
                                        print("🎉 Congratulations, you WIN the Castle Escape adventure!")
                                        break
                                    case _:
                                        print("\nYou freeze, unable to decide. The guard wakes and raises the alarm.")
                                        print("💀 You LOST due to hesitation.")
                                        break
                            except ValueError:
                                print("Error: Please choose 1 or 2.")
                                continue
                    case 2:
                        print("\nYou push the rusty door open and it creaks loudly.")
                        print("A guard on patrol hears the sound and storms in.")
                        print("💀 You LOST the Castle Escape adventure.")
                    case _:
                        print("Error: Please choose from option 1 or 2.")
                        continue
                break
            except ValueError:
                print("Error: Please choose from option 1 or 2.")
                continue

    def spaceStart(self,userName):
        print("\n----------------------------------------------------------------------------------------")
        print(f"Hi {userName}, Welcome to the story of Space Mission")
        print("You are aboard the spaceship *Nova-9*, orbiting an unknown planet."
            "\nSuddenly, an alarm blares — the engine has failed, and oxygen levels are dropping.")

        print("\nYou have two options to survive:"
            "\n1. Attempt emergency repairs on the engine"
            "\n2. Send a distress signal to the nearby alien ship")

        while True:
            try:
                userInput = int(input("Please select your action (1 or 2): "))
                match userInput:
                    case 1:
                        print("\nYou grab your toolkit and rush to the engine room.")
                        print("Sparks fly as you open the panel — you must act fast.")

                        print("\n1. Replace the damaged capacitor")
                        print("2. Bypass the circuit manually")

                        while True:
                            try:
                                inputFix = int(input("What will you do? (1 or 2): "))
                                match inputFix:
                                    case 1:
                                        print("\nThe new capacitor fits perfectly.")
                                        print("The engine roars back to life, and the ship stabilizes.")
                                        print("🎉 Congratulations, you WIN the Space Mission adventure!")
                                        break
                                    case 2:
                                        print("\nYour manual bypass overloads the system.")
                                        print("The engine explodes, and the ship breaks apart.")
                                        print("💀 You LOST the Space Mission adventure.")
                                        break
                                    case _:
                                        print("\nYou freeze, unsure of what to do.")
                                        print("The engine fire spreads uncontrollably.")
                                        print("💀 You LOST due to indecision.")
                                        break
                            except ValueError:
                                print("Error: Please choose 1 or 2.")
                                continue
                    case 2:
                        print("\nYou send a signal, but the alien ship sees it as a threat.")
                        print("They fire back instantly, destroying your ship.")
                        print("💀 You LOST the Space Mission adventure.")
                    case _:
                        print("Error: Please choose from option 1 or 2.")
                        continue
                break
            except ValueError:
                print("Error: Please choose from option 1 or 2.")
                continue


adventure = AdventureGame()
        


