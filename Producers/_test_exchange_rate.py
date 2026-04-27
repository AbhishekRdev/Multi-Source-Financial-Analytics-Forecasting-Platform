import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

ex_token = os.getenv("EXCHANGE_RATE")
currency = "USD"
url = f'https://v6.exchangerate-api.com/v6/{ex_token}/latest/{currency}'
# print(url)
response = requests.get(url)
data = response.json()

print(data)

with open("H:/Az_e2e_fin_pipeline/Epic_1424/Producers/exchange_out.json",'w') as f:
    f.write(str(data))
