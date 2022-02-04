import csv

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pandas as pd

# def homepage(request):
#    return render(request, 'index.html', {})

'''
Read values from file
Construct HTML table?
Serve the data on a different endpoint
Fetch data at interval?
'''


# TODO display picture and maybe update dynamically?
# Add login
@login_required
def index(request):
    with open('static/data.csv') as csv_file:
        rows = []
        # data = csv_file.read()
        data = pd.read_csv(csv_file)
        dataframe = pd.DataFrame(data)
        mean_temp = dataframe['temp'].mean()
        mean_hum = dataframe['hum'].mean()
        mean_pres = dataframe['pres'].mean()

        round_temp = round(mean_temp, 1)
        round_hum = round(mean_hum, 1)
        round_pres = round(mean_pres, 1)

        #mean = dataframe[['temp', 'hum', 'pres']].mean()
        #new_dataframe = pd.DataFrame(mean)
        #data_html = new_dataframe.to_html()
        # data_html = dataframe.to_html()

        '''
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)
        '''
        context = {
            'temp': round_temp,
            'hum': round_hum,
            'pres': round_pres,
            #'data': data_html,
        }
        response = HttpResponse(data, content_type='text/plain')
        # return response
        return render(request, 'index.html', context)


def gallery(request):
    template_path = "templates/index.html"
    context = {
        "images": [
            "Dipp_project.drawio.png"
        ]
    }

    return render(request, template_path, context)

