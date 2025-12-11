from django.urls import path

from . import views

urlpatterns =[


    path('subscriptions-list/',views.SubscriptionsView.as_view(),name='subscription-list'),
]