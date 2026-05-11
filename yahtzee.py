import random

def rollDie(die, freeze):
    """Randomizes the value of die as long as the corresponding freeze is False.
    die is a list of 5 integer values, freeze is a list of 5 boolean values."""

    for i in range(5):
        if not freeze[i]:
            die[i] = random.randint(1, 6)

def displayVictor(*scores):
    max_score = max(scores)
    winning_players = []

    for i, score in enumerate(scores):
        if score == max_score:
            winning_players.append(i)
    
    if len(winning_players) > 1:
        print(f"TIE BETWEEN PLAYERS {winning_players[0]+1} AND", end="")
        for player in winning_players.pop(0):
            print(f"AND {player+1}")
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
    """Prints ASCII art of the five dice specified in a horizontal row.
    NOTE This function is no longer being used in the yahtzee.py program.

    Args:
        die (list): A list of five integer values, each between 1 and 6 (inclusive).
    """

    for row in range(5):
        for face in die:
            print(die_faces[face-1][row], end="   ")
        print()

def printGameDisplay(player, round, rerolls, die, scorecard, round_score):
    """Displays the player's roll, their score card, and other pertinent information through the use of multiple print() calls.

    Args:
        player (int): Player number, assuming Player 1 is number 0
        round (int): The round number, can be obtained through turn // n_players
        rerolls (int): The number of rerolls left for the player's turn. Find it. Somehow.
        die (list): A list of 5 integers representing the player's dice rolls.
        scorecard(object): The current player's scorecard object.
        round_score(dictionary): Parse in the result of calcHandScores() on the player's current hand.
    """

    print("_"*70)
    print(f"|  PLAYER {player+1}'S TURN  |  ROUND:  {round:02d} / 13  |  ROLLS REMAINING:   {rerolls} / 2  |")
    print("‾"*70)
    print("_"*70)
    print("|" + " "*15 + "|" + f"{'SCORECARD':^52}|")
    print(f"|{'THIS ROLL':^15}|" + "‾"*52 + "|")
    print("|" + " "*15 + f"|{'CATEGORY':^19}|{'RECORDED SCORE':^16}|{'ROUND SCORE':^15}|")
    print(f"|{die_faces[die[0]-1][0]:^15}|" + "‾"*52 + "|")

    if scorecard.aces == "BLANK":
        print(f"|{die_faces[die[0]-1][1]:^15}|" + f" {'[1]':<5}{'ACES':<13}|" + " "*16 + "|" + f"{round_score['aces']:^15}" + "|")
    else:
        print(f"|{die_faces[die[0]-1][1]:^15}|" + f" {'[1]':<5}{'ACES':<13}|" + f"{scorecard.aces:^16}" + "|" + " "*15 + "|")
    
    if scorecard.twos == "BLANK":
        print(f"|{die_faces[die[0]-1][2]:^15}|" + f" {'[2]':<5}{'TWOS':<13}|" + " "*16 + "|" + f"{round_score['twos']:^15}" + "|")
    else:
        print(f"|{die_faces[die[0]-1][2]:^15}|" + f" {'[2]':<5}{'TWOS':<13}|" + f"{scorecard.twos:^16}" + "|" + " "*15 + "|")
    
    if scorecard.threes == "BLANK":
        print(f"|{die_faces[die[0]-1][3]:^15}|" + f" {'[3]':<5}{'THREES':<13}|" + " "*16 + "|" + f"{round_score['threes']:^15}" + "|")
    else:
        print(f"|{die_faces[die[0]-1][3]:^15}|" + f" {'[3]':<5}{'THREES':<13}|" + f"{scorecard.threes:^16}" + "|" + " "*15 + "|")

    if scorecard.fours == "BLANK":
        print(f"|{die_faces[die[0]-1][4]:^15}|" + f" {'[4]':<5}{'FOURS':<13}|" + " "*16 + "|" + f"{round_score['fours']:^15}" + "|")
    else:
        print(f"|{die_faces[die[0]-1][4]:^15}|" + f" {'[4]':<5}{'FOURS':<13}|" + f"{scorecard.fours:^16}" + "|" + " "*15 + "|")
    
    if scorecard.fives == "BLANK":
        print(f"|{die_faces[die[1]-1][0]:^15}|" + f" {'[5]':<5}{'FIVES':<13}|" + " "*16 + "|" + f"{round_score['fives']:^15}" + "|")
    else:
        print(f"|{die_faces[die[1]-1][0]:^15}|" + f" {'[5]':<5}{'FIVES':<13}|" + f"{scorecard.fives:^16}" + "|" + " "*15 + "|")

    if scorecard.sixes == "BLANK":
        print(f"|{die_faces[die[1]-1][1]:^15}|" + f" {'[6]':<5}{'SIXES':<13}|" + " "*16 + "|" + f"{round_score['sixes']:^15}" + "|")
    else:
        print(f"|{die_faces[die[1]-1][1]:^15}|" + f" {'[6]':<5}{'SIXES':<13}|" + f"{scorecard.sixes:^16}" + "|" + " "*15 + "|")

    print(f"|{die_faces[die[1]-1][2]:^15}|" + "-"*52 + "|")

    if scorecard.bonus == "BLANK":
        print(f"|{die_faces[die[1]-1][3]:^15}|      BONUS        ", " "*16, " "*15, "", sep="|")
    else:
        print(f"|{die_faces[die[1]-1][3]:^15}|      BONUS        ", f"{scorecard.bonus:^16}", " "*15, "", sep="|")

    print(f"|{die_faces[die[1]-1][4]:^15}|" + "-"*52 + "|")

    if scorecard.three_kind == "BLANK":
        print(f"|{die_faces[die[2]-1][0]:^15}|" + f" {'[7]':<5}{'3 OF A KIND':<13}|" + " "*16 + "|" + f"{round_score['three kind']:^15}" + "|")
    else:
        print(f"|{die_faces[die[2]-1][0]:^15}|" + f" {'[7]':<5}{'3 OF A KIND':<13}|" + f"{scorecard.three_kind:^16}" + "|" + " "*15 + "|")
    
    if scorecard.four_kind == "BLANK":
        print(f"|{die_faces[die[2]-1][1]:^15}|" + f" {'[8]':<5}{'4 OF A KIND':<13}|" + " "*16 + "|" + f"{round_score['four kind']:^15}" + "|")
    else:
        print(f"|{die_faces[die[2]-1][1]:^15}|" + f" {'[8]':<5}{'4 OF A KIND':<13}|" + f"{scorecard.four_kind:^16}" + "|" + " "*15 + "|")

    if scorecard.full_house == "BLANK":
        print(f"|{die_faces[die[2]-1][2]:^15}|" + f" {'[9]':<5}{'FULL HOUSE':<13}|" + " "*16 + "|" + f"{round_score['full house']:^15}" + "|")
    else:
        print(f"|{die_faces[die[2]-1][2]:^15}|" + f" {'[9]':<5}{'FULL HOUSE':<13}|" + f"{scorecard.full_house:^16}" + "|" + " "*15 + "|")
    
    if scorecard.sm_straight == "BLANK":
        print(f"|{die_faces[die[2]-1][3]:^15}|" + f" {'[10]':<5}{'SM. STRAIGHT':<13}|" + " "*16 + "|" + f"{round_score['sm straight']:^15}" + "|")
    else:
        print(f"|{die_faces[die[2]-1][3]:^15}|" + f" {'[10]':<5}{'SM. STRAIGHT':<13}|" + f"{scorecard.sm_straight:^16}" + "|" + " "*15 + "|")
    
    if scorecard.lg_straight == "BLANK":
        print(f"|{die_faces[die[2]-1][4]:^15}|" + f" {'[11]':<5}{'LG. STRAIGHT':<13}|" + " "*16 + "|" + f"{round_score['lg straight']:^15}" + "|")
    else:
        print(f"|{die_faces[die[2]-1][4]:^15}|" + f" {'[11]':<5}{'LG. STRAIGHT':<13}|" + f"{scorecard.lg_straight:^16}" + "|" + " "*15 + "|")

    if scorecard.yahtzee == "BLANK":
        print(f"|{die_faces[die[3]-1][0]:^15}|" + f" {'[12]':<5}{'YAHTZEE':<13}|" + " "*16 + "|" + f"{round_score['yahtzee']:^15}" + "|")
    else:
        print(f"|{die_faces[die[3]-1][0]:^15}|" + f" {'[12]':<5}{'YAHTZEE':<13}|" + f"{scorecard.yahtzee:^16}" + "|" + " "*15 + "|")
    
    if scorecard.chance == "BLANK":
        print(f"|{die_faces[die[3]-1][1]:^15}|" + f" {'[13]':<5}{'CHANCE':<13}|" + " "*16 + "|" + f"{round_score['chance']:^15}" + "|")
    else:
        print(f"|{die_faces[die[3]-1][1]:^15}|" + f" {'[13]':<5}{'CHANCE':<13}|" + f"{scorecard.chance:^16}" + "|" + " "*15 + "|")
    
    print(f"|{die_faces[die[3]-1][2]:^15}|" + "-"*52 + "|")

    print(f"|{die_faces[die[3]-1][3]:^15}|" + "   YAHTZEE BONUS   |" + f"{scorecard.yahtzee_bonus:^16}" + "|" + " "*15 + "|")

    print(f"|{die_faces[die[3]-1][4]:^15}|" + "‾"*52 + "|")

    if rerolls == 0:
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

def handChecker(die):
    """Returns a dictionary of whether or not the die values specified by the argument satisfies the requirements for any of the Yahtzee hands.

    Args:
        die (list): A list of five integer values, each between 1 and 6 (inclusive).
    
    Returns:
        dictionary: A dictionary of boolean values with keys "three kind", "four kind", "yahtzee", "full house", "sm straight", "lg straight".
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

        self.total = -1                # The total score. This will be calculated at the end of the game. Placeholder 0
    
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

# BELOW IS THE MAIN PROGRAM. IT'S UNFINISHED. IT'S ACTUALLY KIND OF BAD. MAYBE REWRITE IT
if __name__ == "__main__":
    player_scores = [ScoreCard(), ScoreCard(), ScoreCard(), ScoreCard()]

    # TODO
    # Make a while loop so that any player can ask for their own scorecard and have it displayed.
    # Keywords to always listen for:
    #   HELP   - Explain the controls
    #   RULES  - Explain the rules of the game
    #   SCORE  - Explain all the score categories
    #   EXIT   - Ends the program immediately (I don't even know if that's possible)
    # Possible other keywords:
    #   SCORECARD [NUMBER] - Show the score card for player [number]

    # Getting the number of players
    print("\nWelcome to a legally-distinct Yahtzee Python program!\nPlease enter the number of players (1-4).\n")
    response = input()

    while not response.isdigit() or not 1 <= int(response) <= 4:
        print("That's not a valid number of players. Please enter a number between 1 and 4.\n")
        response = input()

    n_players = int(response)
    print(f"\nOkay, so we're playing with {n_players} player(s), then? Great!")
    input("Player 1, please get ready. Press ENTER to begin the game!\n")

    # Main program. Each player gets 13 turns.
    for turn in range(n_players*13):
        die_values = [0, 0, 0, 0, 0]
        freeze_values = [False, False, False, False, False]
        current_player = turn % n_players

        print("_"*57, end="\n\n")

        rollDie(die_values, freeze_values)

        for i in range(2):
            round_scores = calcHandScores(die_values)
            printGameDisplay(current_player, (turn // n_players) + 1, 2-i, die_values, player_scores[current_player], round_scores)
            freeze_values = [False, False, False, False, False]

            response = input()
            if response.upper() == "KEEP":
                break
            
            for i in response.split():
                freeze_values[int(i)-1] = True
            rollDie(die_values, freeze_values)
            
            
        
        round_scores = calcHandScores(die_values)
        printGameDisplay(current_player, (turn // n_players) + 1, 0, die_values, player_scores[current_player], round_scores)
        
        while True:
            response = input()
            if response.upper() in player_scores[current_player].commands_dict:
                if player_scores[current_player].commands_dict[response.upper()](player_scores[current_player], round_scores) == -1:
                    print("You may only record a score for each category once. Your may not change previous score assignments.\n")
                else:
                    break
            else:
                print("Please enter a valid score category.\n")
        
        player_scores[current_player].commands_dict[response](player_scores[current_player], round_scores)

        printGameDisplay(current_player, (turn // n_players) + 1, 0, die_values, player_scores[current_player], round_scores)
        
        # TODO make a new scorecard that displays the below instructions but, you know, up above.
        input(f"IGNORE THE INSTRUCTIONS ABOVE. IT'S THE END OF YOUR TURN!\nPress ENTER to continue to PLAYER {(turn+1) % n_players + 1}'S turn:\n")

    for player in range(n_players):
        player_scores[player].calcTotal()
        total_score = player_scores[player].total
        print(f"PLAYER {player+1}'S TOTAL SCORE: {total_score}")

    displayVictor(player_scores[0].total, player_scores[1].total, player_scores[2].total, player_scores[3].total)