from django.conf.urls import *
from luletrafik2.views import main_page, sign_post
from django.contrib import admin
from luletrafik2.admin import admin_site
#admin.autodiscover()
urlpatterns = patterns('',
    (r'^sign/$', sign_post),
    (r'^$', main_page),
	#(r'^admin/', include(admin_site.urls)),
	(r'^admin/', include(admin.site.urls)),
)