from django.contrib import admin
from tracker.models import *
from django.contrib import admin
from .models import CurrentBalance, TrackingHistory, RequestLogs

admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker"
admin.site.site_url = "Expense Tracker"

admin.site.register(CurrentBalance)



class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "amount",
        "current_balance",
        "expense_type",
        "description",
        "created_at",
        "display_age"
    ]
    actions = [make_credit, make_debit] 



search_fields = ['expense_type', 'description']
list_filter = ['expense_type']
ordering = ['-expense_type']

admin.site.register(TrackingHistory)
admin.site.register(RequestLogs)