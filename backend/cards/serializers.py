from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields ='__all__'

# class CarSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Car
# 		fields ='__all__'

# class DoorSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Door
# 		fields ='__all__'