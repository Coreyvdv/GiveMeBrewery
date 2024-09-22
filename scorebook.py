def view_scorebook():
    """
    Creates a scorebook.txt file if there is none present yet.
    Shows entries in scorebook.txt, if present.
    """
    try:
        # Open a scorebook.txt file with mode = read.
        with open("scorebook.txt", "r") as file:
            scorebook = file.read() # Read the file.

        # Display the contents of the file if there's a scorebook.txt file present and there are entries.
        if len(scorebook) != 0:
            print("\n*These are all your entries:*")
            print(f"\n{scorebook}")
        else:
            print("\nYour scorebook is empty at this time! Add something to your scorebook first.")

    # If there's no scorebook.txt file, or if it's empty, user is made aware of this.
    except FileNotFoundError:
        print("\nYour scorebook is empty at this time! Add something to your scorebook first.")

def edit_scorebook():
    """
    Makes a new scorebook.txt file if there is none present yet.
    appends a scorebook entry to the scorebook.txt file.

    """
    while True:
        # User gives a new entry.
        brewery = input("\nPlease enter what brewery made this beer: ")
        beer = input("\nPlease enter the beer you would like to add to your scorebook: ")
        score = input("\nPlease enter what score you would give this beer: ")
        notes = input("\nPlease enter any notes you would like to add to this beer: ")

        # User is made aware of their entry.
        print("\nThe following has been added to your scorebook: ")
        print(f"\nBrewery: {brewery}"
              f"\nBeer: {beer}"
              f"\nScore: {score}"
              f"\nNotes: {notes}")

        # The new entry is appended to the scorebook.
        with open("scorebook.txt", "a") as file:
            file.write(f"Brewery: {brewery}"
                       f"\nBeer: {beer}"
                       f"\nScore: {score}"
                       f"\nNotes: {notes}"
                       "\n\n")

        # User can add more entries if they would like.
        add_more = input("\nWould you like to add anything else to your scorebook [y/n]? ").lower().strip()

        if add_more == "y":
            continue # Loop is repeated for another entry
        else:
            print("\nAlright! Sending you back to the main menu...")
            break # Loop is stopped, user is sent back to main menu.
