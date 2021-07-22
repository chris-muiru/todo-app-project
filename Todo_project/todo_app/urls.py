from django.urls import path
from . import views
urlpatterns = [
    path("index/",views.index,name="index_page"),
    path('del/<int:user_item>',views.remove,name='del')
]
