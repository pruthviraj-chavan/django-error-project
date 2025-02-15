from django.contrib import admin


from about.models import about

class aboutAdmin(admin.ModelAdmin):
    list_display = ('my_title','my_desc')

admin.site.register(about,aboutAdmin)