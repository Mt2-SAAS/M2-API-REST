# Copyright (c) 2017-2018 luispenagos91@gmail.com
# Distribuido bajo la licencia MIT Software Licence
# Mas informacion http://www.opensource.org/licenses/mit-license.php

# imporacion por defecto
from django.urls import path

from . import views

urlpatterns = [
    path("checkout/", views.PaymentwallCallbackView.as_view(), name="checkout"),
    path("widget/", views.ShowPaymentWidget.as_view(), name="widget"),
    path("promo/<str:code>", views.UsePaymentCode.as_view(), name="promo"),
]
