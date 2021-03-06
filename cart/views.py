from django.shortcuts import render, redirect, reverse

''' This code is copied from CI tutorial and adjusted where needed for project'''


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('events'))


def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view-cart'))
