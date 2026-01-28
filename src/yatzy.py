from src.pips import Pips, Hands
class Yatzy:


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def chance(*dice):
        chance_score = sum(dice)
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

    '''
    Extracted common logic from ones, twos, threes
    '''
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
        return Yatzy.calculate_points(Pips.ONE.value, *dice)


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def twos(*dice):
        return Yatzy.calculate_points(Pips.TWO.value, *dice)


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def threes(*dice):
        return Yatzy.calculate_points(Pips.THREE.value, *dice)


    '''
    Rename a variable with a clearer name
    The rutine was too long
    The method had too many parameters
    '''
    def __init__(self, *dice):
        self.dice = list(dice)


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    def fours(self):
        return self.calculate_points(Pips.FOUR.value, *self.dice)


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    def fives(self):
        return self.calculate_points(Pips.FIVE.value, *self.dice)  


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    def sixes(self):
        return self.calculate_points(Pips.SIX.value, *self.dice)

    '''
    Extracted common logic from score_pair and two_pair
    '''
    @classmethod
    def compare_pairs(cls, pairs_needed, *dice):
        score = 0
        pair_count = 0
        for die in Pips.reversedValues():
            if dice.count(die) >= Hands.PAIR.value:
                score += die * 2
                pair_count += 1
                if pair_count >= pairs_needed:
                    return score
        return 0

    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @classmethod
    def score_pair(cls, *dice):
        return cls.compare_pairs(1, *dice)

    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @classmethod
    def two_pair(cls, *dice):
        return cls.compare_pairs(2, *dice)

    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def four_of_a_kind(*dice):
        for die in Pips.reversedValues():
            if dice.count(die) >= Hands.FOUR_OF_A_KIND.value:
                return die * 4
        return 0

    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def three_of_a_kind(*dice):
        for die in Pips.reversedValues():
            if dice.count(die) >= Hands.THREE_OF_A_KIND.value:
                return die * 3
        return 0

    '''
    Extracted common logic from small_straight and large_straight
    '''
    @staticmethod
    def calculate_straights(*dice):
        sorted_dice = sorted(dice)
        if sorted_dice == [1, 2, 3, 4, 5]:
            return 15
        if sorted_dice == [2, 3, 4, 5, 6]:
            return 20
        return 0


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def small_straight(*dice):
        return Yatzy.calculate_straights(*dice)


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def large_straight(*dice):
        return Yatzy.calculate_straights(*dice)


    '''
    Rename a variable with a clearer name
    The rutine was too long
    '''
    @staticmethod
    def fullHouse(*dice):
        THREE_OF_A_KIND = Hands.THREE_OF_A_KIND.value
        PAIR = Hands.PAIR.value
        unique_dice = set(dice)
        if len(unique_dice) == 2:
            first_die = unique_dice.pop()
            second_die = unique_dice.pop()
            if (dice.count(first_die) == THREE_OF_A_KIND and dice.count(second_die) == PAIR):
                return sum(dice)
        return 0