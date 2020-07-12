from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'detail/(\d+)/$', detail, name="detail"),
    url(r'about/$', about, name="about"),
    url(r'contact/$', contact, name="contact"),
]
