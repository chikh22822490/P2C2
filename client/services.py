"""
    services is a boxe (I named it boxe because it is considered like a buisiness logic holder )
    services  will be focusing on buisiness logic on post  update methods
    ==> buisiness logic will  be here (:
"""

from django.apps import apps

Client = apps.get_model('client', 'Client')
Account = apps.get_model('user', 'Account')




