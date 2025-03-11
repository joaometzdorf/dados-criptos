import gspread
import requests

response = requests.get("https://api.coinpaprika.com/v1/coins/")
data = response.json()

gc = gspread.service_account()

sh = gc.open("Criptos")
sheet = sh.sheet1

rows = []

rows.append(["ID", "Name", "Symbol", "Rank", "Type"])

for crypto in data:
    crypto_id = crypto["id"]
    crypto_name = crypto["name"]
    symbol = crypto["symbol"]
    rank = crypto["rank"]
    crypto_type = crypto["type"]

    if rank != 0:
        rows.append([crypto_id, crypto_name, symbol, rank, crypto_type])

sheet.update(range_name="A1", values=rows)
print("Dados inseridos com sucesso!")
