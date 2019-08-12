from django.contrib import admin
from mysite.models import Profi, Position, Course
from django.db import models
from django.forms import widgets

class ProfiAdmin(admin.ModelAdmin):
    list_display = ["name","surname"]
    # fields = ["name","surname","email","position"]
    # exclude = ["date_of_birth"]
    # readonly_fields = ["is_active"]
    raw_id_fields = ["position"]
    save_as = True
    save_on_top = True

    fieldsets = [(None, {'fields':["name","surname"]}),
                 ('Other information', {'fields':["email","date_of_birth","position","is_active"],
                                        'classes':['collapse']}),]
    formfield_overrides = {
        models.DateField:  {'widget': widgets.TextInput}
    }

admin.site.register (Profi, ProfiAdmin)
admin.site.register (Position)
admin.site.register (Course)




