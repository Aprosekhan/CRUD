from django.contrib import admin

from .models import Post

@admin.register(Post)

class AdminPost(admin.ModelAdmin):
    list_display = ('id','Name','Email','Password')

