import random
from time import sleep
import player
from const import MESSAGES
from deck import Deck


class Game:
    max_player_count = 4

    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        self.dealer = player.Dealer()
        self.dealer_cards = []
        self.all_players_count = 1
        self.deck = None  # Creates the deck at the moment of initiation of the game
        self.max_bet, self.min_bet = 100, 0

    @staticmethod
    def _ask_start(message):
        """Choice to start game or not"""
        while True:
            choice = input(message).lower()
            if choice == 'n':
                print("You choose not to play.")
                break
            elif choice == 'y':
                return True
            else:
                print("Make your choice!")
                continue

    def ask_bet(self):
        """Asks for bet"""
        for pl in self.players:
            pl.change_bet(self.max_bet, self.min_bet)

    def first_deal(self):
        self.deck = Deck()  # Creates the deck at the moment of initiation of the game
        """Distributes the first two cards"""
        for pl in self.players:
            pl.cards = []
            pl.full_points = 0
            for _ in range(2):
                card = self.deck.get_card()
                pl.take_card(card)
                if pl.full_points == 21:
                    pl.money += pl.bet * 1.5
                    print(f'Player {pl.name} has blackjack! Player quits the game.')
                    self.players.remove(pl)
        self.dealer.cards = []
        self.dealer.full_points = 0
        card = self.deck.get_card()
        self.dealer.take_card(card)
        self.dealer.print_cards()
        sleep(5)

    @staticmethod
    def check_stop(pl):
        if pl.full_points >= 21:
            return True
        else:
            return False

    def remove_player(self, pl):
        pl.print_cards()
        if isinstance(pl, player.Player):
            print('You lost!\n')
        elif isinstance(pl, player.Bot):
            print(MESSAGES.get('bot_off').format(pl.name), '\n')
        self.players.remove(pl)
        sleep(3)

    def ask_cards(self):
        for pl in self.players:
            while pl.ask_card():
                card = self.deck.get_card()
                pl.take_card(card)

                is_stop = self.check_stop(pl)
                if is_stop:
                    if pl.full_points > 21:
                        self.remove_player(pl)
                    break

                if isinstance(pl, player.Player):
                    pl.print_cards()

    def _launching(self):
        """Starts if the player decided to start the game"""
        while True:
            try:
                bots_count = int(input("How many bots do you want to add?\n"))
                if bots_count <= self.max_player_count - 1:
                    break
            except ValueError:
                continue
        self.all_players_count = bots_count + 1

        for _ in range(bots_count):
            b = player.Bot()
            self.players.append(b)
            print(b.name, "is created")

        self.player = player.Player()
        self.player_pos = random.randint(1, bots_count + 1)
        print("Your position is:", self.player_pos)
        self.players.insert(self.player_pos, self.player)
        print(self.player.name, "is created")

    def new_game(self):
        for pl in self.players:
            pl.full_points = 0
            self.dealer.full_points = 0

    def check_winner(self):
        if self.dealer.full_points > 21:
            # when dealer falls everybody wins
            print(f"Dealer falls! All remaining players win!\n")
            for pl in self.players:
                pl.money += pl.bet * 2
                sleep(3)
        else:
            # compare dealer with each player
            for pl in self.players:
                if pl.full_points == self.dealer.full_points:
                    pl.money += pl.bet
                    print(f'Push! {pl.name} and dealer have the same amount of points, {pl.full_points}.'
                          f'\n{pl.name} has his money back.\n')
                    sleep(3)
                elif 21 >= pl.full_points > self.dealer.full_points:
                    pl.money += pl.bet * 2
                    if isinstance(pl, player.Bot):
                        print(f'{pl.name} wins with {pl.full_points} points! {pl.name} receives his bid doubled!\n')
                        sleep(3)
                    else:
                        print("You win! You receive your bid doubled!\n")
                        sleep(3)
                else:
                    if isinstance(pl, player.Bot):
                        print(f'Dealer wins over {pl.name} with {self.dealer.full_points} points '
                              f'to {pl.full_points} points.\n')
                        sleep(3)
                    else:
                        print(f"You lost with {pl.full_points} points to {self.dealer.full_points} points of Dealer!\n")
                        sleep(3)

    def play_with_dealer(self):
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
        self.dealer.print_cards()

    def check_summary(self):
        print("\nGAME SUMMARY\n")
        sleep(3)

        for pl in self.players:
            pl.print_cards()
            print(f'{pl.name} now has {pl.money} guldens.\n')
            print('=' * 9)
            sleep(5)

    def start_game(self):
        """Initiation of the game"""
        message = MESSAGES.get('ask_start')
        self._ask_start(message)

        # generating data for start of the game
        self._launching()
        while True:

        # inquiry about the bets
            self.ask_bet()

            # giving first two cards to the players
            self.first_deal()

            # print player cards after first deal
            self.player.print_cards()

            # ask players whether they want to take more cards
            self.ask_cards()

            # dealer takes cards
            self.play_with_dealer()

            # check of the results
            self.check_winner()

            # print summary
            self.check_summary()

            # to choose whether to play again
            if self._ask_start(MESSAGES.get('rerun')):
                continue
            else:
                break
