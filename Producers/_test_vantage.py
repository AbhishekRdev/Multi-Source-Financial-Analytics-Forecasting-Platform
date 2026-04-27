import requests
import os
from dotenv import load_dotenv

load_dotenv()

Al_token = os.getenv("ALPHA_VANTAGE_TOKEN") 
SYMBOL = "IBM"
ep_func = "TIME_SERIES_DAILY"
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function={ep_func}&symbol={SYMBOL}&apikey={Al_token}'
r = requests.get(url)
data = r.json()

print(data)

with open("H:/Az_e2e_fin_pipeline/Epic_1424/Producers/Alpha_out.json","w") as f:
    f.write(str(data))
