from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Comment, FavMusic, Product, Song, Movie
from django.core.paginator import Paginator
import json



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




def comment_endpoint(request):
    if request.method =="POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"try again later :b"}, status=400)

        text = data.get("text")
        comment = Comment.objects.create(text=text)

        return JsonResponse({"msg":"record created"},status = 201)
    else:
        return JsonResponse({"msg":"try again later :b"}, status=405)

def retrieve_comment(request, id):
    if request.method =="GET":
        try:
            comment = Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            return JsonResponse({"msg":"try again later :b"}, status=404)
        dict = {
            "id" : comment.id,
            "text" : comment.text,
        }
        return JsonResponse(dict, status=200)
    elif request.method == "DELETE":
        comment.delete()
        return JsonResponse({},status = 204)
    else:
        return JsonResponse({"msg":"try again later :b"}, status=405)

def retrieve_product(request, id):
    if request.method =="GET":
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return JsonResponse({"msg":"try again later :b"}, status=404)
        dict = {
            "id" : product.id,
            "price" : product.price,
            "name" : product.name,
            "currency" : product.currency,
        }
        return JsonResponse(dict, status=200)
    else:
        return JsonResponse({"msg":"try again later :b"}, status=405)



def create_favsongs_endpoint(request):
    if request.method =="POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"try again later :b"}, status=400)

        artist = data.get("artist")
        title = data.get("title")

        FavMusic.objects.create(artist=artist, title=title)

        return JsonResponse({"msg":"record created"},status = 201)
    else:
        return JsonResponse({"msg":"try again later :b"}, status=405)

def rud_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"msg":"try again later :b"}, status=404)

    if request.method == "GET":
        dict = {
        "price" : product.price,
        "name" : product.name,
        "currency" : product.currency,
        }
        return JsonResponse(dict)
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"try again later :b"}, status=400)

        price = data.get("price")
        name = data.get("name")
        currency = data.get("currency")

        product.price = price
        product.name = name
        product.currency = currency

        product.save()
        return JsonResponse({
        "msg":"record updated :D"
        }, status=200)

    elif request.method == "DELETE":
        product.delete()
        return JsonResponse({},status = 204)


    else:
        return JsonResponse({"msg":"try again later :b"}, status=405)




def product_api_call(request):
    if request.method =="POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"try again later"}, status=400)

        price = data.get("price")
        name = data.get("name")
        currency = data.get("currency")

        product = Product.objects.create(price=price, name=name, currency=currency)

        return JsonResponse({"msg":"record created  " + str(product.id)},status = 201)
    elif request.method == "GET":
        products = Product.objects.all()

        results = []
        for product in products:
            record = {
            "price" : product.price,
            "name" : product.name,
            "currency" : product.currency,
            "id" : product.id,
            }
            results.append(record)
        return JsonResponse({
            "result": results,
            })
    else:
        return JsonResponse({"msg":"try again later :b"}, status=405)

def song_api_call(request):
    if request.method =="POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"try again later"}, status=400)

        title = data.get("title")
        artist = data.get("artist")
        year = data.get("year")


        song = Song.objects.create(title=title, artist=artist, year=year)

        return JsonResponse({"msg":"Song saved succesfully  "+ str(song.id)}, status = 201)
    elif request.method =="GET":
        songs = Song.objects.all()

        paginator = Paginator(songs, 3)
        page_numb = request.GET.get("page")
        song_obj = paginator.get_page(page_numb)

        x = []
        for m in song_obj:
            y = {
            "title": m.title,
            "artist": m.artist,
            "year": m.year,
            }
        x.append(y)
        return JsonResponse({"results": x}, status=405)
    else:
        return JsonResponse({"msg":"try again later :b"}, status=405)

def movie_api_call(request):
    if request.method =="POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"try again later"}, status=400)
        name = data.get("name")
        studio = data.get("studio")
        release = data.get("release")

        movie = Movie.objects.create(name=name, studio=studio, release=release)

        return JsonResponse({"msg":"movie succesfully saved.  "+ str(movie.id)}, status = 201)
    elif request.method =="GET":
        movies = Movie.objects.all()

        results = []
        for m in movies:
            record ={
            "name" : m.name,
            "studio" : m.studio,
            "release" : m.release,
            }
            results.append(record)
        return JsonResponse({
        "results": results,
        })
    else:
        return JsonResponse({"msg":"try again later :b"}, status=405)
