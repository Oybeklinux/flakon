from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register("bottles", BottleViewSet)
router.register("categories", CategoryViewSet)
router.register("settings", SettingsViewSet)
# router.register("orders", OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
]
