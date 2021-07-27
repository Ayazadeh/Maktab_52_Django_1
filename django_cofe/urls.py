from django.contrib import admin
from django.urls import path

from views import HomePage
from menu_items.views import create_menu_item
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('test/', create_menu_item)
]
