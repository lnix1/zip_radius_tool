from django.shortcuts import render
from uszipcode import SearchEngine
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

def pull_radius_zips(f):
    radius_results = pd.DataFrame(columns = ['radius_zips', 'original_zips'])
    sr = SearchEngine()
    for z in f['zip_codes']:
        zip_info = sr.by_zipcode(str(z))
        lat = zip_info.lat
        lng = zip_info.lng
        result = sr.by_coordinates(lat, lng, radius = 10, returns = 0)
        radius = []
        for i in result:
            radius.append(i.zipcode)
        radius = pd.DataFrame(radius)
        radius['original_zip'] = z
        radius.columns = ['radius_zips', 'original_zips']
        radius_results = pd.concat([radius_results, radius], axis = 0)
    return radius_results

@csrf_exempt
# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        f = request.FILES['csvFile']
        print(type(f))
        radius_results = pull_radius_zips(f)
        print('checking this works to this point')
    return render(request, "zip_app/index.html", context)
