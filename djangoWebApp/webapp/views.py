import csv

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
# Add login page
def index(request):
    with open('static/data.csv') as csv_file:
        rows = []
        # data = csv_file.read()
        data = pd.read_csv(csv_file)
        dataframe = pd.DataFrame(data)
        mean = dataframe[['temp', 'hum', 'pres']].mean(axis=0)
        new_dataframe = pd.DataFrame(mean)
        data_html = new_dataframe.to_html()
        # data_html = dataframe.to_html()

        '''
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)
        '''
        context = {
            'data': data_html,
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

