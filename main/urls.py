from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [

    path('', HomeTasks.as_view(), name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='reg'),
    path('category/<int:category_id>/', TaskCategory.as_view(), name='categories'),
    path('category/', ByCategory.as_view(), name='category'),
    path('device/<int:device_id>/', DevicesList.as_view(), name='model'),
    path('single/<int:pk>/', product, name='product'),
    path('add/', AddProduct.as_view(),  name='add_product'),
    path('cart/', cart, name='cart'),
    path('remove/<int:pk>/', delete_cart, name='remove'),
    path('del/', delete_full_cart, name='del'),
    path('search/', Search.as_view(), name='search'),
    path('test/', test, name='test')




            ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
