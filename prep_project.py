import random
import time


INTRODUCTION = '''

Come on down! You are the next contestants on the Price is Right!


2 people are needed to play this game. You will be presented with 
a prize and both contestants will guess the price of the item.


Whoever is the closest to the actual price of the prize without 
going over, will be the winner of the bidding game and will move
onto a second game!


'''

GAME_TWO_EXPLANATION = '''

In this next game, the winner of the bidding game will get to 
guess the numbers contained within a price for a new prize!


'''

#Price Points and Ranges for Prizes
washer_price = random.randint(450,600)   #Whirlpool Washing Machine
iron_price = random.randint(20,40)   #Black+Decker Iron
vacuum_price = random.randint(99,198)    #Hoover
fridge_price = random.randint(500,1500) #Frigidaire
blender_price = random.randint(350,600)  #Vitamix
tv_price = random.randint(329,630)  #LG
ipad_price = random.randint(329,799)
hairdryer_price = random.randint(10,38)  #Revlon
car_price = random.randint(19500,27195)  #Toyota Corolla 2020
lv_bag_price = (1327, 2091, 1423, 1586, 1403, 1596, 1940, 4709, 3704, 3950, 3254, 3561, 3802, 3908, 4056, 5408, 1927, 1042, 1430, 1750, 5206, 1230, 1530, 1620, 2160, 1850, 4950, 3512, 4650, 3750, 1470, 1025, 5703) # Louis Vuitton
bbq_price = (451, 349, 490, 847, 354, 613, 985, 423, 896, 672, 718, 609, 692, 795, 819) # Weber Barbeque
oven_price = (548, 679, 483, 692, 435, 396, 674, 781, 764, 649, 523, 584, 851, 740) # GE Oven
dryer_price = (478, 561, 782, 573, 724, 849, 695, 829, 549, 781, 874, 654, 892, 943) # Maytag Dryer
bmw_price = (49701, 50172, 51789, 52341, 56793, 57901, 58430, 59147, 60598, 61852, 62310, 63142, 64209) # BMW Z4 convertible
ducati_price = (20132, 20796, 23189, 24197, 13290, 16792, 14793, 17395, 19357, 19248, 16503, 20789, 25491, 24395, 15493, 17895, 21495, 27895, 39785, 12985, 15297) # Ducati Motorcycle


#List of Prizes to Randomly select from
prize_list = ("Whirlpool Washing Machine", "Black+Decker Iron", "Hoover Vacuum Cleaner", "Frigidaire Refrigerator", "Vitamix Blender", "LG 50 inch TV", "Apple iPad", "Revlon Hair Dryer", "2020 Toyota Corolla")

prize_list_second = ("Louis Vuitton Handbag", "Weber Barbeque Grill", "GE Oven", "Maytag Dryer", "BMW Convertible Z4 Sports Car", "Ducati Motorcycle")


def select_prize_price(prize_item):
    '''Setting Prize's Randomized Price'''

    if prize_item == "Whirlpool Washing Machine":
        price = washer_price
        return(price)
        
    elif prize_item == "Black+Decker Iron":
        price = iron_price
        return(price)
        
    elif prize_item == "Hoover Vacuum Cleaner":
        price = vacuum_price
        return(price)
        
    elif prize_item == "Frigidaire Refrigerator":
        price = fridge_price
        return(price)
        
    elif prize_item == "Vitamix Blender":
        price = blender_price
        return(price)
       
    elif prize_item == "LG 50 inch TV":
        price = tv_price
        return(price)
        
    elif prize_item == "Apple iPad":
        price = ipad_price
        return(price)
        
    elif prize_item == "Revlon Hair Dryer":
        price = hairdryer_price
        return(price)
        
    elif prize_item == "2020 Toyota Corolla":
        price = car_price
        return(price)

    elif prize_item == "Louis Vuitton Handbag":
        price =  random.choice(lv_bag_price)
        return(price)

    elif prize_item == "Weber Barbeque Grill":
        price =  random.choice(bbq_price)
        return(price)

    elif prize_item == "GE Oven":
        price =  random.choice(oven_price)
        return(price)

    elif prize_item == "Maytag Dryer":
        price =  random.choice(dryer_price)
        return(price)

    elif prize_item == "BMW Convertible Z4 Sports Car":
        price =  random.choice(bmw_price)
        return(price)

    elif prize_item == "Ducati Motorcycle":
        price =  random.choice(ducati_price)
        return(price)



def play_main_game():
    ''' Beginning of The Price is Right - Bidding Game'''
            
    print(INTRODUCTION)
    time.sleep(2)

    #Selecting Random Price from List of Prizes
    current_prize = random.choice(prize_list)

    #Select random price from price range
    price = select_prize_price(current_prize)

    #Tell Contestants the Prize Item for Bidding
    print("The prize you will be bidding on is...")
    time.sleep(2)
    print()
    print("A " + current_prize + "!")
    print()
    print()
    print()
    time.sleep(2)

    #Get P1 Bid
    print("Contestant Number 1. Please enter your bid on the prize's price.")
    p1_bid = int(input("Bid: $"))
    print()
    print()
    time.sleep(1)

    #Get P2 Bid
    print("Contestant Number 2. Please enter your bid on the prize's price.")
    p2_bid = int(input("Bid: $"))
    print()
    print()
    time.sleep(1)

    #Find if bids were over and who is closest to price
    p1_diff = price - p1_bid
    p2_diff = price - p2_bid

    if (p1_diff > 0) and (p1_diff < p2_diff) or (p1_diff > 0) and (p2_diff < 0):
        print("The price of the {} was ${}.".format(current_prize, price))
        time.sleep(2)
        print()
        print()
        print("Contestant Number 1 is the winner! You have won the {} and get to move onto the next game!".format(current_prize))

    elif (p2_diff > 0) and (p2_diff < p1_diff) or (p2_diff > 0) and (p1_diff < 0):
        print("The price of the {} was ${}.".format(current_prize, price))
        time.sleep(2)
        print()
        print()
        print("Contestant Number 2 is the winner! You have won the {} and get to move onto the next game!".format(current_prize))

    else:
        print("It looks like you both overbid!")

    time.sleep(5)
    print()
    print()
    print()
    print()
    print()
    print("================ GAME TWO ================")
    print()
    print()
    time.sleep(2)
        

def handle_guess(guess, guessed, second_prize_price):
    """Handle guess by player."""

    #Keep track that they made this guess
    guessed.append(guess)
            
    if guess in second_prize_price:
        print("Good job! The number {} is contained within the price!".format(guess))
    else:
        print("Bummer! The number {} in not in the price.".format(guess))


def show_price(second_prize_price, guessed):
    """Show price with correct numbers filled in."""

    result = ""

    for number in second_prize_price:
        if number in guessed:
            result = result + number
        else:
            result = result + "-"

    print("Price: $" + result)
    print()
    print()


def end_game(second_prize_price, guessed, player_guess_num, max_guess_num):
    """Should the game end? (True or False)"""
    
    #Check if the player has gone over the maximum number of guesses allowed
    while player_guess_num < max_guess_num:

        #Loop whether all numbers in price are contained within guessed list
        for number in second_prize_price:
            if not (number in guessed):
                return False

        return True


def has_won(second_prize_price, guessed):

    for number in second_prize_price:
        if not (number in guessed):
            return False
    return True


def play_second_game():
    """Begin second game with winner of first game"""

    print(GAME_TWO_EXPLANATION)
    time.sleep(3)

    #Create empty list to track player guesses
    guessed = []

    #Select Prize Name from Second Prize List
    second_prize = random.choice(prize_list_second)

    #Set a Price Point from List of Prices aligned with selected prize - set to string type
    second_prize_price = str(select_prize_price(second_prize))
    
    #Find length of price in digits
    max_guess_num = len(str(second_prize_price))

    print("Let's check out the prize you are bidding on!")
    print()
    time.sleep(2)
    print("The prize is... A " + second_prize + "!")
    print()
    time.sleep(2)
    print("There are {} digits in the price.".format(max_guess_num))   
    print()

    #Set maximum amount of guesses based on amount of digits in price
    if max_guess_num < 4:
        max_guess_num = max_guess_num + 2
    else:
        max_guess_num = max_guess_num +1

    time.sleep(1)
    print("You have {} guesses at the numbers within the prize's price.".format(max_guess_num))
    print()
    time.sleep(1)
    print("If you get the price right before you run out of guesses, you win the {}!".format(second_prize))
    print()
    print()
    print()
    time.sleep(2)
    player_guess_num = 0

    #Loop until end game function is True
    while end_game(second_prize_price, guessed, player_guess_num, max_guess_num) is False:
        
        #Take player guess input and increment guesses by 1
        guess = input("Guess a number between 0 and 9 > ")
        print()
        print()

        player_guess_num += 1
        
        #Add guess to guessed list and show player results
        handle_guess(guess, guessed, second_prize_price)
        show_price(second_prize_price, guessed)

    #Check if player ended game with too many guesses or they won
    if has_won(second_prize_price, guessed) is True:
        time.sleep(1)
        print("You did it! You just won a {}!".format(second_prize))
        time.sleep(1)
        print()
        print("Thank you for playing The Price is Right!")
    else:
        time.sleep(1)
        print("Unfortunately, you did not win. The price for the {} was ${}.".format(second_prize,second_prize_price))
        time.sleep(1)
        print()
        print("You didn't win, but thank you for playing The Price is Right!")


play_main_game()

play_second_game()




