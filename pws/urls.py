from django.urls import path
from .views import pwsView,sflOrderDataView,provisioningView


urlpatterns = [
    path('pws/home',pwsView),
    path('pws/sfldata',sflOrderDataView,name='sfldata'),
    path('pws/provision',provisioningView,name='provision')
]
