"""consultancy_busines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin


from consultancy_busines import views as consultancy_busines_views
# from contact_us import views as contact_us_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', consultancy_busines_views.home, name='home'),
    url(r'^support_services/$', consultancy_busines_views.support_services, name='support_services'),
    url(r'^maintenance/$', consultancy_busines_views.maintenance, name='maintenance'),
    url(r'^ceo/$', consultancy_busines_views.ceo, name='ceo'),
    url(r'^deputy_ceo/$', consultancy_busines_views.deputy_ceo, name='deputy_ceo'),
]
