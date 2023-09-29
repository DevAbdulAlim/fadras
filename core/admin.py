from django.contrib import admin
from .models import Project, Markets, Client
# Register your models here.

admin.site.register(Project)
admin.site.register(Markets)
admin.site.register(Client)

admin.site.site_title = "Fadras"
admin.site.site_header = "Fadras Admin"
