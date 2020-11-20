


#import pandas
import pandas as pd


#create empty lists
id = []
ticker = []
amount = []

#read txt file, and append each row to pre-created lists
with open("text.txt", "r") as inp:
    for line in inp:
        ida, tickera, amounta = line.split()
        id.append(ida)
        ticker.append(tickera)
        amount.append(amounta)


#test to see "id" list output
id




#test to see "ticker" list output
ticker


#test to see "amount" list output
amount


#create blank dictionary and combine the 3 lists into a dictionary
file = {}

d = {'id':id,'ticker':ticker, 'amount': amount }


#test dictionary output
d

#convert the dictionary to pandas dataframe
df = pd.DataFrame.from_dict(d)


#test dataframe output
df

