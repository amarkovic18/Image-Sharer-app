from django.urls import path
from .views import HomePage, AddDetail, FormPage

app_name='myapp'
urlpatterns=[
    path('', HomePage.as_view(), name="home"),
    path('detail/<int:pk>', AddDetail.as_view(), name="detail"),
    path('post', FormPage.as_view(), name='post'),
   
]