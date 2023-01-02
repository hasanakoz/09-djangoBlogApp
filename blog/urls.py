from django.urls import path, include
from rest_framework import routers
from .views import CategoryView

router = routers.DefaultRouter()
router.register('category', CategoryView)


urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns += router.urls
