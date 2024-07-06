from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('bucket/' , views.BucketHome.as_view(), name='bucket'), #it should be upper than slug of product , cause django things that we sent slug for the slug url (if we write the bucket down the slug path)
    path('delete_obj_bucket/<key>' , views.DeleteBucketObject.as_view(), name='delete_obj_bucket'),
    path('<slug:slug>/' , views.ProductDetailView.as_view(), name='product_detail'),

]