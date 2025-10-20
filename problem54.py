def hand_type(cards: list[str]) -> int:
    possible_hands = {
        "High Card": 1, # done
        "One Pair": 2, # done
        "Two Pair": 3, # done
        "Three of a Kind": 4, # done
        "Straight": 5, # done
        "Flush": 6, # done
        "Full House": 7, # done
        "Four of a Kind": 8, # done
        "Straight Flush": 9, # done
        "Royal Flush": 10 # done
    }
    
    ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    
    cards = sorted(cards, key=lambda x: ranks[x[0]])
    
    distinct_nums = []
    for i in range(len(cards)):
        if cards[i][0] not in distinct_nums:
            distinct_nums.append(cards[i][0])
    
    num_count = {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "T": 0,
        "J": 0,
        "Q": 0,
        "K": 0,
        "A": 0,
    }

    for card in cards:
        num_count[card[0]] += 1

    num_of_pairs = 0

    for i in num_count:
        if num_count[i] >= 2:
            num_of_pairs += 1
    
    suit = cards[0][1]
    all_same_suit = all(cards[i][1] == suit for i in range(len(cards)))
    ace_present = any(cards[i][0] == 'A' for i in range(len(cards)))
    consecutive = all(ranks[cards[i][0]] + 1 == ranks[cards[i+1][0]] for i in range(len(cards)-1))
    unique_nums = len(distinct_nums)
    three_of_a_kind = any(count == 3 for count in num_count.values())
    four_of_a_kind = any(count == 4 for count in num_count.values())
    
    if all_same_suit and consecutive and ace_present:
        return possible_hands["Royal Flush"]
    if all_same_suit and consecutive:
        return possible_hands["Straight Flush"]
    if all_same_suit:
        return possible_hands["Flush"]
    if consecutive:
        return possible_hands["Straight"]
    if four_of_a_kind:
        return possible_hands["Four of a Kind"]
    if unique_nums == 2 and three_of_a_kind:
        return possible_hands["Full House"]
    if three_of_a_kind:
        return possible_hands["Three of a Kind"]
    if num_of_pairs == 2:
        return possible_hands["Two Pair"]
    if num_of_pairs == 1:
        return possible_hands["One Pair"]
    
    return 1

def draw(player1: list[str], player2: list[str]) -> int:
    ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    
    p1_score = hand_type(player1)
    p2_score = hand_type(player2)
    
    if p1_score != p2_score:
        raise Exception(f"Hands are different types, but draw() was called\n{player1}\t{player2}")

    if p1_score != 1 and p1_score != 2:
        raise Exception(f"Only One Pair and High Card has been handled\n{player1}\t{player2}")
    
    if p1_score == 2:
        p1_count = {
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "T": 0,
            "J": 0,
            "Q": 0,
            "K": 0,
            "A": 0,
        }
        
        p2_count = {
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "T": 0,
            "J": 0,
            "Q": 0,
            "K": 0,
            "A": 0,
        }
        
        for i in range(len(player1)):
            p1_count[player1[i][0]] += 1
            p2_count[player2[i][0]] += 1
        
        p1_num = ranks[[i for i in p1_count if p1_count[i] == 2][0]]
        p2_num = ranks[[i for i in p2_count if p2_count[i] == 2][0]]
        
        if p1_num > p2_num:
            return 1
        if p2_num > p1_num:
            return 2
        
        high_card_tiebreaker = sorted(player1 + player2, key=lambda x: ranks[x[0]], reverse=True)
        if high_card_tiebreaker[0] in player1:
            return 1
        elif high_card_tiebreaker[0] in player2:
            return 2
        
        raise Exception(f"Something went wrong while calculating One Pair\n{player1}\t{player2}")
    
    if p1_score == 1:
        new_list = sorted(player1 + player2, key=lambda x: ranks[x[0]], reverse=True)
        if new_list[0] in player1:
            return 1
        elif new_list[0] in player2:
            return 2
    
    
    raise Exception("Hands have same value")



file = open("./files/0054_poker.txt")

lines = []
for line in file:
    lines.append(line.replace("\n", "").split(" "))

count = 0

for line in lines:
    player_1 = hand_type(line[:5])
    player_2 = hand_type(line[5:])
    
    winner = 0
    
    if player_1 > player_2:
        winner = 1
    elif player_1 == player_2:
        # if player_1 == 0:
            # print("found")
        winner = draw(line[:5], line[5:])
    else:
        winner = 2
    
    if winner == 1:
        count += 1

print(count)