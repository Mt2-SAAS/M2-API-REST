# Copyright (c) 2017-2021 luispenagos91@gmail.com
# Distribuido bajo la licencia MIT Software Licence
# Mas informacion http://www.opensource.org/licenses/mit-license.php

from django.contrib import admin

from .models import PaymentLogs, PaymentCode


class PaymentLogsDisplay(admin.ModelAdmin):
    list_display = ('reference_id', 'account_id', 'username', 'coins', 'status', 'create_at')
    readonly_fields = ('status',)
    search_fields = ['username']


class PaymentCodeDisplay(admin.ModelAdmin):
    list_display = ('id', 'status', 'coins', 'user_claim', 'account_id')
    readonly_fields = ('status',)
    search_fields = ['user_claim']


admin.site.register(PaymentLogs, PaymentLogsDisplay)
admin.site.register(PaymentCode, PaymentCodeDisplay)
