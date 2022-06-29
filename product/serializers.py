from rest_framework import serializers
from .models import *


class BottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottles
        fields = '__all__'




    # def to_representation(self, obj):
    #     image = None
    #     if obj.image and hasattr(obj.image, 'url'):
    #         url = obj.image.url
    #         request = self.context.get('request', None)
    #         if request is not None:
    #             image = request.build_absolute_uri(url)
    #
    #     return {
    #         "id": obj.id,
    #         "name": obj.name,
    #         "volume": obj.volume,
    #         "width": obj.width,
    #         "height": obj.height,
    #         "material": obj.material,
    #         "weight": obj.weight,
    #         "image": image,
    #         "price": obj.price,
    #         "created": obj.created,
    #         "count": "1",
    #         "category": {
    #             "name": obj.category.name,
    #             "id": obj.category.id
    #         } if obj.category else None
    #     }


class CategorySerializer(serializers.ModelSerializer):
    flakons = BottleSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # def to_representation(self, obj):
    #     if not obj:
    #         return None
    #     return {
    #         "id": obj.id,
    #         "total": obj.total,
    #         "phone": obj.phone,
    #         "address": obj.address,
    #         "created": obj.created,
    #         "bottle": {
    #             "name_uz": obj.bottle.name_uz,
    #             "name_en": obj.bottle.name_en,
    #             "name_ru": obj.bottle.name_ru,
    #             "id": obj.bottle.id
    #          }
    #     }
