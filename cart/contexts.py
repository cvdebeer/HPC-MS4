from django.shortcuts import get_object_or_404
from events.models import Event, EventType


def cart_contents(request):
    '''
    This is taken directly from the CI tutorial on carts and adjusted to suit project needs
    '''
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    event_count = 0
    for id, quantity in cart.items():
        event = get_object_or_404(Event, pk=id)
        total += quantity * event.event.price
        event_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'event': event})

    return{'cart_items': cart_items, 'total': total, 'event_count': event_count}
