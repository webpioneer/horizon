
from django.conf.urls.defaults import patterns, url

from main.views import contact


urlpatterns = patterns("",

    url("contact/$", contact, name="contact"),

)
