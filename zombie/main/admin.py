from django.contrib import admin
from main.models import Zombie, Tweet

class ZombieAdmin(admin.ModelAdmin):
	list_display = ('name','cemetery','date_death',)
	search_fields = ('name',)

class TweetAdmin(admin.ModelAdmin):
	list_display = ('zombie','status','created_t',)
	

admin.site.register(Zombie, ZombieAdmin)
admin.site.register(Tweet, TweetAdmin)