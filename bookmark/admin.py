from django.contrib import admin

# Register your models here.

#(vDjBook)$ cd /home/shkim/pyDjango/ch99/bookmark/
#(vDjBook)$ vi admin.py

from django.contrib import admin
from bookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')