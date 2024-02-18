from django.shortcuts import render
from uszipcode import SearchEngine
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from io import StringIO
from django.http import HttpResponse
import csv

def pull_radius_zips(f):
    radius_results = pd.DataFrame(columns = ['radius_zips', 'original_zips'])
    sr = SearchEngine()
    for j in range(0, len(f['zip_code'])):
        zip_info = sr.by_zipcode(str(f['zip_code'][j]))
        lat = zip_info.lat
        lng = zip_info.lng
        result = sr.by_coordinates(lat, lng, radius = 10, returns = 0)
        radius = []
        for i in result:
            radius.append(i.zipcode)
        radius = pd.DataFrame(radius)
        radius['original_zip'] = f['zip_code'][j]
        radius.columns = ['radius_zips', 'original_zips']
        radius_results = pd.concat([radius_results, radius], axis = 0)
    return radius_results

@csrf_exempt
def download(request):
    f = request.FILES.get('csvFile')
    f = f.read()
    f = f.decode('utf-8')
    f = pd.read_csv(StringIO(f))
    radius_results = pull_radius_zips(f)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="radius_zips.csv"'
    radius_results.to_csv(path_or_buf=response, index=False)
    return response

@csrf_exempt
# Create your views here.
def index(request):
    return render(request, "zip_app/index.html")
