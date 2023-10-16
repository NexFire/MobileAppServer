from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def postVratkaInfo(request):
    if(request.method=="POST"):
        data=json.loads(request.body)
        print(json.loads(request.body).keys())
        requiredKeys=["IdVratkaZbozi","Sklad","SkladPoznamka", "Foto"]
        if(len(data)==len(requiredKeys)):
            for a in data.keys():
                print("Key: ",a,", Value: ",data[a])
                if(requiredKeys.count(a)==0):
                    return HttpResponse(json.dumps("Incorrect POST body"),content_type="aplication/json")
            print("Data submited")
            return HttpResponse(json.dumps("Yes data submmited"),content_type="aplication/json")
        else:
            return HttpResponse(json.dumps("Incorrect amount of Multipart form arguments"),content_type="aplication/json")
    else:
        return HttpResponse(json.dumps("We need post method",content_type="aplicaiton/json"))



@csrf_exempt
def postPdf(request):
    if(request.method=="POST"):
        data=request.POST
        dataFile=request.FILES
        if(len(data)!=0 and len(dataFile)!=0):
            try:
                for a in data.keys():
                    print("Key: ",a,", Value: ",data[a])
                with open(data['fileName'],"wb") as file:
                    file.write(dataFile['file'].read())
                print("File written")
                return HttpResponse(json.dumps("File written"),content_type="application/json")
            except:
                return HttpResponse(json.dumps("Write File not correct"),content_type="application/json")
        else:
            return HttpResponse(json.dumps("No parameters"))
    else:
        return HttpResponse("No eat shit mother fucker")

def index(request):
    print(request.method)
    return HttpResponse("<h1>This is the server to send the data to</h1>")
# Create your views here.
