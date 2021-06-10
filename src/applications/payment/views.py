
# Copyright (c) 2017-2021 luispenagos91@gmail.com
# Distribuido bajo la licencia MIT Software Licence
# Mas informacion http://www.opensource.org/licenses/mit-license.php

import logging
# Importando configuraciones del core
from django.conf import settings

# Importando las bases del api de paymentwall
from paymentwall.base import Paymentwall
from paymentwall.widget import Widget
from paymentwall.pingback import Pingback

# Django imports
from django.views import View
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render

# DRF Imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Importando modelos necesarios para el funcionamiento
from applications.authentication.models import Account
from .models import PaymentLogs, PaymentCode

# Configuraciones iniciales de paymentwall
Paymentwall.set_api_type(Paymentwall.API_VC)
Paymentwall.set_app_key(settings.PAYMENTWALL_PUBLIC_KEY) # available in your merchant area
Paymentwall.set_secret_key(settings.PAYMENTWALL_PRIVATE_KEY) # available in your merchant area

logger = logging.getLogger(__name__)

def PayWidget(user, email):
    widget = Widget(
        user,
        'p1_1',
        [],
        {
            'email': email,
            'ps': 'all',
        },
    )
    return widget.get_url()


class UsePaymentCode(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, code):
        user = request.user
        try:
            code = PaymentCode.objects.get(pk=code)
            if not code.status:
                code.use_code(user)
                return Response({'status': 'Codigo Aplicado'}, status=status.HTTP_200_OK)

            return Response({'status': 'Codigo Usado'}, status=status.HTTP_400_BAD_REQUEST)

        except PaymentCode.DoesNotExist:
            return Response({'status': 'Codigo no encontrado'}, status=status.HTTP_404_NOT_FOUND)


class ShowPaymentWidget(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        widget = PayWidget(request.user.login, request.user.email)
        return Response({'widget': widget})


class PaymentwallCallbackView(View):

    def __get_request_ip(self):
        x_fordwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_fordwarded_for:
            ip = x_fordwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def get(self, request, *args, **kwargs):
        # TODO
        # Send Email with link for get a ramdon goods
        pingback = Pingback(request.GET.copy(), self.__get_request_ip())

        if pingback.validate():
            """
                Validate if pinback are valid
            """
            
            virtual_currency = pingback.get_vc_amount()
            if int(virtual_currency) >= 1500:
                virtual_currency += int((virtual_currency *20) /100)
            
            if pingback.is_deliverable():
                """
                    Can deliver the coins
                    Verify if account exist and reference is valid
                """
                try:
                    account = Account.objects.get(login=pingback.get_user_id())
                    paylogs = PaymentLogs.objects.get(reference_id=pingback.get_reference_id())

                    if paylogs:
                        # Refence id Found
                        return HttpResponse('Reference duplicate', status=200)

                except Account.DoesNotExist:
                    return HttpResponse('Account Does Not Exist', status=200)

                except PaymentLogs.DoesNotExist:
                    """
                        If not exist PaymentLog deliver the coins
                    """
                    account = Account.objects.get(login=pingback.get_user_id())
                    account.coins = int(account.coins) + int(virtual_currency)
                    paylogs = PaymentLogs(
                        reference_id=pingback.get_reference_id(),
                        account_id=account.id,
                        username=account.login,
                        coins=virtual_currency,
                        status=True
                    )
                    paylogs.save()
                    account.save()

            elif pingback.is_cancelable():
                if int(virtual_currency) < 0:
                    try:
                        account = Account.objects.get(login=pingback.get_user_id())

                    except Account.DoesNotExist:
                        return HttpResponse('Nothing for do', status=200)

                    account.coins = int(account.coins) - abs(int(virtual_currency))
                    account.save()

            else:
                logger.error('Paymentwall pingback: Unknown pingback type, Paymentwall sent this data: {}'
                      .format(request.GET.copy()))

            return HttpResponse('OK', status=200)
        else:
            logger.error('Paymentwall pingback: Cant validate pingback, error: {} Paymentwall sent this data: {} IP {} '
                  .format(pingback.get_error_summary(), request.GET.copy(), self.__get_request_ip() ))
