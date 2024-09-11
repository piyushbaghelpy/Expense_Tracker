from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import CurrentBalance, TrackingHistory, RequestLogs

admin.site.register(CurrentBalance)
admin.site.register(TrackingHistory)
admin.site.register(RequestLogs)