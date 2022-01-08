import csv
import sys
import pandas as pd

inFile=sys.argv[1]

data=pd.read_csv(inFile)
#with open(inFile, 'r') as file:
#    reader =csv.reader(file)
#    for row in reader:
#        print(row)
a=input("enter column name ")
b=str(input("enter matching records by input"))
c=int(b)+int(b)*5/100
d=int(b)-int(b)*5/100

print(data[a].mean())
print(data[a].median())
x=data.loc[data[a]==int(b)].to_string(index=False)

y=data.loc[data[a].between(d,c)].to_string(index=False)


print("data with input in given column",x)

print("data in 5% range ",y)
