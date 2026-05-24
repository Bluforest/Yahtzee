import random

def rollDie(die, freeze):
    """Randomizes the value of die as long as the corresponding freeze value is false.

    Args:
        die (list): A list of 5 integer values representing dice faces.
        freeze (list): A list of 5 boolean values representing whether or not the die in the corresponding index should be rerolled. True means it should, False means it shouldn't.
    """

    for i in range(5):
        if not freeze[i]:
            die[i] = random.randint(1, 6)

def formatScore(num, been_recorded = False):
    """Formats the argument to contain leading zeroes if it's a 1 digit number, be two spaces ("  ") if it's "BLANK", and leave it unchanged otherwise.
    
    Args:
        num (string): The number to be formatted.
    Returns:
        num (string): The formatted number with a leading zero if necessary or two spaces if blank.
        been_recorded (boolean): True if the given score category has been recorded, false otherwise."""
    
    if been_recorded or num == "BLANK" or num == "" or num == -1:
        return "  "
    elif int(num) // 10 == 0:
        return f"{int(num):02d}"
    else:
        return str(num)

# TODO Display all participating players' score cards (only the 'recorded score' section)
def displayVictor(*scores):
    """Finds and prints the winning player, or determines if there's a tie between two players.
    Args:
        scores: Can be either a list of players' scores or all of them in a tuple within the argument field.
    """
    max_score = max(scores)
    winning_players = []

    for i, score in enumerate(scores):
        if score == max_score:
            winning_players.append(i)
    
    if len(winning_players) > 1:
        tied_players = [str(player + 1) for player in winning_players]
        print(f"TIE BETWEEN PLAYERS {', '.join(tied_players)}!")
    else:
        print(f"PLAYER {winning_players[0]+1} WINS!")

die_faces = [{
   0: "---------",
   1: "|       |",
   2: "|   O   |",
   3: "|       |",
   4: "---------"
},
{
   0: "---------",
   1: "|     O |",
   2: "|       |",
   3: "| O     |",
   4: "---------"
},
{
   0: "---------",
   1: "|     O |",
   2: "|   O   |",
   3: "| O     |",
   4: "---------"
},
{
   0: "---------",
   1: "| O   O |",
   2: "|       |",
   3: "| O   O |",
   4: "---------"
},
{
   0: "---------",
   1: "| O   O |",
   2: "|   O   |",
   3: "| O   O |",
   4: "---------"
},
{
   0: "---------",
   1: "| O   O |",
   2: "| O   O |",
   3: "| O   O |",
   4: "---------"
}]

def printDie(die):
    """Prints ASCII art of the five dice specified in a horizontal row. Does not return any values.
    This function is not used in the main game, only in the menu to demonstrate hands.

    Args:
        die (list): A list of five integer values, each between 1 and 6 (inclusive).
    """

    for row in range(5):
        for face in die:
            print(die_faces[face-1][row], end="   ")
        print()

def printGameDisplay(player, round, rerolls, die, scorecard, round_score, results=False):
    """Displays the player's roll, their score card, and other pertinent information through the use of multiple print() calls.

    Args:
        player (int): Player number, assuming Player 1 is number 0
        round (int): The round number, can be obtained through turn // n_players
        rerolls (int): The number of rerolls left for the player's turn. Find it. Somehow.
        die (list): A list of 5 integers representing the player's dice rolls.
        scorecard (object): The current player's scorecard object.
        round_score (dictionary): Parse in the result of calcHandScores() on the player's current hand.
        reuslts (boolean): Decides on which set of instructions to give the player in the bottom-left corner of the box.
    """

    print("_"*70)
    print(f"|  PLAYER {player+1}'S TURN  |  ROUND:  {round:02d} / 13  |  ROLLS REMAINING:   {rerolls} / 2  |")
    print("‾"*70)
    print("_"*70)
    print("|" + " "*15 + "|" + f"{'SCORECARD':^52}|")

    if rerolls == 0:
        print(f"|{'FINAL HAND':^15}|" + "‾"*52 + "|")
    else:
        print(f"|{'THIS ROLL':^15}|" + "‾"*52 + "|")
    
    print("|" + " "*15 + f"|{'CATEGORY':^19}|{'RECORDED SCORE':^16}|{'ROUND SCORE':^15}|")
    print(f"|{die_faces[die[0]-1][0]:^15}|" + "‾"*52 + "|")

    print(f"|{die_faces[die[0]-1][1]:^15}|" + f" {'[1]':<5}{'ACES':<13}|" + f"{formatScore(scorecard.aces):^16}" + "|" + f"{formatScore(round_score['aces'], scorecard.aces != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[0]-1][2]:^15}|" + f" {'[2]':<5}{'TWOS':<13}|" + f"{formatScore(scorecard.twos):^16}" + "|" + f"{formatScore(round_score['twos'], scorecard.twos != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[0]-1][3]:^15}|" + f" {'[3]':<5}{'THREES':<13}|" + f"{formatScore(scorecard.threes):^16}" + "|" + f"{formatScore(round_score['threes'], scorecard.threes != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[0]-1][4]:^15}|" + f" {'[4]':<5}{'FOURS':<13}|" + f"{formatScore(scorecard.fours):^16}" + "|" + f"{formatScore(round_score['fours'], scorecard.fours != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[1]-1][0]:^15}|" + f" {'[5]':<5}{'FIVES':<13}|" + f"{formatScore(scorecard.fives):^16}" + "|" + f"{formatScore(round_score['fives'], scorecard.fives != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[1]-1][1]:^15}|" + f" {'[6]':<5}{'SIXES':<13}|" + f"{formatScore(scorecard.sixes):^16}" + "|" + f"{formatScore(round_score['sixes'], scorecard.sixes != "BLANK"):^15}" + "|")

    print(f"|{die_faces[die[1]-1][2]:^15}|" + "-"*52 + "|")

    print(f"|{die_faces[die[1]-1][3]:^15}|      BONUS        ", f"{formatScore(scorecard.bonus):^16}", " "*15, "", sep="|")

    print(f"|{die_faces[die[1]-1][4]:^15}|" + "-"*52 + "|")

    print(f"|{die_faces[die[2]-1][0]:^15}|" + f" {'[7]':<5}{'3 OF A KIND':<13}|" + f"{formatScore(scorecard.three_kind):^16}" + "|" + f"{formatScore(round_score['three kind'], scorecard.three_kind != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[2]-1][1]:^15}|" + f" {'[8]':<5}{'4 OF A KIND':<13}|" + f"{formatScore(scorecard.four_kind):^16}" + "|" + f"{formatScore(round_score['four kind'], scorecard.four_kind != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[2]-1][2]:^15}|" + f" {'[9]':<5}{'FULL HOUSE':<13}|" + f"{formatScore(scorecard.full_house):^16}" + "|" + f"{formatScore(round_score['full house'], scorecard.full_house != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[2]-1][3]:^15}|" + f" {'[10]':<5}{'SM. STRAIGHT':<13}|" + f"{formatScore(scorecard.sm_straight):^16}" + "|" + f"{formatScore(round_score['sm straight'], scorecard.sm_straight != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[2]-1][4]:^15}|" + f" {'[11]':<5}{'LG. STRAIGHT':<13}|" + f"{formatScore(scorecard.lg_straight):^16}" + "|" + f"{formatScore(round_score['lg straight'], scorecard.lg_straight != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[3]-1][0]:^15}|" + f" {'[12]':<5}{'YAHTZEE':<13}|" + f"{formatScore(scorecard.yahtzee):^16}" + "|" + f"{formatScore(round_score['yahtzee'], scorecard.yahtzee != "BLANK"):^15}" + "|")
    print(f"|{die_faces[die[3]-1][1]:^15}|" + f" {'[13]':<5}{'CHANCE':<13}|" + f"{formatScore(scorecard.chance):^16}" + "|" + f"{formatScore(round_score['chance'], scorecard.chance != "BLANK"):^15}" + "|")
    
    print(f"|{die_faces[die[3]-1][2]:^15}|" + "-"*52 + "|")

    print(f"|{die_faces[die[3]-1][3]:^15}|" + "   YAHTZEE BONUS   |" + f"{formatScore(scorecard.yahtzee_bonus):^16}" + "|" + " "*15 + "|")

    print(f"|{die_faces[die[3]-1][4]:^15}|" + "‾"*52 + "|")

    if results:
        print(f"|{die_faces[die[4]-1][0]:^15}|" + " "*52 + "|")
        print(f"|{die_faces[die[4]-1][1]:^15}|" + " "*52 + "|")
        print(f"|{die_faces[die[4]-1][2]:^15}|" + f"{'Press ENTER to continue the game.':^52}" + "|")
        print(f"|{die_faces[die[4]-1][3]:^15}|" + " "*52 + "|")
        print(f"|{die_faces[die[4]-1][4]:^15}|" + " "*52 + "|")
    elif rerolls == 0:
        print(f"|{die_faces[die[4]-1][0]:^15}|   * Choose which score category you wish to        |")
        print(f"|{die_faces[die[4]-1][1]:^15}|     assign this hand to.                           |")
        print(f"|{die_faces[die[4]-1][2]:^15}|   * Category name or number (1-13) both work.      |")
        print(f"|{die_faces[die[4]-1][3]:^15}|   * The \"ROUND SCORE\" column shows how many        |")
        print(f"|{die_faces[die[4]-1][4]:^15}|     points your hand is worth in that category.    |")
    else:
        print(f"|{die_faces[die[4]-1][0]:^15}|   * Enter 1-5, separated by spaces, to choose      |")
        print(f"|{die_faces[die[4]-1][1]:^15}|     which die to keep and reroll the rest.         |")
        print(f"|{die_faces[die[4]-1][2]:^15}|   * Press ENTER to reroll all die.                 |")
        print(f"|{die_faces[die[4]-1][3]:^15}|   * Enter \"KEEP\" to retain all die and forfeit     |")
        print(f"|{die_faces[die[4]-1][4]:^15}|     all remaining rerolls.                         |")


    print("|               |                                                    |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")    

def catStrCleanup(string):
    """TODO make a docstring here"""
    clean_string = string.replace("_", " ")

    number_words = {"three": "3", "four": "4"}

    if "kind" in clean_string:
        return (number_words[clean_string[:clean_string.find(' kind')]]+" of a "+clean_string[clean_string.find('kind'):]).upper()
    if "straight" in clean_string:
        return (clean_string[:clean_string.find(' straight')]+"."+clean_string[clean_string.find(' straight'):]).upper()
    return clean_string.upper()

def printFinalScores(player_scores, final_scores):
    """TODO make a docstring here
    final_scores in the program is final_scores outside too
    """
    print(f"{'FINAL SCORES':^70}")
    print("_"*70)
    print(f"|{'CATEGORY':^16}|{'PLAYER 1':^12}|{'PLAYER 2':^12}|{'PLAYER 3':^12}|{'PLAYER 4':^12}|")
    print("|" + "‾"*68 + "|")

    category_names = ["aces", "twos", "threes", "fours", "fives", "sixes"]

    for category in category_names:
        print(f"|  {category.upper():14}|", end="")
        for i in range(4):
            print(f"{formatScore(getattr(player_scores[i], category)):^12}", end="|")
        print()

    print("|" + "-"*68 + "|")

    print(f"|  {'DIGITS TOTAL':14}|", end="")
    for i in range(4):
        if player_scores[i].aces != "BLANK":
            print(f"{formatScore(player_scores[i].aces + player_scores[i].twos + player_scores[i].threes + player_scores[i].fours + player_scores[i].fives + player_scores[i].sixes):^12}", end="|")
        else:
            print(" "*12, end="|")
    print()

    print(f"|  {'BONUS IF >62':14}|", end="")
    for i in range(4):
        print(f"{formatScore(player_scores[i].bonus):^12}", end="|")
    print()

    print(f"|  {'TOP TOTAL':14}|", end="")
    for i in range(4):
        if player_scores[i].aces != "BLANK":
            print(f"{formatScore(player_scores[i].aces + player_scores[i].twos + player_scores[i].threes + player_scores[i].fours + player_scores[i].fives + player_scores[i].sixes + player_scores[i].bonus):^12}", end="|")
        else:
            print(" "*12, end="|")
    print()

    print("|" + "-"*68 + "|")

    category_names = ["three_kind", "four_kind", "full_house", "sm_straight", "lg_straight", "yahtzee", "chance"]

    for category in category_names:
        print(f"|  {catStrCleanup(category):14}|", end="")
        for i in range(4):
            print(f"{formatScore(getattr(player_scores[i], category)):^12}", end="|")
        print()

    print("|" + "-"*68 + "|")

    print(f"|  {'YAHTZEE BONUS':14}|", end="")
    for i in range(4):
        if player_scores[i].aces != "BLANK":
            print(f"{formatScore(player_scores[i].yahtzee_bonus):^12}", end="|")
        else:
            print(" "*12, end="|")
    print()

    print(f"|  {'BOTTOM TOTAL':14}|", end="")
    for i in range(4):
        if player_scores[i].aces != "BLANK":
            print(f"{formatScore(player_scores[i].three_kind + player_scores[i].four_kind + player_scores[i].full_house + player_scores[i].sm_straight + player_scores[i].lg_straight + player_scores[i].yahtzee + player_scores[i].chance + player_scores[i].yahtzee_bonus):^12}", end="|")
        else:
            print(" "*12, end="|")
    print()

    print("|" + "-"*68 + "|")
    print("", " "*16, " "*12, " "*12, " "*12, " "*12, "", sep="|")

    print(f"|  {'GRAND TOTAL':14}|", end="")
    for i in range(4):
        if player_scores[i].aces != "BLANK":
            print(f"{formatScore(final_scores[i]):^12}", end="|")
        else:
            print(" "*12, end="|")
    print()

    print("", " "*16, " "*12, " "*12, " "*12, " "*12, "", sep="|")
    print("‾"*70)

def handChecker(die):
    """Returns a dictionary of whether or not the die values specified by the argument satisfies the requirements for any of the Yahtzee hands.

    Args:
        die (list): A list of five integer values, each between 1 and 6 (inclusive).
    
    Returns:
        checks (dictionary): A dictionary of boolean values with keys "three kind", "four kind", "yahtzee", "full house", "sm straight", "lg straight".
    """

    counts = [0, 0, 0, 0, 0, 0]

    for value in die:
        counts[value-1] += 1

    # Three-, Four-, and Five-of-a-Kind checker
    three_of_a_kind = False
    four_of_a_kind = False
    five_of_a_kind = False

    for count in counts:
        if count >= 3:
            three_of_a_kind = True
        if count >= 4:
            four_of_a_kind = True
        if count >= 5:
            five_of_a_kind = True

    # Full House checker
    full_house = False
    if 3 in counts and 2 in counts:
        full_house = True

    # Small Straight checker
    small_straight = False
    for i in range(3):
        if counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0 and counts[i+3] > 0:
            small_straight = True

    # Large Straight checker
    large_straight = False
    for i in range(2):
        if counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0 and counts[i+3] > 0 and counts[i+4]:
            large_straight = True

    return {
        "three kind": three_of_a_kind,
        "four kind": four_of_a_kind,
        "full house": full_house,
        "sm straight": small_straight,
        "lg straight": large_straight,
        "yahtzee": five_of_a_kind
    }

def calcHandScores(die):
    """Calculates how many points the given list of 5 dice will be worth under all Yahtzee score categories.
    
    Args:
        die (list): A list of five integer values, each between 1 and 6 (inclusive).
    
    Returns:
        scores (dictionary): A dictionary of the given dice's Yahtzee scores, including single values and special hands. Keys: "aces", "twos", "threes", "fours", "fives", "sixes", "three kind", "four kind", "full house", "sm straight", "lg straight", "yahtzee", "chance".
    """

    # Initializes a dictionary for all the scores. Default values are always 0.
    scores = {
        "aces": 0,
        "twos": 0,
        "threes": 0,
        "fours": 0,
        "fives": 0,
        "sixes": 0,
        "three kind": 0,
        "four kind": 0,
        "full house": 0,
        "sm straight": 0,
        "lg straight": 0,
        "yahtzee": 0,
        "chance": 0
    }

    # This is a dictionary of boolean values for the special hands ("three kind" onwards). Key values are the same as in scores.
    valid = handChecker(die)

    number_to_category = {
        1: "aces",
        2: "twos",
        3: "threes",
        4: "fours",
        5: "fives",
        6: "sixes"
    }

    # Aces - Sixes
    for value in die:
        scores[number_to_category[value]] += value
    
    if valid["three kind"]:
        scores["three kind"] = sum(die)
    
    if valid["four kind"]:
        scores["four kind"] = sum(die)
    
    if valid["full house"]:
        scores["full house"] = 25
    
    if valid["sm straight"]:
        scores["sm straight"] = 30
    
    if valid["lg straight"]:
        scores["lg straight"] = 40
    
    if valid["yahtzee"]:
        scores["yahtzee"] = 50
    
    scores["chance"] = sum(die)
    
    return scores

class ScoreCard:
    def __init__(self):    
        # Top part of the score card
        self.aces = "BLANK"           # Score: Sum of all die displaying a 1 | Requirement: None
        self.twos = "BLANK"           # Score: Sum of all die displaying a 2 | Requirement: None
        self.threes = "BLANK"         # Score: Sum of all die displaying a 3 | Requirement: None
        self.fours = "BLANK"          # Score: Sum of all die displaying a 4 | Requirement: None
        self.fives = "BLANK"          # Score: Sum of all die displaying a 5 | Requirement: None
        self.sixes = "BLANK"          # Score: Sum of all die displaying a 6 | Requirement: None

        self.bonus = "BLANK"          # Score: 35 | Requirement: If the total of the above scores is 63 or higher

        # Bottom part of the score card
        self.three_kind = "BLANK"     # Score: Sum of all die faces | Requirement: Three die displaying the same number
        self.four_kind = "BLANK"      # Score: Sum of all die faces | Requirement: Four die displaying the same number
        self.full_house = "BLANK"     # Score: 25 | Requirement: Three of a kind and two of a kind simultaneously
        self.sm_straight = "BLANK"    # Score: 30 | Requirement: Four die in a sequence
        self.lg_straight = "BLANK"    # Score: 40 | Requirement: Five die in a sequence
        self.yahtzee = "BLANK"        # Score: 50 | Requirement: Five die displaying the same number
        self.chance = "BLANK"         # Score: Sum of all die faces | Requirement: None

        self.yahtzee_bonus = 0        # Score: 100 per Yahtzee achieved during the game | Requirement: None

        self.digits_total = -1         # Total of all scores in categories aces-sixes. Placeholder -1
        self.top_total = -1            # Total of all scores in categories aces-sixes and the bonus if applicable. Placeholder -1
        self.bottom_total = -1         # Total of all scores in all categories after bonus, including yahtzee bonus. Placeholder -1
        self.total = -1                # The total score. This will be calculated at the end of the game. Placeholder -1
    
    def calcTotal(self):
        self.total = self.aces + self.twos + self.threes + self.fours + self.fives + self.sixes + self.bonus + self.three_kind + self.four_kind + self.full_house + self.sm_straight + self.lg_straight + self.yahtzee + self.chance

    def recordBonus(self):
        if not self.aces == "BLANK" and not self.twos == "BLANK" and not self.threes == "BLANK" and not self.fours == "BLANK" and not self.fives == "BLANK" and not self.sixes == "BLANK":
            if self.aces + self.twos + self.threes + self.fours + self.fives + self.sixes >= 63:
                self.bonus = 35
            else:
                self.bonus = 0
    
    def recordYahtzeeBonus(self, die):
        if handChecker(die)["yahtzee"] and self.yahtzee == 50:
            self.yahtzee_bonus += 100
    
    def recordAces(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.aces == "BLANK":
            return -1
        
        self.aces = round_scores["aces"]
        self.recordBonus()

        """
        score_add = 0
        for value in die:
            if value == 1:
                score_add += value
        
        self.aces = score_add
        """
    
    def recordTwos(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.twos == "BLANK":
            return -1
        
        self.twos = round_scores["twos"]
        self.recordBonus()

        """
        score_add = 0
        for value in die:
            if value == 2:
                score_add += value
        
        self.twos = score_add
        """
    
    def recordThrees(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.threes == "BLANK":
            return -1
        
        self.threes = round_scores["threes"]
        self.recordBonus()

        """
        score_add = 0
        for value in die:
            if value == 3:
                score_add += value
        
        self.threes = score_add
        """
    
    def recordFours(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.fours == "BLANK":
            return -1
        
        self.fours = round_scores["fours"]
        self.recordBonus()

        """
        score_add = 0
        for value in die:
            if value == 4:
                score_add += value
        
        self.fours = score_add
        """
    
    def recordFives(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.fives == "BLANK":
            return -1
        
        self.fives = round_scores["fives"]
        self.recordBonus()

        """
        score_add = 0
        for value in die:
            if value == 5:
                score_add += value
        
        self.fives = score_add
        """
    
    def recordSixes(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.sixes == "BLANK":
            return -1
        
        self.sixes = round_scores["sixes"]
        self.recordBonus()

        """
        score_add = 0
        for value in die:
            if value == 6:
                score_add += value
        
        self.sixes = score_add
        """
    
    def recordThreeKind(self, round_scores):
        if not self.three_kind == "BLANK":
            return -1
        
        self.three_kind = round_scores["three kind"]

        """
        if handChecker(die)["three kind"]:
            self.three_kind = sum(die)
        else:
            self.three_kind = 0
        """
    
    def recordFourKind(self, round_scores):
        if not self.four_kind == "BLANK":
            return -1
        
        self.four_kind = round_scores["four kind"]
        
        """
        if handChecker(die)["four kind"]:
            self.four_kind = sum(die)
        else:
            self.four_kind = 0
        """
    
    def recordFullHouse(self, round_scores):
        if not self.full_house == "BLANK":
            return -1
        
        self.full_house = round_scores["full house"]
        
        """
        if handChecker(die)["full house"]:
            self.full_house = 25
        else:
            self.full_house = 0
        """
    
    def recordSmallStraight(self, round_scores):
        if not self.sm_straight == "BLANK":
            return -1
        
        self.sm_straight = round_scores["sm straight"]

        """
        if handChecker(die)["sm straight"]:
            self.sm_straight = 30
        else:
            self.sm_straight = 0
        """
    
    def recordLargeStraight(self, round_scores):
        if not self.lg_straight == "BLANK":
            return -1
        
        self.lg_straight = round_scores["lg straight"]

        """
        if handChecker(die)["lg straight"]:
            self.lg_straight = 40
        else:
            self.lg_straight = 0
        """
    
    def recordChance(self, round_scores):
        if not self.chance == "BLANK":
            return -1
        
        self.chance = round_scores["chance"]

        """
        self.chance = sum(die)
        """
    
    def recordYahtzee(self, round_scores):
        if not self.yahtzee == "BLANK":
            return -1
        
        self.yahtzee = round_scores["yahtzee"]

        """
        if handChecker(die)["yahtzee"]:
            self.yahtzee = 50
        else:
            self.yahtzee = 0
        """
    
    commands_dict = {
        "1": recordAces,
        1: recordAces,
        "ACES": recordAces,
        "2": recordTwos,
        2: recordTwos,
        "TWOS": recordTwos,
        "3": recordThrees,
        3: recordThrees,
        "THREES": recordThrees,
        "4": recordFours,
        4: recordFours,
        "FOURS": recordFours,
        "5": recordFives,
        5: recordFives,
        "FIVES": recordFives,
        "6": recordSixes,
        6: recordSixes,
        "SIXES": recordSixes,
        "7": recordThreeKind,
        7: recordThreeKind,
        "THREE OF A KIND": recordThreeKind,
        "3 OF A KIND": recordThreeKind,
        "8": recordFourKind,
        8: recordFourKind,
        "FOUR OF A KIND": recordFourKind,
        "4 OF A KIND": recordFourKind,
        "9": recordFullHouse,
        9: recordFullHouse,
        "FULL HOUSE": recordFullHouse,
        "10": recordSmallStraight,
        10: recordSmallStraight,
        "SM. STRAIGHT": recordSmallStraight,
        "SMALL STRAIGHT": recordSmallStraight,
        "11": recordLargeStraight,
        11: recordLargeStraight,
        "LG. STRAIGHT": recordLargeStraight,
        "LARGE STRAIGHT": recordLargeStraight,
        "12": recordYahtzee,
        12: recordYahtzee,
        "YAHTZEE": recordYahtzee,
        "13": recordChance,
        13: recordChance,
        "CHANCE": recordChance
    }

# BELOW IS THE MAIN PROGRAM
if __name__ == "__main__":
    player_scores = [ScoreCard(), ScoreCard(), ScoreCard(), ScoreCard()]

    # Getting the number of players
    print("\nWelcome to a legally-distinct Yahtzee Python program!\nPlease enter the number of players (1-4).\n")
    response = input()

    while not response.isdigit() or not 1 <= int(response) <= 4:
        print("That's not a valid number of players. Please enter a number between 1 and 4.\n")
        response = input()

    n_players = int(response)

    # POSSIBLE MENUS:
    # MAIN              - Can choose any starting menu or begin the game.
    # SETTINGS          - Can change settings.
    # CONTROLS          - Basic explanation of the controls.
    # RULES             - Basic explanation of the rules of yahtzee.
    # EXAMPLE SCORES    - Basic explanation of the special dice hands.

    # Game state and settings
    in_menu = True
    menu = "MAIN"

    # Main Menu
    while in_menu:
        # Select which menu you want or start the game
        if menu == "MAIN":
            print("\nMAIN MENU")
            print("Type START to begin the game.")
            print("Type HELP to learn the controls.")
            print("Type RULES to learn how Yahtzee works.")
            print("Type SCORE to see scoring examples.")
            print("Type SETTINGS to view current settings.\n")
            response = input("Enter your choice: ")

            if response.strip().lower() == "settings":
                menu = "SETTINGS"
            elif response.strip().lower() == "help":
                menu = "CONTROLS"
            elif response.strip().lower() == "rules":
                menu = "RULES"
            elif response.strip().lower() == "score":
                menu = "EXAMPLE SCORES"
            elif response.strip().lower() == "start":
                in_menu = False
            else:
                print("Invalid input. Please type START, HELP, RULES, SCORE, or SETTINGS.\n")
        
        # Settings Menu
        if menu == "SETTINGS":
            print("\nSETTINGS")
            print(f"Number of players: {n_players}")
            print("Players choose which dice to keep before rerolling.")
            print("Type BACK to return to the main menu.\n")
            input("Press ENTER to return: ")
            menu = "MAIN"

        # Controls Explanation
        if menu == "CONTROLS":
            print("\nCONTROLS")
            print("After each roll, type the dice numbers you want to KEEP.")
            print("Example: typing 1 3 5 keeps dice #1, #3, and #5.")
            print("Type KEEP if you do not want to reroll any dice.")
            print("After the final roll, choose a score category.")
            input("\nPress ENTER to return: ")
            menu = "MAIN"

        # Rules Explanation
        if menu == "RULES":
            print("\nRULES")
            print("Each player gets 13 turns.")
            print("Each turn allows up to 3 total rolls.")
            print("Each score category can only be used once.")
            print("The player with the highest final score wins.")
            input("\nPress ENTER to return: ")
            menu = "MAIN"

        if menu == "EXAMPLE SCORES":
            print("\nEXAMPLE SCORES")
            print("Full House: three of one number and two of another = 25 points.")
            print("Small Straight: four numbers in a row = 30 points.")
            print("Large Straight: five numbers in a row = 40 points.")
            print("Yahtzee: five matching dice = 50 points.")
            print("Chance: total of all dice.")
            input("\nPress ENTER to return: ")
            menu = "MAIN"


    # Main program. Each player gets 13 turns.
    for turn in range(n_players*13):
        die_values = [0, 0, 0, 0, 0]
        freeze_values = [False, False, False, False, False]
        current_player = turn % n_players

        print("_"*57, end="\n\n")

        rollDie(die_values, freeze_values)
        
        end_rerolls = False
        for i in range(2):
            round_scores = calcHandScores(die_values)
            printGameDisplay(current_player, (turn // n_players) + 1, 2-i, die_values, player_scores[current_player], round_scores)

            valid_input = False
            while not valid_input:
                try:
                    response = input()
                    if response.strip().upper() == "KEEP":
                        valid_input = True
                        end_rerolls = True
                        break
                    
                    freeze_values = [False, False, False, False, False]
                    for die_number in response.split():
                        die_index = int(die_number) - 1
                        if die_index < 0 or die_index > 4:
                            raise ValueError
                        freeze_values[die_index] = True
                    valid_input = True
                except:
                    print("Invalid input. Please enter \"KEEP\" or dice numbers between 1 and 5, separated by spaces.")
            
            if end_rerolls:
                break
            
            rollDie(die_values, freeze_values)
            

        round_scores = calcHandScores(die_values)
        printGameDisplay(current_player, (turn // n_players) + 1, 0, die_values, player_scores[current_player], round_scores)
        
        while True:
            response = input("Choose a score category: ")
            category = response.strip().upper()
            
            if category in player_scores[current_player].commands_dict:
                result = player_scores[current_player].commands_dict[category](player_scores[current_player], round_scores)

                if result == -1:
                    print("You may only record a score for each category once. Please choose another category.\n")
                else:
                    break
            else:
                print("Please enter a valid score category.\n")

        player_scores[current_player].commands_dict[response.upper()](player_scores[current_player], round_scores)

        printGameDisplay(current_player, (turn // n_players) + 1, 0, die_values, player_scores[current_player], round_scores, True)
        input()
    
    final_scores = []
    for player in range(n_players):
        player_scores[player].calcTotal()
        final_scores.append(player_scores[player].total)
    
    printFinalScores(player_scores, final_scores)
    displayVictor(*final_scores)
