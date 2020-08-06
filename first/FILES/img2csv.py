import os,png,array
import pandas as pd

os.chdir('Analytics_vidya/Train/Images/test')
import time

from PIL import Image
columnNames = list()

for i in range(784):
    pixel = 'pixel'
    pixel += str(i)
    columnNames.append(pixel)

train_data = pd.DataFrame(columns = columnNames)
start_time = time.time()
for i in range(1,49000):
    t = i
    img_name = str(t)+'.png'
    img = Image.open(img_name)
    rawData = img.load()
        #print rawData
    data = []
    for y in range(28):
        for x in range(28):
            data.append(rawData[x,y][0])
    print i
    k = 0
        #print data
    train_data.loc[i] = [data[k] for k in range(784)]



train_data.to_csv("train_converted.csv",index = False)

print( "Done", time.time()-start_time)
