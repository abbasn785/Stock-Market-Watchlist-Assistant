"""MAIN MODULE TO RUN"""
from datetime import datetime
import stonk_functions as func

#gets the top sector for the week
sectorOG = func.get_sector()
sector = (sectorOG.replace(' ','')).lower()

#gets todays date
day = datetime.today().strftime('%A')
if day.lower() in ("saturday", "sunday"):
    day = "Friday"
today = datetime.now()
date = (f"{today.strftime('%B')} {today.day}")


"""Add Link for Criteria Here using https://finviz.com/screener.ashx"""
#the urls for stock criteria
win_sector = f"https://finviz.com/screener.ashx?v=111&f=sec_{sector},sh_avgvol_o1000,sh_price_o5,sh_relvol_o1.5,targetprice_above&ft=4"
rsi = "https://finviz.com/screener.ashx?v=211&f=sh_avgvol_o1000,sh_price_o5,ta_rsi_os30,ta_sma200_pa,targetprice_above&ft=4"

"""Add New Criteria Variable to urls Dict and assign a label"""
#dict of criteria urls and there label
urls = {win_sector: f"{sectorOG} Winners", rsi : "Oversold"}

#gets the stocks for each criteria and adds them to the stonks dict
stonks = func.get_stocks(urls)

#gets todays watchlist listing
main_str = func.get_main(day,stonks)

#gets current watchlist contents
with open("watchlist.txt", 'r') as file:
     contents = file.read()

#if its Monday, start a new watchlist
if day == 'Monday':
    with open("watchlist.txt", 'w') as file:
        file.write(main_str + '\n')

#if its not Monday, add todays stocks to the current watchlist
else:
    content_list = contents.split('\n\n')
    #remove the current days entry if its there to make space for updated entry
    with open("watchlist.txt", "w") as f:
        for i in content_list:
            if day not in i:
                f.write(f"{i}\n")
        f.truncate()

    #add todays entry
    with open("watchlist.txt", 'a') as file:
        file.write(main_str + '\n')


#gets weeks updated wathlist and prints it
with open("watchlist.txt", 'r') as file:
     contents = file.read()
print('Watchlist', date)

print(contents)




