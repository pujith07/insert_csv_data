from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
import csv

def insert_bank(request):

    a='//Users//pujithhc//django//rolex//datacsv//bank.csv'

    with open(a,'r') as file:
        csv_data=csv.reader(file)
        next(csv_data)
        for row in csv_data:
            bn=row[0].strip()
            instance=Bank(NAME=bn)
            instance.save()

        return HttpResponse('Data is inserted')

