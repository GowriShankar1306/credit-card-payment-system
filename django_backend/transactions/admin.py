from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, Count
from django.shortcuts import render
from django.urls import path
from django.utils import timezone

import csv

from django.http import HttpResponse
from django.contrib import admin

from .models import Transaction


def export_transactions_csv(modeladmin, request, queryset):
    response = HttpResponse(
        content_type='text/csv'
    )

    response['Content-Disposition'] = (
        'attachment; filename="transactions.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
        'ID',
        'User',
        'Payment ID',
        'Amount',
        'Status',
        'Transaction Date'
    ])

    for transaction in queryset:
        writer.writerow([
            transaction.id,
            transaction.user.username,
            transaction.payment_id,
            transaction.amount,
            transaction.status,
            transaction.transaction_date
        ])

    return response


export_transactions_csv.short_description = "Export selected transactions as CSV"

@staff_member_required
def daily_payment_summary(request):
    today = timezone.localdate()

    transactions = Transaction.objects.filter(
        transaction_date__date=today
    )

    total_transactions = transactions.count()

    successful_transactions = transactions.filter(
        status='SUCCESS'
    ).count()

    failed_transactions = transactions.filter(
        status='FAILED'
    ).count()

    total_amount = transactions.aggregate(
        total=Sum('amount')
    )['total'] or 0

    context = {
        'today': today,
        'total_transactions': total_transactions,
        'successful_transactions': successful_transactions,
        'failed_transactions': failed_transactions,
        'total_amount': total_amount,
    }

    return render(
        request,
        'admin/daily_payment_summary.html',
        context
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'payment_id',
        'amount',
        'status',
        'transaction_date',
    )

    list_filter = (
        'status',
        'transaction_date',
    )

    search_fields = (
        'user__username',
        'payment_id',
    )

    actions = [export_transactions_csv]

    def get_urls(self):      
        urls = super().get_urls()

        custom_urls = [
            path(
                'daily-summary/',
                self.admin_site.admin_view(daily_payment_summary),
                name='daily-payment-summary',
            ),
        ]

        return custom_urls + urls