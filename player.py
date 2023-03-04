import random

class Player:
    def __init__(self, name):
        self.name = name
        self.card_hand = list()
        self.card_value = 0
        self.busted = False
        self.beat_dealer = False

    def add_card_value(self, card):
        if type(card) == int:
            self.card_value += card
        elif type(card) == str and card != 'Ace':
            self.card_value += 10
        elif card == 'Ace':
            if self.card_value + 11 <= 21:
                self.card_value += 11
            else:
                self.card_value += 1

class Deck:
    def __init__(self):
        self.cards = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
        self.deck = dict()

    def get_deck_count(self):
        """
        Ask user for input on number of decks to use, then build the deck
        :return:
        """
        deck_size = input("How many card decks should be in the deck? "
                           "Enter number or leave blank for regular 52 card deck ")
        if len(deck_size) == 0: deck_size = 1
        total_decks = int(deck_size) * 52
        unique_cards = int(total_decks/len(self.cards))
        for card in self.cards:
            self.deck[card] = unique_cards
        return self.deck

    def deal_cards(self, cards_to_deal):
        """
        Retruns a random card from the deck to a player,
        and then updates the deck to account for dealt card
        :param cards_to_deal:
        :return: Returns the card for the player
        """
        cards_to_return = list()
        for i in range(cards_to_deal):
            random_card = random.choice(list(self.deck.keys()))
            # Reduce card count in deck by 1
            # and then remove entirely from deck if count
            # reaches 0
            self.deck[random_card] = self.deck[random_card] - 1
            if self.deck[random_card] == 0: del self.deck[random_card]
            cards_to_return.append(random_card)

        return cards_to_return