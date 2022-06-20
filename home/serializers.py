from rest_framework import serializers
from .models import Products , Order , OrderItem ,Recommended,Category , Counter

class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    category_products =  HomeSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','Name','category_products']
        
class RecommendedSerializers(serializers.ModelSerializer):
    product= serializers.CharField(source='product_name.Name')
    recomended_devices =  HomeSerializers(many=True, read_only=True,)
    class Meta:
        model = Recommended
        fields = ['id','product','recomended_devices']

        
class  jsonOrderItem(serializers.ModelSerializer):
    item= serializers.CharField(source='item.Name')
    class Meta:
        model = OrderItem
        fields = "__all__"
        
class  jsonOrder(serializers.ModelSerializer):
    # items= serializers.CharField(source=f"{OrderItem.quantity} of {OrderItem.item}")
    class Meta:
        model = Order
        fields = "__all__"      



class  jsonCounter(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = "__all__" 