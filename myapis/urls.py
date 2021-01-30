
from django.urls import path,include
from .views import CatViewset,PostViewset

from rest_framework import routers
router =routers.DefaultRouter()
router.register('cat',CatViewset)
router.register('posts',PostViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]