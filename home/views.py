from .models import Products ,Category,OrderItem , Order ,Recommended, Counter
from .serializers import HomeSerializers,CategorySerializers  ,RecommendedSerializers ,jsonOrder,jsonOrderItem,jsonCounter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from collections import Counter
from django.db.models import F
# from authentications.models import User



# @api_view(['Post','GET'])
# def Home_listAPI(request):
#     all_ads=Products.objects.all()
#     permission_classes = [permissions.IsAdminUser]
#     return Response(HomeSerializers(all_ads,many=True).data)


@api_view(['GET','Post'])
def Recommended_listAPI(request):
    all_ads=Recommended.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    return Response(RecommendedSerializers(all_ads,many=True).data)

class product(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = HomeSerializers
    

@api_view(['GET','Post'])
def Category_listAPI(request):
    all_ads=Category.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    return Response(CategorySerializers(all_ads,many=True).data)
    
class orderitem(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = jsonOrderItem


class order(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = jsonOrder



def count(self, **kwargs):

    survey_counter = Counter.objects.get_or_create(survey_wizard_type= 'survey_wizard_one')[0] # x can be any value from one to nine
    survey_counter.survey_wizard_count = F('survey_wizard_count') + 1 
    survey_counter.save()

    return Response(survey_counter(survey_counter,many=True).data)


    

    
    
