"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# ebdjango/urls.py (example)
from django.contrib import admin
from django.urls import path
from main.views import home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
]
# The urlpatterns list is a list of URL patterns that Django uses to match the requested URL to the appropriate view.