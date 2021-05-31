from nsetools import Nse
from pprint import pprint # just for neatness of display
import json
nse = Nse()

#get detail of particular stock
q = nse.get_quote('TATAMOTORS') # it's ok to use both upper or lower case for codes.
# pprint(q["basePrice"])

#list all stocks
all_stock_codes = nse.get_stock_codes()
# pprint(all_stock_codes["INFY"])
# for x in all_stock_codes.keys():
#   print(x)

all_stock_codes = nse.get_stock_codes()
hi=[]
for x in  all_stock_codes.keys():
    hi.append(x)


for i in range(1,100):
    q = nse.get_quote(hi[i])
    print(hi[i] +" : "+ str(q["basePrice"]))