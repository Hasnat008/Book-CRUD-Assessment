from django.contrib import admin
from .models import *
# Register your models here.

class AdminBookModel(admin.ModelAdmin):
    list_display = ['Title','Author','Publication_Year','ISBN','Price']


class AdminAuthorModel(admin.ModelAdmin):
    list_display = ['First_Name','Last_Name','Address']


admin.site.register(BookModel,AdminBookModel)
admin.site.register(AuthorModel,AdminAuthorModel)
