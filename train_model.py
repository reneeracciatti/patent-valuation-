
mport requests
import pandas as pd

# Fetch real USPTO assignment data
def fetch_uspto_data():
    url = "https://developer.uspto.gov/data/patent/assignment"
    response = requests.get(url)
    return pd.DataFrame(response.json()['results'])

# Load real data instead of sample CSV
df = fetch_uspto_data()

