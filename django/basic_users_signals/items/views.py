from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import StockForm, OrderForm
from .models import Stock, Order

from django.contrib import messages

# Create your views here.
@login_required
def stock(requests):

    if requests.method == 'POST':
        form = StockForm(requests.POST)
        if form.is_valid():
            form.save()
            messages.success(requests,'Product Added!')
            return redirect("stock")

    else:
        form = StockForm()
        products = Stock.objects.all()

    return render(requests, 'items/stock.html', {'form': form, 'products': products})

@login_required
def order(requests):
    
    if requests.method == 'POST':
        form = OrderForm(requests.POST)
        if form.is_valid():
            product = Stock.objects.filter(product = form.cleaned_data.get('product')).first()
            ordered = Order(
                stock_item = product,
                quantity = form.cleaned_data.get('quantity')
            )
            ordered.save() # hace falta el save aca si esta en signals? Si xq asi se activa la señal
            messages.success(requests, 'Product Ordered!')
            return redirect("order")

    else:
        form = OrderForm()

    return render(requests, 'items/order.html', {'form': form})