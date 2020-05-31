from django.conf.urls import url, include
from django.contrib import admin
from commissions.views import home
from accounts import urls as accounts_urls
from commissions import urls as commissions_urls
from checkout import urls as checkout_urls

"""
********************************************************************

ORIGINAL CODE IN THIS FILE COPIED FROM:

https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication/django_auth

********************************************************************
"""

"""mile4 URL Configuration

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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^accounts/', include(accounts_urls, namespace='accounts')),
    url(r'^commissions/', include(commissions_urls, namespace='commissions')),
    url(r'^checkout/', include(checkout_urls, namespace='checkout'))

]
