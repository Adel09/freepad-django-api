from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth import login, authenticate
from .models import Profile, PadRequest, Donation
from django.db import IntegrityError
import traceback
from .serializers import RequestSerializer


# Create your views here.
@api_view(['post'])
@csrf_exempt
def register(request):
    first_name = request.data['first_name']
    username = request.data['email']
    email = request.data['email']
    password = request.data['password']
    try:
        user = User.objects.create_user(
            first_name=first_name,
            last_name = request.data['last_name'],
            email=email,
            username = username,
            password=password
        )
        user.save()
        profile = Profile.objects.create(
            owner=user,
            category=request.data['category'],
            phone = request.data['phone'],
            city = request.data['city'],
            state=request.data['state'],
            pharmacy = request.data['pharmacy']
        )
        profile.save()
        token = Token.objects.create(user=user)
        login(request, user)
        res = {
            'status' : 200,
            'message' : 'User created successfully',
            'data' : {
                'token' : token.key
            }
        }
        return JsonResponse(res, status=200, safe=False)
    except:
        traceback.print_exc()
        res = {
            'status' : 500,
            'message' : 'failed'
        }
        return JsonResponse(res, status=500, safe=False)



@api_view(['get'])
def getProfile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(owner=request.user)
        if profile.category == "DONOR":
            res = {
                "status" : 200,
                "message" : "success",
                "data" : {
                    "name" : f'{user.first_name} {user.last_name}',
                    "email" : user.email,
                    "category" : profile.category,
                    "image" : profile.image.url,
                    "wallet" : profile.wallet,
                    "people_helped" : profile.people_helped,
                    "city" : profile.city,
                    "state" : profile.state
                }
            }
            return JsonResponse(res, status=200, safe=False)
        elif profile.category == "RECIPIENT":
            res = {
                "status" : 200,
                "message" : "success",
                "data" : {
                    "name" : f'{user.first_name} {user.last_name}',
                    "email" : user.email,
                    "category" : profile.category,
                    "image" : profile.image.url,
                    "pharmacy" : profile.pharmacy,
                    "city" : profile.city,
                    "state" : profile.state
                }
            }
            return JsonResponse(res, status=200, safe=False)
        else:
            res = {
                "code" : 404,
                "message" : "Category not found"
            }
            return JsonResponse(res, status=404, safe=False)
    else:
        res = {
            'status' : 401,
            'message' : 'Unauthenticated'
        }
        return JsonResponse(res, status=401, safe=False)

@api_view(['GET'])
def getRequests(request):
    if request.user.is_authenticated:
        user = request.user
        requests = PadRequest.objects.filter(completed=False)
        serializer = RequestSerializer(requests, many=True)
        res = {
            "status" : 200,
            "message" : "success",
            "data" : serializer.data
        }
        return JsonResponse(res, safe=False, status=200)
    else:
        res = {
            'status' : 401,
            'message' : 'Unauthenticated'
        }
        return JsonResponse(res, status=401, safe=False)

@api_view(['post'])
@csrf_exempt
def loginuser(request):
    username = request.data['email']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    profile = Profile.objects.get(owner=user)
    category = profile.category
    token = Token.objects.get(user=user)
    if user is not None:
        login(request, user)
        res = {
            "status" : 200,
            "message" : "Login successful",
            "category" : category,
            "data" : {
                "token" : token.key
            }
        }
        return JsonResponse(res, safe=False, status=200)
    else:
        res = {
            "status" : 401,
            "message" : "Incorrect credentials"
        }
        return JsonResponse(res, safe=False, status=401)

@api_view(['GET'])
def donate(request, id):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(owner=user)
        if profile.category == 'DONOR':
            padrequest = PadRequest.objects.get(id=id)
            donation = Donation.objects.create(
                donated_by=user,
                donated_to=padrequest
            )
            donation.save()
            res = {
                "status" : 200,
                "message" : "success",
                "thanks" : "Thank you for your donation"
            }
            return JsonResponse(res, safe=False, status=200) 
        else:
            res = {
                "status" : 400,
                "message" : "Only Donors can donate!"
            }
            return JsonResponse(res, safe=False, status=400) 




@api_view(['post'])
@csrf_exempt
def createRequest(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(owner=user)
        padrequest = PadRequest.objects.create(
            owner=user,
            name= f'{user.first_name} {user.last_name}',
            title=f'Help {user.first_name} in {profile.city}',
            city = profile.city,
            state = profile.state,
            pharmacy = profile.pharmacy,
            image = profile.image.url
        )
        padrequest.save()
        res = {
            "status" : 200,
            "message" : "success"
        }
        return JsonResponse(res, safe=False, status=200)
    else:
        res = {
            'status' : 401,
            'message' : 'Unauthenticated'
        }
        return JsonResponse(res, status=401, safe=False)

