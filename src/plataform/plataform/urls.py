"""
URL configuration for plataform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from common.views import HomeView, LogsView, NumbersView, ItemsView, LogAPI, AuthorizedNumberAPI, ItemAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomeView.as_view(), name='index'),
    path('logs/', LogsView.as_view(), name='logs'),
    path('numbers/', NumbersView.as_view(), name='numbers'),
    path('items/', ItemsView.as_view(), name='items'),

    path('api/logs/create/', LogAPI.create_log, name='create_log'),
    path('api/logs/status/', LogAPI.update_status, name='update_status'),
    path('api/logs/csv/', LogAPI.get_csv_file, name='get_csv_file'),
    path('api/logs/delete/', LogAPI.delete_log, name='delete_log'),

    path('api/number/create/', AuthorizedNumberAPI.create_autorized_number, name='create_autorized_number'),
    path('api/number/get/', AuthorizedNumberAPI.get_all_autorized_number, name='get_all_autorized_number'),
    path('api/number/delete/', AuthorizedNumberAPI.delete_autorized_number, name='delete_autorized_number'),

    path('api/item/create/', ItemAPI.create_item, name='create_item'),
    path('api/item/get/', ItemAPI.get_all_item, name='get_all_item'),
    path('api/item/delete/', ItemAPI.delete_item, name='delete_item'),
]
