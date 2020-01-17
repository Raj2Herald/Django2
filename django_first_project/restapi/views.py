from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firstapp.models import Airport
import json

@csrf_exempt
def view_get_post_airport(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        airports = Airport.objects.all()
        print("QuerySet objects => ",airports)
        list_of_airports = list(airports.values("code","location"))
        print("List of Airport objects => ",list_of_airports)
        dictionary_name = {
        "airports":list_of_airports
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['code'])
        print(python_dictionary_object['location'])
        Airport.objects.create(code=python_dictionary_object['code'],location=python_dictionary_object['location'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        airport = Airport.objects.get(id = ID)
        print(type(airport.code))
        return JsonResponse({
            "id":airport.id,
            "code":airport.code,
            "location":airport.location
        })
    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })