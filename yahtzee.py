import random

colors_enabled = True

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

def colorize(text, color):
    if colors_enabled:
        return color + text + RESET
    return text

def rollDie(die, freeze):
    """Randomizes the value of die as long as the corresponding freeze value is false.

    Args:
        die (list): A list of 5 integer values representing dice faces.
        freeze (list): A list of 5 boolean values representing whether or not the die in the corresponding index should be rerolled. True means it should, False means it shouldn't.
    """

    for i in range(5):
        if not freeze[i]:
            die[i] = random.randint(1, 6)

def rollDieEasy(die, freeze, scorecard):
    """Randomizes the value of die as long as the corresponding freeze value is false. Increases the odds that the player will roll beneficial dice.

    Args:
        die (list): A list of 5 integer values representing dice faces.
        freeze (list): A list of 5 boolean values representing whether or not the die in the corresponding index should be rerolled. True means it should, False means it shouldn't.
        scorecard (object): The current player's scorecard object.
    """

    if True not in freeze:
        for i in range(5):
            die[i] = random.randint(1, 6)
        return

    kept_dice_permanent  = [x for x, keep in zip(die, freeze) if keep]
    kept_dice_count = len(kept_dice_permanent)

    copies = 0
    for i in range(kept_dice_count):
        kept_dice = kept_dice_permanent.copy()
        kept_dice.pop(i)
        
        if kept_dice_permanent[i] in kept_dice:
            copies += 1
    
    # Going for a yahtzee
    if copies == kept_dice_count:
        target_num = kept_dice_permanent[0]

        for i in range(5):
            if not freeze[i]:
                if random.randint(1, 4) == 1:
                    die[i] = target_num
                else:
                    die[i] = random.randint(1, 6)
    
    # Going for a straight
    elif copies == 0:
        if scorecard.sm_straight == "BLANK" or scorecard.lg_straight == "BLANK":
            target_num = list(set([1, 2, 3, 4, 5, 6]) - set(kept_dice_permanent))

            for i in range(5):
                if not freeze[i]:
                    if random.randint(1, 3) == 1:
                        die[i] = target_num[random.randint(0, len(target_num)-1)]
                    else:
                        die[i] = random.randint(1, 6)
        else:
            for i in range(5):
                if not freeze[i]:
                    if random.randint(1, 3) == 1:
                        die[i] = random.randint(4, 6)
                    else:
                        die[i] = random.randint(1, 6)

    # Going for a full house
    else:
        if scorecard.full_house == "BLANK":
            target_num = list(dict.fromkeys(kept_dice_permanent))

            for i in range(5):
                if not freeze[i]:
                    if random.randint(1, 4) == 1:
                        die[i] = target_num[random.randint(0, len(target_num)-1)]
                    else:
                        die[i] = random.randint(1, 6)
        else:
            for i in range(5):
                if not freeze[i]:
                    if random.randint(1, 3) == 1:
                        die[i] = random.randint(4, 6)
                    else:
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
        print(colorize(f"TIE BETWEEN PLAYERS {', '.join(tied_players)}!", YELLOW))
    else:
        print(colorize(f"PLAYER {winning_players[0] + 1} WINS!", GREEN))

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

def printGameDisplay(player, round, rerolls, die, scorecard, round_score, results = False):
    """Displays the player's roll, their score card, and other pertinent information through the use of multiple print() calls.

    Args:
        player (int): Player number, assuming Player 1 is number 0
        round (int): The round number, can be obtained through turn // n_players
        rerolls (int): The number of rerolls left for the player's turn. Find it. Somehow.
        die (list): A list of 5 integers representing the player's dice rolls.
        scorecard (object): The current player's scorecard object.
        round_score (dictionary): Parse in the result of calcHandScores() on the player's current hand.
        results (boolean): Decides on which set of instructions to give the player in the bottom-right corner of the box.
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
    """Short for Category String Cleanup. Turns the internal score category names (eg. "sm_straight", "four_kind") into something that can be presented to the public.
    Used when iterating over the dictionary of score categories and printing the reuslt.

    Args:
        string (string): The string to clean up. This should be the internal dictionary key for one of the yahtzee score category names.
    """
    clean_string = string.replace("_", " ")

    number_words = {"three": "3", "four": "4"}

    if "kind" in clean_string:
        return (number_words[clean_string[:clean_string.find(' kind')]]+" of a "+clean_string[clean_string.find('kind'):]).upper()
    if "straight" in clean_string:
        return (clean_string[:clean_string.find(' straight')]+"."+clean_string[clean_string.find(' straight'):]).upper()
    return clean_string.upper()

def printFinalScores(player_scores, final_scores):
    """Creates and prints a tabulated display of each active player's end-of-game scores. Should only be called at the end of the game.

    Args:
        player_scores (list): A list of ScoreCard objects representing each player's scorecard. Should be the same as the global variable of the same name.
        final_scores (list): A list of integers representing each player's final scores. Should be the same as the global variable of the same name.
    """
    print(colorize(f"{'FINAL SCORES':^70}", BLUE))
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
    
    category_to_score = {
        "three kind": sum(die),
        "four kind": sum(die),
        "full house": 25,
        "sm straight": 30,
        "lg straight": 40,
        "yahtzee": 50
    }

    for category in category_to_score:
        scores[category] = category_to_score[category] if valid[category] else 0
    
    scores["chance"] = sum(die)
    
    return scores

class ScoreCard:
    def __init__(self):    
        # Easy Mode
        self.easy_mode = False        # Default False

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

        self.digits_total = -1        # Total of all scores in categories aces-sixes. Placeholder -1
        self.top_total = -1           # Total of all scores in categories aces-sixes and the bonus if applicable. Placeholder -1
        self.bottom_total = -1        # Total of all scores in all categories after bonus, including yahtzee bonus. Placeholder -1
        self.total = -1               # The total score. This will be calculated at the end of the game. Placeholder -1
        
    def calcTotal(self):
        self.total = self.aces + self.twos + self.threes + self.fours + self.fives + self.sixes + self.bonus + self.three_kind + self.four_kind + self.full_house + self.sm_straight + self.lg_straight + self.yahtzee + self.chance + self.yahtzee_bonus

    def recordBonus(self):
        if not self.aces == "BLANK" and not self.twos == "BLANK" and not self.threes == "BLANK" and not self.fours == "BLANK" and not self.fives == "BLANK" and not self.sixes == "BLANK":
            if self.aces + self.twos + self.threes + self.fours + self.fives + self.sixes >= 63:
                self.bonus = 35
            else:
                self.bonus = 0
    
    def recordYahtzeeBonus(self, round_scores):
        if round_scores["yahtzee"] and self.yahtzee == 50:
            self.yahtzee_bonus += 100
    
    def recordAces(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.aces == "BLANK":
            return -1
        
        self.aces = round_scores["aces"]
        self.recordBonus()
    
    def recordTwos(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.twos == "BLANK":
            return -1
        
        self.twos = round_scores["twos"]
        self.recordBonus()
    
    def recordThrees(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.threes == "BLANK":
            return -1
        
        self.threes = round_scores["threes"]
        self.recordBonus()
    
    def recordFours(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.fours == "BLANK":
            return -1
        
        self.fours = round_scores["fours"]
        self.recordBonus()

    
    def recordFives(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.fives == "BLANK":
            return -1
        
        self.fives = round_scores["fives"]
        self.recordBonus()
    
    def recordSixes(self, round_scores):
        # Checks if the aces have been recorded already
        if not self.sixes == "BLANK":
            return -1
        
        self.sixes = round_scores["sixes"]
        self.recordBonus()
    
    def recordThreeKind(self, round_scores):
        if not self.three_kind == "BLANK":
            return -1
        
        self.three_kind = round_scores["three kind"]
    
    def recordFourKind(self, round_scores):
        if not self.four_kind == "BLANK":
            return -1
        
        self.four_kind = round_scores["four kind"]
    
    def recordFullHouse(self, round_scores):
        if not self.full_house == "BLANK":
            return -1
        
        self.full_house = round_scores["full house"]

    def recordSmallStraight(self, round_scores):
        if not self.sm_straight == "BLANK":
            return -1
        
        self.sm_straight = round_scores["sm straight"]
    
    def recordLargeStraight(self, round_scores):
        if not self.lg_straight == "BLANK":
            return -1
        
        self.lg_straight = round_scores["lg straight"]
    
    def recordChance(self, round_scores):
        if not self.chance == "BLANK":
            return -1
        
        self.chance = round_scores["chance"]
    
    def recordYahtzee(self, round_scores):
        if not self.yahtzee == "BLANK":
            return -1
        
        self.yahtzee = round_scores["yahtzee"]
    
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
        "SM STRAIGHT": recordSmallStraight,
        "SMALL STRAIGHT": recordSmallStraight,
        "11": recordLargeStraight,
        11: recordLargeStraight,
        "LG. STRAIGHT": recordLargeStraight,
        "LG STRAIGHT": recordLargeStraight,
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
    highlight_color = CYAN
    highlight_color_name = "CYAN"

    # Getting the number of players
    print(f"\nWelcome to a legally-distinct Yahtzee Python program!\nPlease enter the number of players ({colorize('1-4', highlight_color)}).\n")
    response = input()

    while not response.isdigit() or not 1 <= int(response) <= 4:
        print(colorize("That's not a valid number of players. Please enter a number between 1 and 4.\n", RED))
        response = input()

    n_players = int(response)

    # Game state and settings
    in_menu = True    # False = Game Starts
    menu = "MAIN"     # Default
    keep_dice = True  # As opposed to the player selecting the dice they wish to REROLL

    # Main Menu
    # TODO Start filling out more colors. Currently I'm using WHTIE as a substitute for bold.
    while in_menu:
        # Select which menu you want or start the game
        if menu == "MAIN":
            print("\n"+"_"*50)
            print(f"{colorize('MAIN MENU', WHITE)}\n\nType {colorize('START', highlight_color)} to begin the game.\nType {colorize('SETTINGS', highlight_color)} to view and change current settings.\nType {colorize('RULES', highlight_color)} to learn how Yahtzee works.\nType {colorize('SCORE', highlight_color)} to see scoring examples.\nType {colorize('HELP', highlight_color)} to learn the controls.")
            response = input("\nENTER YOUR CHOICE: ")

            match response.strip().lower():
                case "settings" | "setting":
                    menu = "SETTINGS"
                case "help" | "controls":
                    menu = "CONTROLS"
                case "rules" | "rule":
                    menu = "RULES"
                case "score" | "scores":
                    menu = "EXAMPLE SCORES"
                case "start" | "begin":
                    in_menu = False
                case _:
                    print(colorize("\nNot a valid menu option. Please type \"START\", \"HELP\", \"RULES\", \"SCORE\", or \"SETTINGS\".", RED))
        
        # Settings Menu
        if menu == "SETTINGS":
            print("\n"+"_"*50)
            print(f"{colorize('SETTINGS', WHITE)}\n")
            print(f"[{colorize('1', highlight_color)}] Change number of players. (Current: {n_players})")
            print(f"[{colorize('2', highlight_color)}] Change whether you'd like to select dice to KEEP or REROLL. (Current: {"KEEP" if keep_dice else "REROLL"})")
            print(f"[{colorize('3', highlight_color)}] Toggle colors. (Current: {'ON' if colors_enabled else 'OFF'})")
            print(f"[{colorize('4', highlight_color)}] Change highlight color. (CURRENT: {highlight_color_name})")
            print(f"[{colorize('5', highlight_color)}] Go to easy mode submenu.")
            print(f"[{colorize('6', highlight_color)}] Return to main menu.\n")

            response = input("ENTER YOUR CHOICE: ")

            match response.strip().lower():
                case "1" | "player" | "players":
                    print(f"\nPlease enter the number of players ({colorize('1-4', highlight_color)}).\n")
                    response = input()

                    while not response.isdigit() or not 1 <= int(response) <= 4:
                        print(colorize("That's not a valid number of players. Please enter a number between 1 and 4.\n", RED))
                        response = input()

                    n_players = int(response)
                    continue
                case "2" | "keep" | "reroll":
                    keep_dice = not keep_dice
                    continue
                case "3" | "color" | "colors":
                    colors_enabled = not colors_enabled
                    continue
                case "4" | "highlight":
                    while True:
                        print("\n"+"_"*50)
                        print(f"{colorize('HIGHLIGHT COLOR', WHITE)}\n")
                        print(f"[{colorize('1', highlight_color)}] Select {colorize('CYAN', CYAN)}{' (CURRENT)' if highlight_color_name == 'CYAN' else ''}")
                        print(f"[{colorize('2', highlight_color)}] Select {colorize('BLUE', BLUE)}{' (CURRENT)' if highlight_color_name == 'BLUE' else ''}")
                        print(f"[{colorize('3', highlight_color)}] Select {colorize('MAGENTA', MAGENTA)}{' (CURRENT)' if highlight_color_name == 'MAGENTA' else ''}")
                        print(f"[{colorize('4', highlight_color)}] Select {colorize('YELLOW', YELLOW)}{' (CURRENT)' if highlight_color_name == 'YELLOW' else ''}")
                        print(f"[{colorize('5', highlight_color)}] Select {colorize('GREEN', GREEN)}{' (CURRENT)' if highlight_color_name == 'GREEN' else ''}")
                        print(f"[{colorize('6', highlight_color)}] BACK")
                        response = input("ENTER YOUR CHOICE: ")
                        match response.strip().lower():
                            case "1" | "cyan":
                                highlight_color = CYAN
                                highlight_color_name = "CYAN"
                                break
                            case "2" | "blue":
                                highlight_color = BLUE
                                highlight_color_name = "BLUE"
                                break
                            case "3" | "magenta":
                                highlight_color = MAGENTA
                                highlight_color_name = "MAGENTA"
                                break
                            case "4" | "yellow":
                                highlight_color = YELLOW
                                highlight_color_name = "YELLOW"
                                break
                            case "5" | "green":
                                highlight_color = GREEN
                                highlight_color_name = "GREEN"
                                break
                            case "6" | "back" | "exit" | "return" | "leave":
                                break
                            case _:
                                print(colorize("Please select a valid option from the list.", RED))
                case "5" | "easy" | "easy mode":
                    menu = "EASY_MODE_SELECTION"
                case "6" | "leave" | "return" | "exit" | "back":
                    menu = "MAIN"
                    continue
                case _:
                    print(colorize("\nInvalid option. Please choose a valid option from the list.", RED))
                    continue
        
        # Easy Mode Toggle Submenu
        if menu == "EASY_MODE_SELECTION":
            print("\n" + "_"*50 + "\n" + colorize("EASY MODE", WHITE))
            print(f"\n[{colorize('1', highlight_color)}] PLAYER 1 (CURRENT: {'EASY' if player_scores[0].easy_mode else 'NORMAL'})\n[{colorize('2', highlight_color)}] PLAYER 2 (CURRENT: {'EASY' if player_scores[1].easy_mode else 'NORMAL'})\n[{colorize('3', highlight_color)}] PLAYER 3 (CURRENT: {'EASY' if player_scores[2].easy_mode else 'NORMAL'})\n[{colorize('4', highlight_color)}] PLAYER 4 (CURRENT: {'EASY' if player_scores[3].easy_mode else 'NORMAL'})\n[{colorize('5', highlight_color)}] Return to settings menu.\n\n")

            response = input("ENTER YOUR CHOICE: ")

            match response.strip().lower():
                case "1" | "player 1":
                    player_scores[0].easy_mode = not player_scores[0].easy_mode
                case "2" | "player 2":
                    player_scores[1].easy_mode = not player_scores[1].easy_mode
                case "3" | "player 3":
                    player_scores[2].easy_mode = not player_scores[2].easy_mode
                case "4" | "player 4":
                    player_scores[3].easy_mode = not player_scores[3].easy_mode
                case "5" | "leave" | "return" | "exit" | "back":
                    menu = "SETTINGS"
                case _:
                    print(colorize("\nInvalid option. Please choose a valid option from the list.", RED))
                    continue



        # Controls Explanation
        if menu == "CONTROLS":
            print("\n" + "_"*50 + "\n" + colorize("REROLLS", WHITE))

            if keep_dice:
                print(f"After each roll, type numbers {colorize('1-5', highlight_color)}, separated by spaces, corresponding to the dice you wish to KEEP.")
                print(f"Ex: typing {colorize('\"1 3 5\"', highlight_color)} keeps dice #1, #3, and #5 and rerolls dice #2 and #4.\n")
                print(f"Go to the {colorize('SETTINGS', highlight_color)} menu if you wish to instead select the dice to REROLL.")
            else:
                print(f"After each roll, type numbers {colorize('1-5', highlight_color)}, separated by spaces, corresponding to the dice you wish to REROLL.")
                print(f"Ex: typing {colorize('\"1 3 5\"', highlight_color)} keeps dice #2 and #4 and rerolls dice #1, #3, and #5.\n")
                print(f"Go to the {colorize('SETTINGS', highlight_color)} menu if you wish to instead select the dice to KEEP.")
            
            print("Dice are ordered from top to bottom (eg. the die at the top is #1 and the die at the bottom is #5).\n")

            print(f"Type {colorize('KEEP', highlight_color)} to retain all dice and immediately skip to score selection.")
            
            print("\n" + colorize("RECORDING SCORE", WHITE))
            print("After the final roll, choose a score category.\nFor this, you may either enter the number in [brackets] to the left of the category or type the category name itself.") 

            print("\n" + colorize("NAVIGATING MENUS", WHITE))
            print("All menus are case-insensitive. You do not need to type in all caps.\nUsually, you may type the menu name or its corresponding number.")

            input("\nPress ENTER to return: ")
            menu = "MAIN"

        # TODO Elaborate on this a little bit.
        # Rules Explanation
        if menu == "RULES":
            print("\n" + "_"*50 + "\n" + colorize("RULES", WHITE))
            print("Each player gets 13 turns.")
            print("Each turn allows up to 3 total rolls.")
            print("Each score category can only be used once.")
            print("The player with the highest final score wins.")
            input("\nPress ENTER to return: ")
            menu = "MAIN"

        if menu == "EXAMPLE SCORES":
            print("\n" + "_"*50 + "\n" + colorize('EXAMPLE SCORES', WHITE) + "\n")
            print(f"Please choose from the following:\n[{colorize('1', highlight_color)}] Three of a Kind\n[{colorize('2', highlight_color)}] Four of a Kind\n[{colorize('3', highlight_color)}] Full House\n[{colorize('4', highlight_color)}] Small Straight\n[{colorize('5', highlight_color)}] Large Straight\n[{colorize('6', highlight_color)}] Yahtzee\n[{colorize('7', highlight_color)}] Chance\n[{colorize('8', highlight_color)}] Return to Main Menu\n")
            response = input()
            
            match response.strip().lower():
                case "1" | "three of a kind" | "3 of a kind" | "three kind" | "3 kind":
                    print("_"*50)
                    print(f"{colorize('THREE OF A KIND', WHITE)}\nYour hand qualifies as a Three of a Kind when at least three of your dice display the same number.\nFor valid hands, your Three of a Kind score is equal to the sum of all dice faces.\n\nEXAMPLES:")
                    printDie([4, 6, 3, 4, 4])
                    print("Score: 21 (4 + 6 + 3 + 4 + 4 = 21)\n")
                    printDie([3, 1, 1, 1, 5])
                    print("Score: 11 (3 + 1 + 1 + 1 + 5 = 11)\n")
                    printDie([2, 2, 4, 4, 5])
                    print("Score: 0 (Doesn't qualify)\n")

                    input("Press ENTER to continue.")
                case "2" | "four of a kind" | "4 of a kind" | "four kind" | "4 kind":
                    print("_"*50)
                    print(f"{colorize('FOUR OF A KIND', WHITE)}\nYour hand qualifies when at least four dice display the same number.")
                    print("For valid hands, your Four of a Kind score is equal to the sum of all dice faces.\n\nEXAMPLES:")
                    printDie([6, 6, 6, 6, 2])
                    print("Score: 26 (6 + 6 + 6 + 6 + 2 = 26)\n")
                    printDie([3, 3, 3, 3, 5])
                    print("Score: 17 (3 + 3 + 3 + 3 + 5 = 17)\n")
                    printDie([2, 2, 2, 4, 5])
                    print("Score: 0 (Doesn't qualify)\n")
                    input("Press ENTER to continue.")
                    
                case "3" | "full house":
                    print("_"*50)
                    print(f"{colorize('FULL HOUSE', WHITE)}\nYour hand qualifies when you have three of one number and two of another number.")
                    print("A Full House is worth 25 points.\n\nEXAMPLES:")
                    printDie([2, 2, 3, 3, 3])
                    print("Score: 25\n")
                    printDie([5, 1, 5, 1, 1])
                    print("Score: 25\n")
                    printDie([4, 4, 4, 4, 4])
                    print("Score: 0 (Doesn't qualify)\n")
                    input("Press ENTER to continue.")
                    
                case "4" | "small straight" | "sm straight" | "sm. straight":
                    print("_"*50)
                    print(f"{colorize('SMALL STRAIGHT', WHITE)}\nYour hand qualifies when you have four dice in a row.")
                    print("A Small Straight is worth 30 points.\n\nEXAMPLES:")
                    printDie([1, 2, 3, 4, 6])
                    print("Score: 30\n")
                    printDie([5, 5, 4, 2, 3])
                    print("Score: 30\n")
                    printDie([1, 2, 4, 5, 6])
                    print("Score: 0 (Doesn't qualify)\n")
                    input("Press ENTER to continue.")
                    
                case "5" | "large straight" | "lg straight" | "lg. straight":
                    print("_"*50)
                    print("LARGE STRAIGHT\nYour hand qualifies when all five dice are in a row.")
                    print("A Large Straight is worth 40 points.\n\nEXAMPLES:")
                    printDie([1, 2, 3, 4, 5])
                    print("Score: 40\n")
                    printDie([6, 4, 3, 5, 2])
                    print("Score: 40\n")
                    printDie([1, 2, 3, 4, 6])
                    print("Score: 0 (Only a small straight)\n")
                    input("Press ENTER to continue.")
                    
                case "6" | "yahtzee" | "five of a kind" | "five kind" | "5 of a kind" | "5 kind":
                    print("_"*50)
                    print(f"{colorize('YAHTZEE', WHITE)}\nYour hand qualifies when all five dice display the same number.")
                    print("A Yahtzee is worth 50 points.\n\nEXAMPLES:")
                    printDie([6, 6, 6, 6, 6])
                    print("Score: 50\n")
                    printDie([1, 1, 1, 1, 1])
                    print("Score: 50\n")
                    printDie([4, 1, 6, 6, 2])
                    print("Score: 0 (Doesn't qualify)\n")
                    input("Press ENTER to continue.")
                    
                case "7" | "chance" | "sum" | "total":
                    print("_"*50)
                    print(f"{colorize('CHANCE', WHITE)}\nChance has no special requirement.")
                    print("Your score is simply the sum of all dice faces.\n\nEXAMPLES:")
                    printDie([1, 3, 4, 5, 6])
                    print("Score: 19 (1 + 3 + 4 + 5 + 6 = 19)\n")
                    printDie([6, 4, 5, 5, 6])
                    print("Score: 26 (6 + 4 + 5 + 5 + 6 = 26)\n")
                    input("Press ENTER to continue.")
                    
                case "exit" | "8" | "leave" | "return":
                    menu = "MAIN"
                case _:
                    print(colorize("\nInvalid input. Please choose one of the listed options.\n", RED))

    # Main game. Each player gets 13 turns.
    for turn in range(n_players*13):
        die_values = [0, 0, 0, 0, 0]
        freeze_values = [False, False, False, False, False]
        current_player = turn % n_players

        print("_"*57, end="\n\n")

        if player_scores[current_player].easy_mode:
            rollDieEasy(die_values, freeze_values, player_scores[current_player])
        else:
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
                    
                    if keep_dice:
                        freeze_values = [False, False, False, False, False]
                        for die_number in response.strip().split():
                            die_index = int(die_number) - 1
                            if die_index < 0 or die_index > 4:
                                raise ValueError
                            freeze_values[die_index] = True
                    else:
                        freeze_values = [True, True, True, True, True]
                        for die_number in response.strip().split():
                            die_index = int(die_number) - 1
                            if die_index < 0 or die_index > 4:
                                raise ValueError
                            freeze_values[die_index] = False
                    
                    valid_input = True
                except:
                    print(colorize("Invalid input. Please enter \"KEEP\" or dice numbers between 1 and 5, separated by spaces.", RED))
            
            if end_rerolls:
                break
            
            if player_scores[current_player].easy_mode:
                rollDieEasy(die_values, freeze_values, player_scores[current_player])
            else:
                rollDie(die_values, freeze_values)
            

        round_scores = calcHandScores(die_values)
        player_scores[current_player].recordYahtzeeBonus(round_scores)
        printGameDisplay(current_player, (turn // n_players) + 1, 0, die_values, player_scores[current_player], round_scores)
        
        while True:
            response = input("Choose a score category: ")
            category = response.strip().upper()
            
            if category in player_scores[current_player].commands_dict:
                result = player_scores[current_player].commands_dict[category](player_scores[current_player], round_scores)

                if result == -1:
                    print(colorize("You may only record a score for each category once. Please choose another category.\n", RED))
                else:
                    break
            else:
                print(colorize("Please enter a valid score category.\n", RED))

        printGameDisplay(current_player, (turn // n_players) + 1, 0, die_values, player_scores[current_player], round_scores, True)
        input()
    
    # Main game finished. Display tabulation of final scores and state the winner.
    final_scores = []
    for player in range(n_players):
        player_scores[player].calcTotal()
        final_scores.append(player_scores[player].total)
    
    printFinalScores(player_scores, final_scores)
    displayVictor(*final_scores)
