# Program to simulate a deck of cards so flip over a random one for different
# workouts so you do a random amount of reps per set

# Imports
from random import randint, shuffle


# Set up Ordered Deck
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []

for suit in suits:
    for value in values:
        deck.append(f'{value} of {suit}')


# Run program
shuffle(deck)
keep_going = ''
card_count = 0
total_reps = 0

exercise = input('Name your excersise: ')

while len(deck) and keep_going == '':
    card = deck[randint(0, len(deck) - 1)]
    print(card)

    value = 0
    card_value = card.split(' ')[0]

    if len(card_value) < 3:
        value = int(card_value)
    elif card_value == 'Jack' or card_value == 'Queen' or card_value == 'King':
        value = 10
    else:
        value = 11
    print(f'Do {value} {exercise}s!')

    card_count += 1
    total_reps += value

    deck.remove(card)

    keep_going = input('Press any button to stop.')

print(f'You did {total_reps} {exercise}s, using {card_count} cards.')
