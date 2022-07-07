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
# Create your views here



product_list = [
    { 'name': 'blue sofa',
        'room': 'living',
        'price':'1499',
        'color': ['blue'],
        'image': '../static/images/living_sofabl1.webp',
        'tags': ['sofa','couch','loveseat','blue','velvet','wood','living','living room','furniture',],
    },
    { 'name': 'brown sofa',
        'room': 'living',
        'price':'1499',
        'color': ['brown'],
        'image': '../static/images/living_sofabr1.webp',
        'tags': ['sofa','couch','loveseat','brown','leather','wood','living','living room','furniture',],
    },
    { 'name': 'lamp',
        'room': 'living',
        'price':'199',
        'color': ['gold, white'],
        'image': '../static/images/living_lamp1.webp',
        'tags': ['lamp','floor','floor lamp','gold','brass','white','light','lighting','fixture',],
    },
        { 'name': 'headboard',
        'room': 'bedroom',
        'price':'299',
        'color': ['brown'],
        'image': '../static/images/bedroom_headboard1.jpeg',
        'tags': ['headboard','wood','live edge','queen','king','rustic','industrial','bed'],
    },
        { 'name': 'doors',
        'room': 'bedroom',
        'price':'399',
        'color': ['black'],
        'image': '../static/images/bedroom_doors1.webp',
        'tags': ['mirror','wardrobe','metal','black','sliding','barndoor','barn','door','panel',],
    },
        { 'name': 'desk',
        'room': 'bedroom',
        'price':'99',
        'color': ['brown', 'black'],
        'image': '../static/images/bedroom_desk1.jpeg',
        'tags': ['desk','wood','metal','brown','black','dropleaf','folding','collapsible','industrial',],
    },
        { 'name': 'faucet1',
        'room': 'bathroom',
        'price':'299',
        'color': ['black'],
        'image': '../static/images/bathroom_faucet1.jpeg',
        'tags': ['bathroom','faucet','shelf','unique','wall','modern','sink',],
    },
        { 'name': 'tile',
        'room': 'bathroom',
        'price':'299',
        'color': ['white', 'black'],
        'image': '../static/images/bathroom_tile1.jpeg',
        'tags': ['tile','art deco','black','white','stripes','hexagon','modern','bathroom','kitchen',],
    },
        { 'name': 'sink',
        'room': 'bathroom',
        'price':'149',
        'color': ['white'],
        'image': '../static/images/bathroom_sink1.jpeg',
        'tags': ['white','art deco', 'unique','sink','vanity','porcelain',],
    },
        { 'name': 'faucet2',
        'room': 'kitchen',
        'price':'299',
        'color': ['black', 'gold'],
        'image': '../static/images/kitchen_faucet1.jpeg',
        'tags': ['kitchen','faucet','black','gold','brass','flexible','multi-stream','coil',],
    },
        { 'name': 'paint',
        'room': 'kitchen',
        'price':'99',
        'color': ['blue'],
        'image': '../static/images/kitchen_paint1.png',
        'tags': ['blue','paint','cabinet','cabinets','kitchen',],
    },
        { 'name': 'sink2',
        'room': 'kitchen',
        'price':'299',
        'color': ['black'],
        'image': '../static/images/kitchen_sink1.jpeg',
        'tags': ['kitchen','sink','stainless','steel','stainless steel','graphite','black','undermount','farmhouse',],
    },
]


shopping_cart = [
    { 'name': 'blue sofa',
        'room': 'living',
        'price':'1499',
        'color': ['blue'],
        'image': '../static/images/living_sofabl1.webp',
        'tags': ['sofa','couch','loveseat','blue','velvet','wood','living','living room','furniture',],
    },
    { 'name': 'sink',
        'room': 'bathroom',
        'price':'149',
        'color': ['white'],
        'image': '../static/images/bathroom_sink1.jpeg',
        'tags': ['white','art deco', 'unique','sink','vanity','porcelain',],
    },
]

cart_total = 15
cart_total_str = str(cart_total)



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
    data = { 'product_list': product_list }
    return render(request, 'pages/search.html', data)

def kitchen(request):
    print(HttpResponse("Kitchen page: Show pics of kitchen furniture and accessories."))
    data = { 'product_list': product_list }
    return render(request, "pages/kitchen.html", data)

def bathroom(request):
    print(HttpResponse("Bathroom page: Show pics of bathroom fixtures."))
    data = { 'product_list': product_list }
    return render(request, "pages/bathroom.html", data)

def bedroom(request):
    print(HttpResponse("Bedroom page: Show pics of bedroom furniture and accessories."))
    data = { 'product_list': product_list }
    return render(request, "pages/bedroom.html", data)

def living(request):
    print(HttpResponse("Living Room page: Show pics of living room furniture and accessories."))
    data = { 'product_list': product_list }
    return render(request, "pages/living.html", data)

def my_cart(request):
    print(HttpResponse("Living Room page: Show pics of living room furniture and accessories."))
    data = { 'shopping_cart': shopping_cart }
    return render(request, "pages/my_cart.html", data)

def about_us(request):
    print(HttpResponse("About Us: Our Mission to Help You Get the Look!"))
    return render(request, 'pages/about_us.html')