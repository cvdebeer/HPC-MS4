from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .forms import MakePaymentForm, BookingForm
from django.conf import settings
from django.utils import timezone
from events.models import Event, EventType
from .models import Booking, BookingLineItem
import stripe

stripe.api_key = settings.STRIPE_SECRET


def checkout(request):
    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if booking_form.is_valid() and payment_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.date = timezone.now()
            booking.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                event = get_object_or_404(Event, pk=id)
                total += quantity * event.price
                booking_line_item = BookingLineItem(
                    booking=booking,
                    event=event,
                    quantity=quantity
                )
                booking_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency='ZAR',
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
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
            print(payment_form.errors)
            messages.error(
                request, 'We were unable to tkae a payment with that card!')
    else:
        payment_form = MakePaymentForm()
        booking_form = BookingForm()
    return render(request, 'checkout.html', {'booking_form': booking_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
