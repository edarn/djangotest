from django.contrib import admin
from luletrafik2.models import Greeting

class GreetingSpec(admin.ModelAdmin):
   fields =['content']

admin_site = admin.AdminSite()
admin_site.register(Greeting)