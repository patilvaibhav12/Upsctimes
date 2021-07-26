from django.contrib import admin
from .models import homepost, books, newspaper, eml, history, geography, polity, currentaffairs, generalscience, impupdates,pjobs, gjobs
# Register your models here.


admin.site.register(books)
admin.site.register(newspaper)
admin.site.register(eml)
admin.site.register(history)
admin.site.register(geography)
admin.site.register(polity)
admin.site.register(currentaffairs)
admin.site.register(generalscience)
admin.site.register(impupdates)


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/main.css",)
        }

        js = ("js/blog.js",)

admin.site.register(homepost, BlogAdmin)
admin.site.register(pjobs, BlogAdmin)
admin.site.register(gjobs, BlogAdmin)