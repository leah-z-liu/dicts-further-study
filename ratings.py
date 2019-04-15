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


# put your code here
def get_restaurant_ratings(file_name):
    """Given file with restaurant ratings, return formated string with name and rating"""

    restaurant_ratings = {}
    with open(file_name) as opened_file:
        
        for line in opened_file:
            line = line.rstrip()
            line_list = line.split(":")
            restaurant = line_list[0]
            rating =line_list[1]
            restaurant_ratings[restaurant] = rating

    restaurants_list = sorted(restaurant_ratings.keys())

    for restaurant in restaurants_list:
        print(f"{restaurant} is rated at {restaurant_ratings[restaurant]}.")

get_restaurant_ratings("scores.txt")



