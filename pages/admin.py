from django.contrib import admin
from .models import Command


@admin.action(description='فعال کردن نظر')
def activer(modeladmin, request, queryset):
    queryset.update(is_active=True)


class CommendActive(admin.ModelAdmin):
    actions = [activer]


admin.site.register(Command, CommendActive)
