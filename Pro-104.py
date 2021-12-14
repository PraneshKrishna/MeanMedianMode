from collections import Counter
import csv
#------------------

with open('HeightWeight.csv',newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)
#------------------

    file_data.pop(0)

#------------------

    new_data = []
for i in range(len(file_data)):
    m_num = file_data[i][2]
    new_data.append(float(m_num))

#------------------

n = len(new_data)
total = 0
for x in new_data:
    total += x

mean = total/n
print("mean or average of weight is: "+ str(mean))

#------------------

if n % 2 == 0:
    median1 = float(new_data[n // 2])
    median2 = float(new_data[n // 2-1])
    median = (median1 + median2)/2
else:
    median = new_data[n//2]
    print(n)

print("Median of weight is: "+str(median))

#------------------

data = Counter(new_data)
modeRange = {
"75-85":0,
"85-95":0,
"95-105":0,
"105-115":0,
"115-125":0,
"125-135":0,
"135-145":0,
"145-155":0,
"155-165":0,
"165-175":0,
}
for weight,occurence in data.items():
    if 75<weight<85:
        modeRange["75-85"]+= occurence
    elif 85<weight<95:
        modeRange["85-95"]+= occurence   
    elif 95<weight<105:
        modeRange["95-105"]+= occurence        
    elif 105<weight<115:
        modeRange["105-115"]+= occurence
    elif 115<weight<125:
        modeRange["115-125"]+= occurence
    elif 125<weight<135:
        modeRange["125-135"]+= occurence
    elif 135<weight<145:
        modeRange["135-145"]+= occurence
    elif 145<weight<155:
        modeRange["145-155"]+= occurence 
    elif 155<weight<165:
        modeRange["155-165"]+= occurence
    elif 165<weight<175:
        modeRange["165-175"]+= occurence

#mode_Range,mode_occurence = 0,0
#for range , occurence in modeRange.items:
