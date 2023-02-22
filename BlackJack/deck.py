import itertools
from random import shuffle
from const import PRINTED, SUITS, RANKS
from player import AbstractPlayer


class Card:
    """Defines the card data"""
    def __init__(self, suit, rank, picture, points):
        self.suit = suit
        self.rank = rank
        self.picture = picture
        self.points = points

    def __str__(self):
        message = f'{self.rank} {self.suit} \n' + self.picture + '\nPoints: ' + str(self.points)
        return message


class Deck:
    """Defines the deck, automatically shuffling it at the creating"""
    def __init__(self):
        self.cards = self.generate_deck()
        shuffle(self.cards)

    @staticmethod
    def generate_deck():
        """Generates deck"""
        cards = []
        for suit, rank in itertools.product(SUITS, RANKS):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            picture = PRINTED.get(rank)
            c = Card(suit, rank, picture, points)
            cards.append(c)
        return cards

    def get_card(self):
        """To take the card from deck. Last card of the deck is removed from the deck"""
        return self.cards.pop()

    def __len__(self):
        """Returns number of cards, remaining in deck"""
        return len(self.cards)

