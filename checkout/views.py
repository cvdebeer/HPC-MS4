import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils import timezone

from events.models import Event, EventType

from .forms import BookingForm, MakePaymentForm
from .models import BookingLineItem

stripe.api_key = settings.STRIPE_SECRET


def checkout(request):
    if request.method == "POST":
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.date = timezone.now()
            booking.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                event = get_object_or_404(Event, pk=id)
                total += quantity * event.event.price
                booking_line_item = BookingLineItem(
                    booking=booking,
                    event=event,
                    quantity=quantity
                )
                booking_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=event,
                    source=request.POST['stripeToken'],
                )
            except stripe.error.CardError:
                messages.error(request, 'Your card payment has been declined!')

            if customer.paid:
                messages.error(request, 'You have successfully paid')
                request.session['cart'] = {}
                return redirect(reverse('events'))
            else:
                messages.error(request, 'Unable to take payment')
        else:
            messages.error(
                request, 'We were unable to take a payment with that card!')
    else:
        booking_form = BookingForm()
    return render(request, 'checkout/checkout.html', {'booking_form': booking_form, 'publishable': settings.STRIPE_PUBLISHABLE})
