from django.contrib import admin
import models

class TweetAdmin(admin.ModelAdmin):
    list_display = ('posted_by', 'posted_on')

admin.site.register(models.Tweet, TweetAdmin)
