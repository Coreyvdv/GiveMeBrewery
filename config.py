# Describing the base URL for the API we will be using for this application
BASE_URL = "https://api.openbrewerydb.org/v1/breweries"

# Options are listed in a constant variable, making it easier for developers to add or remove user options.
USER_OPTIONS = (
    "Go through ALL breweries (are you bored?)",
    "list breweries by state",
    "list breweries by city",
    "list breweries by type",
    "View your scorebook",
    "Add an entry to your scorebook",
    "Exit GiveMeBrewery"
)

# Brewery types are also listed in a constant variable, making it easier for developers to add or remove brewery types.
BREWERY_TYPES = (
    "micro",
    "nano",
    "regional",
    "brewpub",
    "large",
    "planning",
    "bar",
    "contract",
    "proprietor",
    "closed"
)
