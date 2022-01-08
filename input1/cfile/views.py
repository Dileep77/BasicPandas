from django.shortcuts import render
from django.http import HttpResponse


import csv
import pandas as pd
# Create your views here.
def takedata(request):
    return render(request,"get.html")

def resultfile(request):

    file1=request.GET['myfile']
    file2=request.GET['column']
    file3=request.GET['num']
    data=pd.read_csv(file1)
    a=file2
    b=file3
    c=int(b)+int(b)*5/100
    d=int(b)-int(b)*5/100

    mean1=data[a].mean()
    median1=data[a].median()


    #matchingdata=data.loc[data[a]==int(file3)]
    matchingdata=data[data[a]==int(file3)].to_string(index=False)


    rangedata=data.loc[data[a].between(d,c)].to_string(index=False)

    return render(request,"resultfile.html",{'mean1':mean1,'median1':median1,'matchingdata':matchingdata,'rangedata':rangedata})
