import random
from time import sleep

# color codes to make money stand out easier, color codes found on stack overflow, uses
# escape codes to modify how text is printed. White acts as a reset after the
# desired code is printed.
green = '\033[32m'
white = '\033[0m'

# each question is in increasing order or difficulty from 1-26 with each tier having 2 questions. Respective answers and responses are ordered the same by index.
questions = ["What color are school buses in the United States?",
"Which animal is known as ‘man’s best friend’?",
"What planet is known as the Red Planet?",
"In which sport would you use a racket?",
"What is the smallest planet in our solar system?",
"What is the name of the cowboy in Toy Story?",
"What is the capital of Canada?",
"What is the largest mammal in the world?",
"Which continent is the Sahara Desert located on?",
"What is the main ingredient in guacamole?",
"What is the chemical symbol for gold?",
"Who was the first president of the United States?",
"In what year did the Titanic sink?",
"What is the longest-running Broadway show of all time?",
"What element does ‘O’ represent on the periodic table?",
"What U.S. city is known as the “Windy City”?",
"Which famous scientist developed the three laws of motion?",
"Which famous artist cut off part of his own ear?",
"What is the hardest natural substance on Earth?",
"Who was the most significant British politician during World War II?",
"Which gas makes up the majority of the Earth’s atmosphere?",
"What is the capital of South Korea?",
"What is the currency of Japan?",
"What language has the most native speakers worldwide?",
"What is the longest river in South America?",
"Who was the second man to walk on the Moon?",
"In computing, what does “CPU” stand for?",
"What year did the United States declare independence?",
"What is the most commonly spoken language in Brazil?",
"What is the term for animals that eat only plants?",
"What is the name of the ship that brought the Pilgrims to America in 1620?",
"Who formulated the theory of general relativity?",
"In what year was the United Nations founded?",
"Who was the first woman to win a Nobel Prize?",
"What organ is primarily responsible for detoxifying chemicals in the human body?",
"Who was the Roman god of war?",
"What is the largest island in the world?",
"In Greek mythology, who is the king of the gods?",
"Who was the first female Prime Minister of the United Kingdom?",
"What is the largest desert in the world?",
"What is the capital of Brazil?",
"What year did the Titanic sink?",
"What is the name of the largest volcano on Earth?",
"Which country is home to the city of Machu Picchu?",
"Who is credited with inventing the first successful airplane?",
"Who was the first emperor of China?",
"Which civilization built the pyramids of Giza?",
"In Greek mythology, who was the hero who completed the twelve labors?",
"Which famous explorer was the first to circumnavigate the globe?",
"In what country would you find the ancient city of Petra?",
"Which famous historical figure was known as the “Conqueror”?",
"Which ancient civilization is credited with creating the first written language?"]

options_a = ["A) Red", "A) Cat", "A) Venus", "A) Soccer", "A) Earth", "A) Buzz", "A) Toronto", "A) Elephant", "A) Asia", "A) Tomato",
"A) Au", "A) Abraham Lincoln", "A) 1905", "A) The Lion King", "A) Oxygen", "A) Boston", "A) Galileo Galilei", "A) Claude Monet",
"A) Steel", "A) Neville Chamberlain", "A) Oxygen", "A) Tokyo", "A) Yuan", "A) English", "A) Amazon River", "A) Neil Armstrong",
"A) Central Programming Unit", "A) 1775", "A) Spanish", "A) Omnivores", "A) Santa Maria", "A) Isaac Newton", "A) 1919",
"A) Rosalind Franklin", "A) Kidneys", "A) Mars", "A) Greenland", "A) Apollo", "A) Queen Elizabeth II", "A) Sahara Desert",
"A) Rio de Janeiro", "A) 1910", "A) Mount Vesuvius", "A) Mexico", "A) Charles Lindbergh", "A) Qin Shi Huang", "A) Romans",
"A) Achilles", "A) Christopher Columbus", "A) Egypt", "A) Julius Caesar", "A) Sumerians"]

options_b = ["B) Blue", "B) Horse", "B) Mars", "B) Tennis", "B) Mercury", "B) Woody", "B) Montreal", "B) Blue Whale", "B) South America", "B) Avocado",
"B) Ag", "B) John Adams", "B) 1912", "B) Wicked", "B) Osmium", "B) Chicago", "B) Isaac Newton", "B) Pablo Picasso",
"B) Quartz", "B) Winston Churchill", "B) Carbon Dioxide", "B) Beijing", "B) Yen", "B) Spanish", "B) Paraná River", "B) Michael Collins",
"B) Computer Processing Unit", "B) 1776", "B) English", "B) Herbivores", "B) Mayflower", "B) Albert Einstein", "B) 1939",
"B) Ada Lovelace", "B) Stomach", "B) Jupiter", "B) Australia", "B) Hades", "B) Theresa May", "B) Gobi Desert",
"B) São Paulo", "B) 1912", "B) Mauna Loa", "B) Peru", "B) Orville and Wilbur Wright", "B) Genghis Khan", "B) Greeks",
"B) Hercules", "B) Marco Polo", "B) Israel", "B) Alexander the Great", "B) Egyptians"]

options_c = ["C) Yellow", "C) Dog", "C) Jupiter", "C) Baseball", "C) Mars", "C) Andy", "C) Ottawa", "C) Giraffe", "C) Africa", "C) Lettuce",
"C) Gd", "C) George Washington", "C) 1918", "C) Phantom of the Opera", "C) Ozone", "C) New York", "C) Albert Einstein", "C) Vincent van Gogh",
"C) Diamond", "C) Margaret Thatcher", "C) Nitrogen", "C) Seoul", "C) Won", "C) Hindi", "C) Orinoco River", "C) Yuri Gagarin",
"C) Central Processing Unit", "C) 1783", "C) French", "C) Carnivores", "C) Beagle", "C) Niels Bohr", "C) 1945",
"C) Marie Curie", "C) Liver", "C) Apollo", "C) Borneo", "C) Zeus", "C) Margaret Thatcher", "C) Kalahari Desert",
"C) Brasília", "C) 1915", "C) Mount St. Helens", "C) Brazil", "C) Leonardo da Vinci", "C) Emperor Wu", "C) Egyptians",
"C) Odysseus", "C) Ferdinand Magellan", "C) Jordan", "C) Genghis Khan", "C) Indus Valley Civilization"]

options_d = ["D) Green", "D) Parrot", "D) Saturn", "D) Basketball", "D) Pluto", "D) Rex", "D) Vancouver", "D) Orca", "D) Australia", "D) Onion",
"D) Go", "D) Thomas Jefferson", "D) 1923", "D) Les Misérables", "D) Orpiment", "D) San Francisco", "D) Nikola Tesla", "D) Salvador Dalí",
"D) Obsidian", "D) Tony Blair", "D) Hydrogen", "D) Pyongyang", "D) Peso", "D) Chinese", "D) São Francisco River", "D) Buzz Aldrin",
"D) Central Performance Unit", "D) 1789", "D) Portuguese", "D) Insectivores", "D) Discovery", "D) Stephen Hawking", "D) 1955",
"D) Florence Nightingale", "D) Lungs", "D) Vulcan", "D) Madagascar", "D) Hermes", "D) Mary Robinson", "D) Antarctic Desert",
"D) Buenos Aires", "D) 1920", "D) Mount Kilimanjaro", "D) Argentina", "D) Amelia Earhart", "D) Liu Bang", "D) Mayans",
"D) Perseus", "D) Vasco da Gama", "D) Syria", "D) William the Conqueror", "D) Babylonians"]

key = ["C", "C", "B", "B", "B", "B", "C", "B", "C", "B", "A", "C", "B", "C", "A", "B", "B", "C", "C", "B",
"C", "C", "B", "D", "A", "D", "C", "B", "D", "B", "B", "B", "C", "C", "C", "A", "A", "C", "C", "D",
"C", "B", "B", "B", "B", "A", "C", "B", "C", "A", "D", "A"]

s_question =  ["What is the square root of 144?",
"What is 11 × 12?",
"If x + 5 = 13, what is x?",
"If you divide 72 by 8, then add 9, what’s the result?",
"What is 13²?",
"How much is 0.5 + 0.25 + 1.25?",
"If 3x = 27, what is x?",
"If a pizza has 8 slices and you eat 3, how many are left?",
"If a = 7 and b = 3, what is (a² - b²)?",
"What is 15% of 80?",
"What is 20% of 120?",
"What is 10% of 250 plus 20% of 150?",
"If a shirt costs $40 and is discounted by 25%, what is the sale price?",
"If 6 pens cost $9, how much do 4 pens cost at the same rate?",
"If a book is $12 and you buy 3, how much change do you get from $50?",
"What is ¾ of 64?",
"What is 1/3 of 90 plus 1/6 of 60?",
"If a car travels 60 miles in 1 hour, how far does it travel in 2.5 hours?",
"What is the next prime number after 29?",
"If 5⁴ = ?, what is the answer?"]

s_key = [12, 132, 8, 18, 169, 2, 9, 5, 40, 12, 24, 55, 30, 6, 14, 48, 55, 150, 31, 625]

class Case:
    def __init__(self, number, value, difficulty):
        self.number = number
        self.value = value
        self.difficulty = difficulty
        self.question = ""
        self.option_a = ""
        self.option_b = ""
        self.option_c = ""
        self.option_d = ""
        self.key = ""
        self.isEmpty = False

    def get_number(self):
        return self.number

    def set_number(self, x):
        self.number = x

    def get_value(self):
        return self.value

    def set_value(self, x):
        self.value = x

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self, x):
        self.difficulty = x

    def set_question(self, question, a, b, c, d, key):
        self.question = question
        self.option_a = a
        self.option_b = b
        self.option_c = c
        self.option_d = d
        self.key = key

    def __str__(self):
        return f"Case: {self.number}, Value: ${format(self.value, ',')}"

    def print_value(self):
        return f"${format(self.value, ',')}"

    def print_case(self):
        return str(self.number)

    def ask_question(self):
        print(f"Diff: {self.difficulty}")
        print(f"Here's the question in the case:\n{self.question}\n{self.option_a}\n{self.option_b}\n{self.option_c}\n{self.option_d}\n")

        while True:
            try:
                response = input("Select the correct answer: ")
                response = response.upper()
                if response == self.key:
                    print("Correct! The money from this case has been added to the pool.")
                    return True

                # if the user selects swap then they win the money in the other case
                elif response in ("A","B","C","D"):
                    print("Sorry, that is not correct.")
                    print(f"The correct answer was {self.key}")
                    return False

                else:
                    print("Choice invalid, try again.")

            except ValueError:
                print("Choice invalid, try again.")

class MathCase(Case):
    def __init__(self, number, value, difficulty):
        super().__init__(number, value, difficulty)

    def set_question(self, question, a, b, c, d, key):
        self.question = question
        self.key = key

    def __str__(self):
        return f"Case: {self.number}, Value: ${format(self.value, ',')}**"

    def ask_question(self):
        print(f"--**MATH CHALLENGE**--")
        print(f"Here's the question in the case:\n{self.question}\n")

        while True:
            try:
                response = int(input("Type in the correct answer without commas or spaces: "))
                if response == self.key:
                    print("Correct! The money from this case has been added to the pool.")
                    return True

                else:
                    print("Sorry, that is not correct.")
                    print(f"The correct answer was {self.key}")
                    return False

            except ValueError:
                print("Choice invalid, try again.")

def select_question(i):
    if case_objects[i].__class__.__name__ == "MathCase":
        rand = random.randint(0, len(s_question))
        case_objects[i].set_question(s_question[rand], "", "", "", "", s_key[rand])
        correct = case_objects[i].ask_question()
    else:
        rand = random.randint(0, 1)
        print((case_objects[i].difficulty * 2) + rand - 1)
        case_objects[i].set_question(questions[(case_objects[i].difficulty * 2) + rand - 2],
                                     options_a[(case_objects[i].difficulty * 2) + rand - 2],
                                     options_b[(case_objects[i].difficulty * 2) + rand - 2],
                                     options_c[(case_objects[i].difficulty * 2) + rand - 2],
                                     options_d[(case_objects[i].difficulty * 2) + rand - 2],
                                     key[(case_objects[i].difficulty * 2) + rand - 2])
        correct = case_objects[i].ask_question()

    return correct

def displayValues(values):
    """
    Displays the values left in the game in an appealing way.
    Inputs:  (list of all values remaining)
    Output: None
    """

    print("\n------VALUES------")

    # prints all integers in formatted commas and dollar signs with appropriate padding
    # according to length
    for i in range(13):
        if case_objects[i].isEmpty:
            print(end="       | ")
        elif len(str(values[i])) == 1:
            print(f"${values[i]}", end="     | ")
        elif len(str(values[i])) == 2:
            print(f"${values[i]}", end="    | ")
        elif len(str(values[i])) == 3:
            print(f"${values[i]}", end="   | ")
        elif len(str(values[i])) == 4:
            print(f"${values[i]}", end="  | ")
        elif len(str(values[i])) == 5:
            print(f"${values[i]}", end=" | ")
        elif len(str(values[i])) == 6:
            print(f"${values[i]}", end="| ")
        else:
            print(f"${values[i]}", end=" ")
        if case_objects[i + 13].isEmpty:
            print()
        else:
            # format function is used here to give the integer an appearance of monetary
            # value, similar to how it is in the game. It splits every 3 digits with
            # what is contained in the quote.
            print(f"${format(values[i + 13], ',')}")
    print()

    # sleep function from time module adds delay for visual effect by pausing the program
    sleep(1.5)


def displayCases():
    """
    Displays the remaining cases in the game in an appealing way.
    Inputs:  (list of all cases remaining)
    Output: None
    """

    print("\n--------CASES---------")
    for i in range(26):
        if case_objects[i].number == 0 and (i + 1) % 6 == 0:
            print("")
        elif case_objects[i].number == 0:
            print("", end="    ")
        elif (i + 1) % 6 == 0:
            print(case_objects[i].number)
        elif (i + 1) < 10:
            print(case_objects[i].number, end="   ")
        else:
            print(case_objects[i].number, end="  ")
    print()
    sleep(1.5)


def playRound(currentRound, pool, values):
    """
    Starts a new round of the game, and .
    Inputs: caseList (list of all cases remaining)
    Output: None
    """
    print("---------------------")
    print(f"|      ROUND {currentRound}      |")
    print("---------------------\n")
    print(f"The size of the pool is {green}${format(pool, ',')}{white}")
    print(f"Your case is: {my_case}\n")

    # the amount of cases remaining descends from 6 each round until it gets to one which
    # stays that way until the end
    if currentRound == 1:
        casesLeft = 6
    elif currentRound == 2:
        casesLeft = 5
    elif currentRound == 3:
        casesLeft = 4
    elif currentRound == 4:
        casesLeft = 3
    elif currentRound == 5:
        casesLeft = 2
    else:
        casesLeft = 1

    for i in range(casesLeft, 0, -1):
        print(f"Cases left to open: {i}")
        while True:
            try:
                caseSelection = int(input("\nSelect a case: "))
                is_found = False
                for i in range(26):
                    if caseSelection == case_objects[i].number:
                        print(f"Case {case_objects[i].number} has {green}{case_objects[i].print_value()}{white} in it.")
                        correct = select_question(i)
                        if correct:
                            pool += case_objects[i].value
                        else:
                            pass
                        is_found = True
                        case_objects[i].value = 0
                        case_objects[i].number = 0
                        case_objects[i].isEmpty = True
                    else:
                        pass
                """"""
                if is_found:
                    break
                else:
                    print("Please select a case on the board.")

            # try-except loop will catch anyone typing something other than an integer that
            # cannot be compared in math
            except ValueError:
                print("Please select a case on the board.")

        displayCases()
        displayValues(values)

    return pool


def banker(values, currentRound, previousOffers, pool):
    """
    Initiates a deal from the banker at the end of each round.
    Inputs: Remaining values, the current round, and all previous offers
    Output: Previous offers with new offer added
    """

    print("The banker is calling! He wants to offer you a deal.")
    mean = 0
    n = 0
    offer = 0

    # adds all values still in the game to the total and creates a count of all of them
    for i in values:
        if i == " ":
            pass
        else:
            mean += i
            n += 1

    mean = (mean + (pool*0.5) / n + 1)

    # increases value of deal per round based on an increasing percentage of the average
    # algorithm comes from my research of a few deal or no deal games in real life
    if currentRound == 1:
        offer = mean * 0.2

    elif currentRound == 2:
        offer = mean * 0.3

    elif currentRound == 3:
        offer = mean * 0.45

    else:
        offer = mean * 0.5
    offer = round(offer)

    sleep(1)
    print(f"\nYour offer is: {green}${format(offer, ',')}{white}")

    # shows previous offers past round 1
    if round != 1:
        print("\nYour previous offers: ")
        for i in previousOffers:
            print(f"${format(i, ',')}")

    print("\nType 'DEAL' to accept the offer, or type 'NO DEAL' to reject it.")

    # request user to accept deal or not by typing deal or no deal
    while True:
        response = input("\nDeal or No Deal? ")
        response = response.upper()
        if response == "DEAL":
            print(f"\nYou have selected 'DEAL'. The case you were holding on to had {green}${format(case_objects[my_case - 1].value, ',')}{white} in it.")
            if case_objects[my_case - 1].value >= 100000:
                correct = select_question(my_case)
                if correct:
                    print(f"\nCongratulations! You have won {green}${format(offer, ',')}{white}!")
                else:
                    print(f"Sorry, you dont get any money.")
            else:
                print(f"\nCongratulations! You have won {green}${format(offer, ',')}{white}!")
            exit()
        elif response == "NO DEAL":
            print("\nYou have entered 'NO DEAL'. The game will now proceed to the next round.")
            break
        else:
            print("\nYou may only select 'DEAL' or 'NO DEAL'. Try again.")

    # adds offer to previous offers list
    previousOffers.append(offer)
    return previousOffers


# defined values
currentRound = 0
casesLeft = 0
previousOffers = []
caseList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26]
values = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000,
          10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000,
          750000, 1000000]
difficulties =  {0.01: 1, 1: 2, 5: 3, 10: 4, 25: 5, 50: 6, 75: 7, 100: 8, 200: 9, 300: 10, 400: 11, 500: 12, 750: 13,
    1000: 14, 5000: 15, 10000: 16, 25000: 17, 50000: 18, 75000: 19, 100000: 20, 200000: 21, 300000: 22, 400000: 23,
    500000: 24, 750000: 25, 1000000: 26}

valuesRandom = values.copy()
pool = 0

case_objects = []

# setting the randomized list of values to pair to each case index respectively
random.seed(None)
random.shuffle(valuesRandom)


for i in range(26):
    rand = random.randint(0, 10)
    if rand == 10:
        case_objects.append(MathCase(caseList[i], valuesRandom[i], difficulties[valuesRandom[i]]))
    else:
        case_objects.append(Case(caseList[i], valuesRandom[i], difficulties[valuesRandom[i]]))
def print_all(case_objects):
    for i in range(26):
        print(case_objects[i])
        print(case_objects[i].__class__.__name__)
print_all(case_objects)


# intro
print("Welcome to Deal or No Deal! I am your host, Howie Mandel.\n\n"
      "Here are the rules:\n\n"
      " - You will be presented with a board with a list of cases.\n"
      " - Then you'll be asked to select a case to keep until the end of the game.\n"
      " - Then you will be asked to select a number of cases to open.\n"
      " - You must answer a trivia question whose difficulty is based on its value.\n"
      " - This will repeat until you either have taken a deal from the banker, or\n"
      "   you have opened all the cases.\n\n"
      "Good luck!\n")

input("Press enter to continue...")

displayCases()

# game initiation to select a case to keep, hoping it has the million in it
while True:
    try:
        my_case = int(input("\nSelect a case to hold on to for the rest of the game: "))

        if my_case > 26 or my_case < 1:
            print("\n*** Invalid input. Please enter a number between 1 and 26. ***")

        else:
            break

    # try-except loop will catch anyone typing something other than an integer that
    # cannot be compared in math
    except ValueError:
        print("\n*** Invalid input. Please enter a number between 1 and 26. ***")

# empties the selection in the number only since it is still an unknown value
case_objects[my_case-1].number = 0

# displaying both makes it easy for the user to see changes and refer to the board
displayCases()
displayValues(values)

# initiates round 1
currentRound = 1

# cycles the round structure up until round 9
while currentRound <= 9:
    pool = playRound(currentRound, pool, values)
    previousOffers = banker(values, currentRound, previousOffers, pool)
    currentRound += 1

# final aspect of the game forces the user to keep their case or trade it
print("\nOnly one case remains. You can now choose to keep your current case, or take\n"
      "home the other case on the board. What will you do?")

while True:
    try:
        finalChoice = input("\nType 'KEEP' or 'QUESTION': ")
        finalChoice = finalChoice.upper()

        # if the user selects keep you win the money what is in your case
        if finalChoice == "KEEP":
            print(f"You have won {green}${format(valuesRandom[my_case - 1], ',')}{white}! Congratulations!")
            break

        # if the user selects swap then they win the money in the other case
        elif finalChoice == "QUESTION":
            correct = select_question(my_case)
            if correct:
                print(f"\nCongratulations! You have won {green}${format(case_objects[my_case].value, ',')}{white}!")
            else:
                print(f"Sorry, you dont get any money.")

            break

        else:
            print("Choice invalid, try again.")

    except ValueError:
        print("Choice invalid, try again.")

input()