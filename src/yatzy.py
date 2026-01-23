from src.pips import Pips
class Yatzy:


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def chance(die_one, die_two, die_three, die_four, die_five):
        chance_score = die_one + die_two + die_three + die_four + die_five
        return chance_score

    
    '''
    The rutine was too long
    '''
    @staticmethod
    def yatzy(dice):
        if not dice:
            return 0
        if len(set(dice)) == 1:
            return 50
        return 0


    @staticmethod
    def calculate_points(pips, *dice):
        chance_score = 0
        for i, j in enumerate(dice):
            if dice[i] == pips:
                i += 1
                chance_score += pips
        return chance_score


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def ones(*dice):
        return Yatzy.calculate_points(Pips.ONE, *dice)


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def twos(*dice):
        return Yatzy.calculate_points(Pips.TWO, *dice)


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def threes(*dice):
        return Yatzy.calculate_points(Pips.THREE, *dice)

    def __init__(self, d1=0, d2=0, d3=0, d4=0, _5=0):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4):
                sum += 4
        return sum

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)):
            if (self.dice[i] == 5):
                s = s + 5
        return s

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)):
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum

    def score_pair(self, d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        at = 0
        for at in range(6):
            if (counts[6 - at - 1] == 2):
                return (6 - at) * 2
        return 0

    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def small_straight(dice_one, dice_two, dice_three, dice_four, dice_five):
        sorted_dice_conbination = sorted([dice_one, dice_two, dice_three, dice_four, dice_five])
        if sorted_dice_conbination == [1, 2, 3, 4, 5]:
            return 15
        return 0


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def large_straight(dice_one, dice_two, dice_three, dice_four, dice_five):
        sorted_dice_conbination = sorted([dice_one, dice_two, dice_three, dice_four, dice_five])
        if sorted_dice_conbination == [2, 3, 4, 5, 6]:
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
