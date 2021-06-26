import csv

with open ('HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)

#picking the weight data 
new_data = []
for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float (num))

new_data.sort()
n = len(new_data)
total = 0
for i in new_data:
    total = total + i

mean = total/n
print("Mean="+str(mean))