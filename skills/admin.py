from django.contrib import admin
from .models import *

# Register your models here.

from django.contrib.admin.options import ModelAdmin

admin.site.site_header = 'TechEra Administration'                 # default: "Django Administration"
admin.site.index_title = 'TechEra Database Structure'                 # default: "Site administration"
admin.site.site_title = 'TechEra Site Admin'                      # default: "Django site admin"


class LearnerAdmin(ModelAdmin):
    list_display = []
    search_fields = []
    list_filter = []


admin.site.register(Learner, LearnerAdmin)
