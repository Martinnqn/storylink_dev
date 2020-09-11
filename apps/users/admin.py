from django.contrib import admin
from django.contrib.admin.models import LogEntry

# Register your models here.

from apps.users.models import CustomUser, UserEvents, UserSubscriptionModelAux, PubSubscriptionModelAux, UserProfile
from apps.publications.models import StoryPublication, ResourcePublication, Tag, StoryChapter, ChapterLike, StoryLike

# users app
admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(UserEvents)
admin.site.register(UserSubscriptionModelAux)
admin.site.register(PubSubscriptionModelAux)


class StoryPublicationAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)  # publications app


admin.site.register(StoryPublication)
admin.site.register(StoryChapter)
admin.site.register(ResourcePublication)
admin.site.register(Tag)
admin.site.register(StoryLike)
admin.site.register(ChapterLike)


# admin.site.register(LogEntryAdmin)
admin.site.register(LogEntry)
