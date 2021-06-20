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
            ordered.save()
            if ordered.id:
                messages.success(requests,f'You have ordered {ordered.quantity} {product.product}(s)!')
            else:
                messages.error(requests,'No Stock!')
            return redirect("order")

    else:
        form = OrderForm()

    return render(requests, 'items/order.html', {'form': form})