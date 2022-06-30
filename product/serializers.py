from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class BottleSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Bottles
        fields = '__all__'

    def to_representation(self, obj):
        serializer = ImageSerializer(obj.images, many=True)
        datas = serializer.data
        lst = []
        for data in datas:
            url = data['image']
            request = self.context.get('request', None)
            if request is not None:
                url = request.build_absolute_uri(url)
                lst.append(url)

        return {
            "id": obj.id,
            "name": obj.name,
            "volume": obj.volume,
            "width": obj.width,
            "height": obj.height,
            "weight": obj.weight,
            "images": lst,
            "price": obj.price,
            # "created": obj.created,
            "count": "1",
            "neck_diameter": obj.neck_diameter,
            "length": obj.length,
            "min_order": obj.min_order,
            "category": {
                "name": obj.category.name,
                "id": obj.category.id
            } if obj.category else None,
            "field": {
                "name": obj.field.name,
                "id": obj.field.id
            } if obj.field else None
        }


class CategorySerializer(serializers.ModelSerializer):
    flakons = BottleSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class FieldCategorySerializer(serializers.ModelSerializer):
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
