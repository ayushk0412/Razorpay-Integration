from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay
# Create your views here.


def index(request):
    # OPTIONALclient.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000
        currency = 'INR'
        client = request.Client(
            auth=('', ''))
        payment = client.order.create(
            {'amount': amount, 'currency': "INR", 'payment_capture': '1'})
    return render(request, "index.html")


@csrf_exempt
def success(request):
    return render(request, "success.html")
