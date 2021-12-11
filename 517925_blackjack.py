# ----------------------------------------------------------------------------
# |
# | File:         517925_blackjack.py
# | Author:       Tan Duc Mai
# | Student ID:   517925
# | Description:  Assignment 2 - Implement a card game called Blackjack (21)
# | This is my own work as defined by Eynesbury
# | Academic Misconduct policy.
# |
# ----------------------------------------------------------------------------


# ------------------------------- Module Import -------------------------------
import card_deck


# ---------------------------- Function Definitions ---------------------------
def display_details(filename, author, student_id):
    """Display the author's details."""
    print(f'File   : {filename}',
          f'Author : {author}',
          f'ID     : {student_id}',
          f'This is my own work as defined by the',
          f'Eynesbury Academic Integrity Policy.',
          sep='\n',
          end='\n\n',
    )


def input_name():
    """Prompt for, read, and validate the player's name.

    Returns
    -------
    str
        The valid user's input name.
    """
    username = None

    while username is None or ' ' in username or len(username) >= 12:
        username = input('Enter your name: ')
        if ' ' in username or len(username) >= 12:
            print('ERROR: Must be 1 word and less than 12 characters.')
        print()

    return username


def display_hand(player_name, hand):
    """Displays the hand and its total to the screen.

    Parameters
    ----------
    player_name : str
        It is either the user's name or "Dealer".
    hand : list
        The list of cards, either the dealer_hand or player_hand list.

    Returns
    -------
    None
    """
    # Output the hand.
    print(f'{player_name}\'s hand', end=': ')

    if player_name != 'Dealer':
        i = 0
        for card in hand:
            i += 1
            if i < len(hand):
                print(card[0], 'of', card[1], end=', ')
            else:
                print(card[0], 'of', card[1])
    else:
        print(hand[0][0], 'of', hand[0][1])

    # Output the total value.
    print(f'Hand Total: ({get_hand_total(hand)})', end='\n\n')


def get_hand_total(hand):
    """Take a list of cards and returns the total point value of them.

    Parameters
    ----------
    str
        The cards drawn.

    Returns
    -------
    int
        The total point value of all card values in the 'hand'.
    """
    # Variable initialisation.
    point = 0
    count_ace = 0

    # Add the value of cards.
    for card in hand:
        if card[0] == 'Ace':
            count_ace += 1
        elif card[0] in ['Jack', 'Queen', 'King']:
            point += 10
        else:
            point += int(card[0])

    # Determine the value of Ace cards.
    if (point + 11*count_ace) <= 21:
        point += 11*count_ace
    else:
        point += 1*count_ace

    return point


def input_hit_choice():
    """Prompt for, read, and validate the user's choice.

    Returns
    -------
    str
        The valid user choice which is either 'h' (hit) or 's' (stand).
    """
    choice = None
    valid_choices = ['h', 's']

    while choice is None or choice not in valid_choices:
        choice = input('Do you want to hit or stand (h/s): ')
        if choice not in valid_choices:
            print("ERROR: Must be 'h' or 's'.")
    print()

    return choice


def player_play(name, hand):
    """Continue to draw cards until the user responds 's' (stand) or
       their cards' total exceeds 21.

    Parameters
    ----------
    name : str
        The player's name.
    hand : list
        The list of cards drawn by the player.

    Returns
    -------
    None
    """
    user_hit = None

    while user_hit is None or (user_hit == 'h' and get_hand_total(hand) <= 21):
        user_hit = input_hit_choice()

        if user_hit == 'h':
            # Draw another card.
            hand.append(card_deck.draw_card())
            # Output the total value.
            display_hand(name, hand)


def dealer_play(hand):
    """Continue to draw cards until the dealer's cards' total reaches 17.

    Parameters
    ----------
    list
        The list of cards drawn by the dealer.

    Returns
    -------
    None
    """
    dealer_hit = None

    while dealer_hit is None or (dealer_hit == '' and get_hand_total(hand) >= 17):
        # Draw another card.
        hand.append(card_deck.draw_card())
        # Output the total value.
        display_hand('Dealer', hand)

        dealer_hit = input('Press "Enter" to continue...')
        print()


def play_game():
    print("--------- Welcome to Blackjack ---------\n")

    # Display the author's details.
    display_details('517925_blackjack.py', 'Tan Duc Mai', '517925')

    # Variable initialisation.
    valid_answers = ['y', 'n']
    rounds = 0
    dealer_hand = []
    player_hand = []

    # Ask to play.
    play = None
    while play is None or play not in valid_answers:
        play = input('Do you want to play blackjack (y/n): ')
        if play not in valid_answers:
            print("ERROR: Only enter 'y' or 'n'")

    # Start the game if the user responds 'y'.
    if play == valid_answers[0]:
        name = input_name()

        while play == valid_answers[0]:
            rounds += 1

            # Draw cards.
            dealer_hand.append(card_deck.draw_card())

            for _ in range(2):
                player_hand.append(card_deck.draw_card())

            # Display hands.
            display_hand('Dealer', dealer_hand)
            display_hand(name, player_hand)

            # Check for Blackjack.
            dealer_point = get_hand_total(dealer_hand)
            player_point = get_hand_total(player_hand)
            count_21 = [dealer_point, player_point].count(21)

            if count_21 == 0:
                player_play(name, player_hand)
                dealer_play(dealer_hand)
            elif count_21 == 2:
                print('Two player blackjack!-> Push!')
                print()
            else:
                print('Blackjack', end='! ')
                if dealer_point == 21:
                    print('Dealer wins!')
                else:
                    print(f'{name} wins!')
                print()

            # Reset the card once a game is complete.
            dealer_hand = []
            player_hand = []

            # Ask to play again.
            again = None
            while again is None or again not in valid_answers:
                again = input('Do you want to play again (y/n): ')
                if again not in valid_answers:
                    print("ERROR: Only enter 'y' or 'n'")
            play = again
            print()

        # Summary.
        print(f'You played {rounds} games.')

    else:
        print('Maybe next time...')


# --------------------------- Call the Main Function --------------------------
if __name__ == '__main__':
    play_game()
    print("\n---------- See you again soon ----------")
