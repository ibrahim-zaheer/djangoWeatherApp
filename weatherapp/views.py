from django.shortcuts import render

import json 

import urllib.request 

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=dd411b0bf578a4258b4b94ebf0e5a2a5').read()
       

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

