import random
from abc import ABC, abstractmethod

import const


class AbstractPlayer(ABC):
    """Abstract method for creation of new players"""
    def __init__(self):
        self.cards = []
        self.bet = 0
        self.full_points = 0
        self.money = 100
        self.name = None

    def change_points(self):
        """Calculation of all points of the cards at hand"""
        self.full_points = sum([card.points for card in self.cards])

    def take_card(self, card):
        self.cards.append(card)
        self.change_points()

    @abstractmethod
    def change_bet(self, max_bet, min_bet):
        pass

    def print_cards(self):
        """Prints player's cards at hand"""
        print(f"{self.name} data:")
        for card in self.cards:
            print(card, '\n')
        print(f"{self.name} has {self.full_points} points.\n")

    @abstractmethod
    def ask_card(self):
        pass


class Player(AbstractPlayer):
    """Defines the Player"""
    def __init__(self):
        super().__init__()
        self.name = input("Write your name:\n").title()

    def change_bet(self, max_bet, min_bet):
        """Change of bet by the player"""
        while True:
            value = int(input("Make your bet: \n"))
            if min_bet < value <= max_bet:
                self.bet = value
                self.money -= self.bet
                break
        print(f"Your bet is {self.bet} \n")

    def ask_card(self):
        self.print_cards()
        choice = input(const.MESSAGES.get('ask_card')).lower()
        if choice == 'y':
            return True


class Bot(AbstractPlayer):
    """Defines the behaviour of the bots"""
    def __init__(self):
        super().__init__()
        self.max_points = random.randint(17, 20)
        self.name = const.NAMES.pop(random.randint(0, 3))

    def change_bet(self, max_bet, min_bet):
        """Change of bet by the bot"""
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print(self.name, 'gives:', self.bet)

    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False


class Dealer(AbstractPlayer):
    def __init__(self):
        super().__init__()
        self.name = 'Dealer'
        self.max_points = 17

    def change_bet(self, max_bet, min_bet):
        """
        NOTE: This type is dealer. It will not make bets.
        """
        raise Exception('This is a dealer.')

    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False
