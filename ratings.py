"""Restaurant rating lister."""
# open the file
# initialize a dict
# loop over lines in file
# split at ":"
# set restaurant name to be the first element
# set rating to be the second element
# add rest name to dict and set rating
# get list of keys of dict
# sort list of keys
# loop over sorted list
# look up rest name
# format then print rest name and value 

def add_new_rating():
    """Return new rest and rating from user input"""
    print("Let's add a new restaurant rating!")
    restaurant = input("Restaurant name: ")
    rating = input("Rating (from 1-5): ")
    # make sure rating is int
    # make sure is within range(1, 5)
    while (rating.isdigit() == False 
          or int(rating) < 1 or int(rating) > 5):
        print("Please enter number between 1 and 5!")
        rating = input("Rating (from 1-5): ")

    # create a restaurant variable by getting input
    # create rating variable by getting input 

    return [restaurant, rating]



# put your code here
def get_restaurant_ratings(file_name, add_new = False):
    """Given file with restaurant ratings, return formated string with name and rating"""

    restaurant_ratings = {}
    with open(file_name) as opened_file:
        
        for line in opened_file:
            line = line.rstrip()
            line_list = line.split(":")
            restaurant = line_list[0]
            rating =line_list[1]
            restaurant_ratings[restaurant] = rating

    if add_new:
        new_rating = add_new_rating()
        new_rest = new_rating[0]
        new_rating = new_rating[1]
        restaurant_ratings[new_rest] = new_rating

    restaurants_list = sorted(restaurant_ratings.keys())

    for restaurant in restaurants_list:
        print(f"{restaurant} is rated at {restaurant_ratings[restaurant]}.")


def get_user_choice():

    # ask user input on choices
    print("Hi, what would you like to do?\n (S)ee all\n (A)dd new\n (Q)uit")
    # see all is A
    # add new is B
    # quit is Q
    choice = input("> ")
    # if input == Q, do nothing
    if choice == "S":
        get_restaurant_ratings("scores.txt")
    elif choice == "A":
        get_restaurant_ratings("scores.txt", True)

    # if input == A, call get_restaurant_ratings 
    # if input == B, call get_restaurant_ratings with choice = True

get_user_choice()


