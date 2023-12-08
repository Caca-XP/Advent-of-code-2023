from functools import cmp_to_key

test = open('input7.txt', 'r')
test = test.read().split('\n')

##### Part 1

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
score = ['Five of a Kind', 'Four of a Kind', 'Full House', 'Three of a Kind', 'Two Pair', 'Pair', 'High Card']

def check_hand(hand):
    dict = {}
    for card in hand:
        if card in dict.keys():
            dict[card] += 1
        else:
            dict[card] = 1
    if 5 in dict.values():
        return score[0]
    elif 4 in dict.values():
        return score[1]
    elif 3 in dict.values() and 2 in dict.values():
        return score[2]
    elif 3 in dict.values():
        return score[3]
    elif list(dict.values()).count(2) == 2:
        return score[4]
    elif 2 in dict.values():
        return score[5]
    else:
        return score[6]

def compare(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    if score.index(check_hand(hand1)) > score.index(check_hand(hand2)):
        return -1
    elif score.index(check_hand(hand1)) < score.index(check_hand(hand2)):
        return 1
    else:
        for i in range(len(hand1)):
            if cards.index(hand1[i]) > cards.index(hand2[i]):
                return -1
            elif cards.index(hand1[i]) < cards.index(hand2[i]):
                return 1
        return 0

winnings = 0
hands_and_bids = []
for line in test:
    if line == "":
        continue
    hand, bid = line.split(" ")
    hands_and_bids.append([hand, int(bid)])

# sort hands_and_bids with compare function
sorted_hands_and_bids = sorted(hands_and_bids, key=cmp_to_key(compare))

for i in range(len(sorted_hands_and_bids)):
    winnings += sorted_hands_and_bids[i][1] * (i+1)

# print(sorted_hands_and_bids)
print(winnings)

##### Part 2
cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
score = ['Five of a Kind', 'Four of a Kind', 'Full House', 'Three of a Kind', 'Two Pair', 'Pair', 'High Card']

def check_hand(hand):
    dict = {}
    jokers = 0
    for card in hand:
        if card in dict.keys():
            dict[card] += 1
        else:
            dict[card] = 1
    jokers = dict.pop('J', 0)
    if jokers == 5:
        return score[0]
    maxed = dict.pop(max(dict, key=dict.get))
    if 5 in dict.values() or maxed + jokers == 5:
        return score[0]
    elif 4 in dict.values() or maxed + jokers == 4:
        return score[1]
    elif (3 in dict.values() and 2 in dict.values()) or (maxed + jokers == 3 and 2 in dict.values()):
        return score[2]
    elif 3 in dict.values() or maxed + jokers == 3:
        return score[3]
    elif list(dict.values()).count(2) == 2 or maxed + max(dict.values()) == 4:
        return score[4]
    elif 2 in dict.values() or maxed + jokers == 2:
        return score[5]
    else:
        return score[6]

def compare(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    if score.index(check_hand(hand1)) > score.index(check_hand(hand2)):
        return -1
    elif score.index(check_hand(hand1)) < score.index(check_hand(hand2)):
        return 1
    else:
        for i in range(len(hand1)):
            if cards.index(hand1[i]) > cards.index(hand2[i]):
                return -1
            elif cards.index(hand1[i]) < cards.index(hand2[i]):
                return 1
        return 0

winnings = 0
hands_and_bids = []
for line in test:
    if line == "":
        continue
    hand, bid = line.split(" ")
    hands_and_bids.append([hand, int(bid)])

# sort hands_and_bids with compare function
sorted_hands_and_bids = sorted(hands_and_bids, key=cmp_to_key(compare))

for i in range(len(sorted_hands_and_bids)):
    winnings += sorted_hands_and_bids[i][1] * (i+1)

# for i in range(len(sorted_hands_and_bids)):
#     print((i+1), sorted_hands_and_bids[i][0], check_hand(sorted_hands_and_bids[i][0]), sorted_hands_and_bids[i][1])

print(winnings)