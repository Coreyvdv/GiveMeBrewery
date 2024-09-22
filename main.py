# Importing the required packages
from config import USER_OPTIONS
from api_endpoints import determine_endpoint, get_brewery_count, list_breweries
from scorebook import view_scorebook, edit_scorebook

def welcome_statement():
    """
    User is welcomed by the application.
    Credit is given to the maker of the app and creator of the Open Brewery Database.
    """
    print("Welcome to GiveMeBrewery! (v1.0)")
    print("GiveMeBrewery is made by Corey.")
    print("It uses the Open Brewery Database created by Chris J Mears.\nPlease read about it here: https://www.openbrewerydb.org/")

def user_picks_option():
    """
    Available options are enumerated and listed for the user.
    The user is asked to pick an option, the user's choice is saved and corresponding code will be executed.

    Returns:
        the choice the user made, turned into an integer. Must be one of the options listed.
    """
    print("\n*MAIN MENU*")
    print("\nYou can do the following:")

    # Items in USER_OPTIONS are enumerated and listed.
    for index, option in enumerate(USER_OPTIONS, start=1):
        print(f"[{index}]: {option}")

    # User is asked to choose one of the listed options.
    try:
        user_choice = int(input("\nPlease choose what you want to do at this time: ").strip())
        if user_choice not in range(1, len(USER_OPTIONS) + 1):
            raise ValueError
        else:
            return user_choice

    # If the user's input is not a valid option, they get an error message and have to try again.
    except ValueError:
        print(f"\nThat's not a valid option, please pick between option 1 and {len(USER_OPTIONS)}.")
        print("Also, please make sure you insert a number.")

if __name__ == "__main__":
    welcome_statement()
    while True:
        chosen_option = user_picks_option()
        if chosen_option == 1:
            search_query = determine_endpoint("")
            brewery_count = get_brewery_count(search_query)
            list_breweries(brewery_count, search_query)
        elif chosen_option == 2:
            search_query = determine_endpoint("state", "state")
            brewery_count = get_brewery_count(search_query)
            list_breweries(brewery_count, search_query)
        elif chosen_option == 3:
            search_query = determine_endpoint("city", "city")
            brewery_count = get_brewery_count(search_query)
            list_breweries(brewery_count, search_query)
        elif chosen_option == 4:
            search_query = determine_endpoint("type", "brewery type")
            brewery_count = get_brewery_count(search_query)
            list_breweries(brewery_count, search_query)
        elif chosen_option == 5:
            view_scorebook()
        elif chosen_option == 6:
            edit_scorebook()
        elif chosen_option == len(USER_OPTIONS):
            print("\nThank you for using GiveMeBrewery. See you next time!")
            break
