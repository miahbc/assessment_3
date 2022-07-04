from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests
from requests_oauthlib import OAuth1
import json
from dotenv import load_dotenv
import os

load_dotenv()
print('Hello World!!!!')
print(os.environ['apikey'])
print(os.environ['secretkey'])
# print(os.environ)
# Create your views here.



product_list = [
    { 'name': 'sofa',
        'room': 'living',
        'price':'1499',
        'color': ['blue', 'brown'],
        'image': ['ecommerce_project/static/images/living_sofabl1.webp'],
    },
    { 'name': 'lamp',
        'room': 'living',
        'price':'199',
        'color': ['gold, white'],
        'image': ['ecommerce_project/static/images/living_lamp1.webp'],
    },
        { 'name': 'headboard',
        'room': 'bedroom',
        'price':'299',
        'color': ['brown'],
        'image': ['ecommerce_project/static/images/bedroom_headboard1.jpeg'],
    },
        { 'name': 'doors',
        'room': 'bedroom',
        'price':'399',
        'color': ['black'],
        'image': ['ecommerce_project/static/images/bedroom_doors1.webp'],
    },
        { 'name': 'desk',
        'room': 'bedroom',
        'price':'99',
        'color': ['brown', 'black'],
        'image': ['ecommerce_project/static/images/bedroom_desk1.jpeg'],
    },
        { 'name': 'faucet1',
        'room': 'bathroom',
        'price':'299',
        'color': ['black'],
        'image': ['ecommerce_project/static/images/bathroom_faucet1.jpeg'],
    },
        { 'name': 'tile',
        'room': 'bathroom',
        'price':'299',
        'color': ['white', 'black'],
    },
        { 'name': 'sink',
        'room': 'bathroom',
        'price':'149',
        'color': ['white'],
        'image': ['ecommerce_project/static/images/bathroom_sink1.jpeg'],
    },
        { 'name': 'faucet2',
        'room': 'kitchen',
        'price':'299',
        'color': ['black', 'gold'],
        'image': ['ecommerce_project/static/images/kitchen_faucet1.jpeg'],
    },
        { 'name': 'paint',
        'room': 'kitchen',
        'price':'99',
        'color': ['blue'],
        'image': ['ecommerce_project/static/images/kitchen_paint1.png'],
    },
        { 'name': 'sink2',
        'room': 'kitchen',
        'price':'299',
        'color': ['black'],
        'image': ['ecommerce_project/static/images/kitchen_sink1.jpeg'],
    },
]



def index(request):
    # query the database to get the question_list
    # the keys on our data object can be accessed from the template
    response = render(request, 'pages/index.html')
    return response

def products(request):

    # GET requests can't have a body. We have to look for the data in the URL. 
    print(request.GET.get('query'))
    query = request.GET.get('query')

    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
    endpoint = f"http://api.thenounproject.com/icon/{query}"

    API_response = requests.get(endpoint, auth=auth)
    print(API_response.content)
    JSON_API_response = json.loads(API_response.content)
    image_url = JSON_API_response['icon']['preview_url']
    return JsonResponse({'url': image_url })

def search(request):
    print(HttpResponse("Search page: find furniture and accessories."))
    return render(request, 'pages/search.html')

def kitchen(request):
    print(HttpResponse("Kitchen page: Show pics of kitchen furniture and accessories."))
    return render(request, "pages/kitchen.html")

def bathroom(request):
    print(HttpResponse("Bathroom page: Show pics of bathroom fixtures."))
    data = { 'product_list': product_list }
    return render(request, "pages/bathroom.html", data)

def bedroom(request):
    print(HttpResponse("Bedroom page: Show pics of bedroom furniture and accessories."))
    return render(request, "pages/bedroom.html")

def living(request):
    print(HttpResponse("Living Room page: Show pics of living room furniture and accessories."))
    return render(request, "pages/living.html")