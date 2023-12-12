from daftlistings import Daft
from daftlistings.enums import SearchType
import pandas as pd

daft = Daft()

daft.set_location("Dublin City")

daft.set_search_type(SearchType.RESIDENTIAL_RENT)

daft.set_min_price(100)

daft.set_max_price(5000)

daft.set_min_beds(2)

daft.set_max_beds(2)

listings = daft.search()

df = pd.DataFrame(listings)

print(df)
