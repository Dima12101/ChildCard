from django.contrib import admin
from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Card._meta.fields]

    list_filter = ['creator_id', 'date']
    search_fields = ['child_name']

    class Meta:
        model = Card


admin.site.register(Card, CardAdmin)
