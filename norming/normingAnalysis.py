"""
This is a script used ro quickly organize the result csv from the qualtrics norming survey.
Before running this script, open the data csv and delete all the extra information, 
which includes the rows with incomplete data, and ALL the columns that are NOT a part of item arousal, valence,
complexity, and pair relatedness.

"""

#Install libraries
import pandas as pd
import csv

#read the data csv
data = pd.read_csv('data.csv')

#set up columns for writing csv
header = ['Item Number','Arousal', 'Valence', 'Complexity', 'Pleasantness', 'Pair Number', 'Relatedness']
result = []
item_number = 1
relatedness = []
pair_number = 1

#make pandas dataframe from data
df = pd.DataFrame(data)

#make new dataframe of each column's mean
new_df = pd.DataFrame(df.mean())

#record rows of csv data. Ranges are counted manually and need to change if the number of items in original csv changes
#in this case, the pair 1 data is on row index 264
for x in range(356,397,1):
    relatedness.append(f'{new_df.iat[x,0]}') #add all pair relatedness to an array

for x in range(0,355,4):
    #store the data in the correct format
    if item_number < len(relatedness) + 1:
        result.append([f'{item_number}', f'{new_df.iat[x,0]}', f'{new_df.iat[x+1,0]}', f'{new_df.iat[x+2,0]}', f'{new_df.iat[x+3,0]}', f'{pair_number}', relatedness[item_number - 1]])
    else:
        result.append([f'{item_number}', f'{new_df.iat[x,0]}', f'{new_df.iat[x+1,0]}', f'{new_df.iat[x+2,0]}', f'{new_df.iat[x+3,0]}'])
    item_number += 1
    pair_number += 1

#set path for the csv file
with open('analysisResult.csv', 'w') as f:
    writer = csv.writer(f) #create the csv writer

    writer.writerow(header) #write the header

    writer.writerows(result) #write all rows of data

    print('data saved to path')