from rest_framework.authtoken import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RegistrationViewsets,LogoutView


router=DefaultRouter()
router.register('', RegistrationViewsets,basename='register')
urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('logout/',LogoutView.as_view()),
    path('register/',include(router.urls)),
]