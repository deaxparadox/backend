from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest

from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart


def order_create(request):
    cart: Cart = Cart(request) 
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['quantity']
                )
            # clear the cart
            cart.clear()
            
            # Launch asynchronous task 
            order_created.delay(order.id)

            # set the order in the session
            request.session['order_id'] = order.id 
            
            # redirect to payment 
            return redirect(reverse("payment:process"))

            # return render(request, "orders/order/created.html", {
            #     "order": order
            # })
    else: 
        form = OrderCreateForm()
    return render(request, "orders/order/create.html", {
        "cart": cart, "form": form
    })