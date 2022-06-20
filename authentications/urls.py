# from django.urls import path,include
# from . import views
# from rest_framework import routers

# r = routers.DefaultRouter()
# r.register('', views.CompanyRegistrationView)

# rr = routers.DefaultRouter()
# rr.register('', views.PersonRegistrationView)
# urlpatterns = [
#     path('registration/user/', include(rr.urls)),

#     # path('registration/user/', PersonRegistrationView.as_view(), name='register-user'),
#     # path('registration/company/', CompanyRegistrationView.as_view(), name='register-company'),
#     path('registration/company/', include(r.urls)),
#     # path('login/',LoginAPI.as_view(),name='login user')
# ]
from django.contrib import admin
from django.urls import path,include
from . import  views
from .views import ( CompanySignupView,
PersonSignupView,
CustomAuthToken, LogoutView)

#json urls
from rest_framework import routers


# Routers (json)
r1 = routers.DefaultRouter()
r1.register('', views.viewsUser)

r2 = routers.DefaultRouter()
r2.register('', views.viewsPerson)

r3 = routers.DefaultRouter()
r3.register('', views.viewsCompany)

urlpatterns = [
    path('signup/company/', CompanySignupView.as_view()),
    path('signup/user/', PersonSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),

    path('theuser/', include(r1.urls)),
    path('personRegister/', include(r2.urls)),
    path('companyRegister/', include(r3.urls)),

    
]