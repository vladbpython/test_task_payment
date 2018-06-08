from django.conf.urls import url
import v2_views
urlpatterns = [
    url(r'^agreements/(?P<agreement_id>(\d*))/payments/$', v2_views.payments,name='agreement'),
    url(r'^agreements/$', v2_views.payments,name='agreements'),
    url(r'^payments/$',v2_views.all_payments,name='payments'),
]
