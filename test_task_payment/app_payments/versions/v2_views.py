from api_decorators import access_token_checker,settings,Response,api_view
from ..payments import JsonReader
# Create your views here.


@access_token_checker()
@api_view(['GET', 'POST'])
def payments(request,agreement_id=None):
    data = JsonReader(settings.PAYMENTS_JSON).f_read()
    status = 200
    if agreement_id:
        data = [v_data for k,v in data.iteritems() for v_data in v if agreement_id == k]
    return Response(data,status)

@access_token_checker()
@api_view(['GET', 'POST'])
def all_payments(request):
    data = [payment for array in JsonReader(settings.PAYMENTS_JSON).f_read().values() for payment in array]
    status = 200
    return Response(data,status)