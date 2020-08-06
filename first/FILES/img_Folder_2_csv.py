import pandas as pd
import time
from PIL import Image
import os,array

os.chdir("E://Telugu Character Recogniton//Resized_Vowel_Dataset")

columnNames = list()

for i in range(784):
    pixel = 'pixel'
    pixel += str(i)
    columnNames.append(pixel)
columnNames.append('Class')

train_data = pd.DataFrame(columns = columnNames)

start_time = time.time()
for i in range(1,1200):
    t = i
    img_name = str(t)+'.jpg'
    img = Image.open(img_name)
    rawData = img.load()
        #print rawData
    data = []
    for y in range(28):
        for x in range(28):
            data.append(rawData[x,y][0])

    k = 0
        #print data
    data_with_class=[data[k] for k in range(784)]
    if i>1 and i<=200:
        data_with_class.append(1)
    if i>201 and i<=400:
        data_with_class.append(2)
    if i>401 and i<=600:
        data_with_class.append(3)
    if i>601 and i<=800:
        data_with_class.append(4)
    if i>801 and i<=1000:
        data_with_class.append(5)
    if i>1001 and i<=1200:
        data_with_class.append(6)

        
    train_data.loc[i] = data_with_class



train_data.to_csv("E://Telugu Character Recogniton//CSV_datasetsix_vowel_dataset.csv",index = False)

print( "Done", time.time()-start_time)
