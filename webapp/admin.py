from django.contrib import admin
from webapp.models import UserProfile, BandProfile, FanProfile, Event, Comment, Achievement, Feedback

admin.site.register(UserProfile)
admin.site.register(BandProfile)
admin.site.register(FanProfile)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Achievement)
admin.site.register(Feedback)