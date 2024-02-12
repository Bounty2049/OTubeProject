from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.serializers import UserSerializer

from products.models import Library


class UserAPI(APIView):
    def get(self, request):
        user = User.objects.all()
        return Response({'users': UserSerializer(user, many=True).data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'users': serializer.data})

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'errors': 'Objects does not exist'})

        try:
            instance = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'errors': 'Object does not exist'})
        
        serializer = UserSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()

        return Response({'user': serializer.data})


@permission_classes([IsAuthenticated])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@permission_classes([IsAuthenticated])
def user_detail(request, pk):

    try:
        users = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        serializer = UserSerializer(users)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(users, data=data)
        if serializer.is_valid:
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        users.delete()
        return HttpResponse(status=204)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            form.messages.success(request, 'Congratulations, your successful registered')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'form': form, 
        'libraries': Library.objects.filter(user=request.user)
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
