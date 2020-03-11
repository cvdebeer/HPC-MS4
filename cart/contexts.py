from django.shortcuts import get_object_or_404
from events.models import Event, EventType


def cart_contents(request):
    '''
    This is taken directly from the CI tutorial on carts and adjusted to suit project needs
    '''
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    total_participant = 0
    total_non_participant = 0
    total_trainee = 0
    event_count = 0
    for id, quantity in cart.items():
        event = get_object_or_404(Event, pk=id)
        total_participant += quantity * event.event.cost_participant
        total_non_participant += quantity * event.event.cost_non_participant
        total_trainee += quantity * event.event.cost_trainee
        total = total_participant + total_non_participant + total_trainee
        event_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'event': event})

    return{'cart_items': cart_items, 'total': total, 'event_count': event_count}
