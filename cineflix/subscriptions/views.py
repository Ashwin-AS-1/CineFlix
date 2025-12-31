from django.shortcuts import render

# Create your views here.
from django.views import View

from . models import SubscriptionPlans

class SubscriptionsView(View):

    template ='subscriptions/subscription-list.html'

    def get(self,request,*args,**kwargs):
        
        plans =SubscriptionPlans.objects.all()

        data = {'plans':plans}

        return render(request,self.template,context=data)
    

