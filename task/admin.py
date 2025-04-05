from django.contrib import admin

from .models import Task , Comment , Note , Attachment , Board ,Column , Workspace

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Note)
admin.site.register(Attachment)
admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Workspace)

