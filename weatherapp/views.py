from django.shortcuts import render
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
# Create your views here.
def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=2af7e462108098f68ef5b6292ca57702').read()
        # source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '11a3c55dbe4cefad294710275920329f').read()

        list_of_data = json.loads(source)
        data={
            "city_name":str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']),
            "sunrise":str(list_of_data['sys']['sunrise']) ,
            "sunset":str(list_of_data['sys']['sunset']) ,
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        }
        print(data)
    else:
        data={}    
    return render(request,'index.html',data)    

