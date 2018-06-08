# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
from django.conf.urls import url
from django.conf import settings
import requests
from django.shortcuts import render
from django.http import request
from django.urls import reverse
# Register your models here.

class AdminPayments(admin.ModelAdmin):

    def get_urls(self):
        return [
            url(r'^$', self.admin_json_payments_list, name='app_payments_paymentsfromjson_changelist'),
        ]

    def admin_json_payments_list(self,request):
        model = self.model
        model.opts = self.model._meta
        opts = model._meta
        app_label = opts.app_label
        title = opts.verbose_name_plural
        context = {}

        url = reverse('api_v2:payments')
        headers = {'Access-Token':'A8oMYPs8nL71obvF6zcJK0Xjo'}
        r =requests.get(request.build_absolute_uri(url),headers=headers)
        data = r.json()
        model.full_result_count = len(data)
        model.result_count = len(data)
        results_keys = set([k for item in data for k in item.keys()])
        context = {
            'cl': model,
            'title': title
        }
        context['results'] = data
        context['app_label'] = 'app_payments'
        context['results_keys'] = sorted(results_keys,reverse=True)
        return render(request, 'admin_payments/change_list.html', context)

admin.site.register(PaymentsFromJson,AdminPayments)