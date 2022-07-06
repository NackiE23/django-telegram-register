from django.contrib.auth import get_user_model, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

User = get_user_model()


# --  VIEWS -- #
def index(request):
    context = {
        'title': 'Index'
    }
    return render(request, 'control/index.html', context=context)


def profile(request, user_pk):
    context = {
        'title': f'Profile {request.user.name}'
    }
    return render(request, 'control/profile.html', context=context)


class LoginUser(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'control/login.html'
    extra_context = {'title': 'Login'}

    def get_success_url(self):
        return reverse('profile', kwargs={'user_pk': self.request.user.pk})


def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse("login"))


# --  SERIALIZER -- #
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'email', 'password', 'username', 'name', 'user_id']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            password=make_password(validated_data['password'])
        )
        user.name = validated_data['name']
        user.username = validated_data['username']
        user.user_id = validated_data['user_id']
        user.save()

        return user


# --  API -- #
class UserAPICreate(APIView):
    def get(self, request):
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True).data
        return Response(serialized_users)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
