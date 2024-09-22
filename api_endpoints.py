# Importing the required packages
import requests
from config import BASE_URL, BREWERY_TYPES

def determine_endpoint(criteria, criteria_prompt=None):
    """
    Determines the API endpoint based on user-selected criteria.

    Arguments:
        criteria: The type of criteria for filtering breweries, used to make a correct API-request.
        criteria_prompt: based on the user's selected option, helps the user with their input.

    Returns:
        The query string for the API request.

    """
    if criteria_prompt:  # Only show this prompt if the user chose anything besides all breweries.
        print(f"\n*LISTING BREWERIES BY {criteria_prompt.upper()}*")

        # if user chose to sort by brewery type.
        if criteria_prompt == "brewery type":
            print("\nYou can choose one of the following types:\n")
            for type in BREWERY_TYPES:
                print(type) # List the brewery types.

            while True:
                user_input = input(f"\nPlease enter a {criteria_prompt}: ").strip().lower().replace(" ", "_")

                # Check if the input is a valid brewery type
                if user_input in BREWERY_TYPES:
                    search_criteria = f"?by_{criteria}={user_input}&"
                    break  # Exit the loop if valid input is provided
                else:
                    print(f"\nThat's not a valid brewery type, please try again!")

        else:
            user_input = input(f"\nPlease enter a {criteria_prompt}: ").strip().lower().replace(" ", "_")
            search_criteria = f"?by_{criteria}={user_input}&"

    else: # No prompt needed for listing all breweries
        search_criteria = "?"

    return search_criteria

def get_brewery_count(query_string):
    """
    Gets the total number of breweries based on the query string.

    Arguments:
        query_string: The query string for the API request.

    Returns:
        The total number of breweries if successful, else None.

    """
    try:
        # Making API-request to get the total amount of breweries.
        response = requests.get(BASE_URL + '/meta' + query_string)

        # Checking response status.
        if response.status_code != 200:
            print(f"Error getting brewery count: {response.status_code}")
            return None
        # Return the amount of breweries based on the criteria.
        else:
            metadata = response.json()
            total = int(metadata['total'])
            return total

    # Handle errors
    except requests.exceptions.RequestException as e:
        print(f"Error getting brewery count: {e}")
        return None

def list_breweries(total_breweries, query_string):
    """
     Lists breweries based on the total count and query string.

     Args:
         total_breweries: The total number of breweries to display, used for pagination.
         query_string: The query string for the API request.
     """
    # Variables essential for pagination.
    page_count = 1 # Starting on the first page.
    per_page = 10
    max_pages = (total_breweries // per_page) + 1 # Max pages calculated with total_breweries using metadata fetched earlier.
    stop_loop = False # Used to stop or continue loop that's used for the pagination.

    while True:
        print(f"\n*Page number: {page_count}*\n")
        try:
            # Making API-request to get the breweries on the current page.
            response = requests.get(BASE_URL + query_string + f"page={page_count}&per_page={per_page}")

            # Checking response status.
            if response.status_code != 200:
                print(f"Request failed, try again. Status code: {response.status_code}")
            else:
                # Display details for every brewery.
                all_breweries = response.json()
                for brewery in all_breweries:
                    print(f"Name: {brewery['name']}")
                    print(f"Type of brewery: {brewery['brewery_type']}")
                    print(f"Country: {brewery['country']}")
                    print(f"State: {brewery['state']}")
                    print(f"City: {brewery['city']}")
                    print(f"Postal code: {brewery['postal_code']}")
                    print(f"Street: {brewery['address_1']}")
                    print(f"Website: {brewery['website_url']}")
                    print("-" * 50)

        # Handle erros.
        except requests.exceptions.RequestException as e:
            print(f"Request failed, try again: {e}")
            return None

        while True:
            # User prompt with options to go to the next page, pick a specific page, or stop.
            if page_count < max_pages:  # If not at the last page yet
                print(f"Do you wish to go to the next page (page {page_count + 1})?")
                next_page = input(f"\nPress 'enter' for next page, pick a page number(max = {max_pages}), or type 'stop' to quit: ").lower().strip()
            else:  # On the last page
                print(f"You have reached the last page (page {page_count}). Do you wish to return to page 1?")
                next_page = input(f"\nPress 'enter' for page 1, pick a page number(max = {max_pages}), or type 'stop' to quit: ").lower().strip()

            # The user input is handled below.
            if next_page == 'stop':
                stop_loop = True # This stops this current while-loop
                break
            elif next_page.isdigit():  # check if the user entered a page number.
                chosen_page = int(next_page)
                if 1 <= chosen_page <= max_pages:
                    page_count = chosen_page  # Set the page_count as the page the user has chosen.
                    break
                else:
                    print(f"\nInvalid page number. Please pick a number between 1 and {max_pages}.\n")
            elif page_count == max_pages:  # If the last page is reached, restart or stop.
                page_count = 1  # Restart from page 1 if the user doesn't type 'stop'.
                break
            else:
                page_count += 1  # Go to the next page
                break

        if stop_loop:
            print("\nExiting... Going back to main menu")
            break
