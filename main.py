from player import Player, Deck

def game_inputs():
   # Build card deck
    deck = Deck()
    deck.get_deck_count()

    # Get all players
    player_names_raw = input("Enter names separated by space:  ")
    players_names_list = player_names_raw.split(" ")

    # Add dealer automatically to player dictionary
    dealer = Player("Dealer")
    players = {"Dealer" : dealer}
    #players = dict()

    for name in players_names_list:
        players[name] = Player(name)
        #player = Player(name)
    return players, deck

def play_game(players,deck):

    # Deal cards
    for name in players:
        cards_from_deck = deck.deal_cards(2)
        for card in cards_from_deck:
            players[name].card_hand.append(card)
            players[name].add_card_value(card)

    for name in players:

        if name == "Dealer":
            while players[name].card_value < 17:
                new_card = deck.deal_cards(1)
                players[name].card_hand.append(new_card[0])
                players[name].add_card_value(new_card[0])
                if players[name].card_value > 21:
                    players[name].busted = True

        else:
            print(f"Player {players[name].name}, "
                  f"Hand: {players[name].card_hand}, "
                  f"Card Value: {players[name].card_value}")

            if players[name].card_value < 21:
                hit = input("Hit? If no, you hold (y/n):  ")
                while hit == "y" and players[name].card_value < 21:
                    new_card = deck.deal_cards(1)
                    for card in new_card:
                        players[name].card_hand.append(card)
                        players[name].add_card_value(card)
                    print(f"Player {players[name].name}, "
                          f"Hand: {players[name].card_hand}, "
                          f"Card Value: {players[name].card_value}")
                    if players[name].card_value > 21:
                        print("You Bust")
                        players[name].busted = True
                        break
                    elif players[name].card_value == 21:
                        print("You win!")
                        break
                    hit = input("Hit? If no, you hold (y/n):  ")
    for name in players:
        if name == "Dealer": continue
        elif not players[name].busted and players[name].card_value < players["Dealer"].card_value:
            players[name].beat_dealer = True
    return players,deck

def main():
    players, full_deck = game_inputs()
    final_hand, final_deck = play_game(players,full_deck)
    for name in players:
        if name == "Dealer": continue
        print(f"Player {players[name].name}, "
              f"Hand: {players[name].card_hand}, "
              f"Card Value: {players[name].card_value} "
              f"Beat Dealer?: {players[name].beat_dealer}")
        print(final_deck.deck)
main()

