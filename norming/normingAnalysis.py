"""

"""

#Install all the things
import pandas as pd
import csv

data = pd.read_csv('data.csv')

#set up for writing csv
header = ['Item Number','Arousal', 'Valence', 'Complexity', 'Pair Number', 'Relatedness']
result = []
item_number = 1
relatedness = []
pair_number = 1

df = pd.DataFrame(data)

avg = df.mean(axis = 0)

new_df = pd.DataFrame(df.mean())

#record rows of csv data. Ranges are counted manually and need to change if the number of items in original csv changes

for x in range(264,305,1):
    relatedness.append(f'{new_df.iat[x,0]}')

for x in range(0,263,3):
    if item_number < len(relatedness) + 1:
        result.append([f'{item_number}', f'{new_df.iat[x,0]}', f'{new_df.iat[x+1,0]}', f'{new_df.iat[x+2,0]}', f'{pair_number}', relatedness[item_number - 1]])
    else:
        result.append([f'{item_number}', f'{new_df.iat[x,0]}', f'{new_df.iat[x+1,0]}', f'{new_df.iat[x+2,0]}'])
    item_number += 1
    pair_number += 1

#set path for the csv file
with open('analysisResult.csv', 'w') as f:
#with open('C:\\Users\\Ellyn\\Desktop\\Python-Image-Analysis\\img analysis py\\analysisResult.csv', 'w') as f:
    writer = csv.writer(f) #create the csv writer

    writer.writerow(header) #write the header

    writer.writerows(result) #write all rows of data

    print('data saved to path')