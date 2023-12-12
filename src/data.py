from daftlistings import Daft
from daftlistings.enums import SearchType
from daftlistings.listing import Listing
import pandas as pd
from pprint import pprint


daft = Daft()

daft.set_location("Dublin City")
daft.set_search_type(SearchType.RESIDENTIAL_RENT)
daft.set_min_price(100)
daft.set_max_price(5000)


listings = daft.search()


def try_get_ber(listing: Listing):
    try:
        return listing.ber
    except:
        return None


def try_get_bedrooms(listing: Listing):
    try:
        return int(listing.bedrooms.split(" ")[0].split(",")[0])
    except:
        return None


def flatten_listing(listing: Listing):
    return {
        "bathrooms": int(listing.bathrooms.split(" ")[0].split(",")[0])
        if listing.bathrooms
        else None,
        "bedrooms": try_get_bedrooms(listing),
        "ber": try_get_ber(listing),
        "latitude": listing.latitude,
        "longitude": listing.longitude,
        "monthly_price": listing.monthly_price,
        "is_apartment": "Apartments" in listing.sections
        or "Apartment" in listing.sections,
    }


df = pd.DataFrame(map(flatten_listing, listings))
df.to_csv("./data.csv", index=False)
