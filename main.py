import requests as r
import json
from prettytable import PrettyTable

url = 'https://api.compound.finance/api/v2/ctoken'
payload = '{ "addresses": [] "block_timestamp":}'
response = r.post(url,data=payload)
market = json.loads(response.content)['cToken']
#print(market)
comp_table = PrettyTable(['Token','Lend','Borrow'])
for m in market:
  comp_table.add_row([m['underlying_name'],
  float(m['supply_rate']['value']),
  float(m['borrow_rate']['value'])])
print(comp_table)


