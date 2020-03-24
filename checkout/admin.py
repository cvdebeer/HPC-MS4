from django.contrib import admin

from .models import Booking, BookingLineItem


class BookingLineAdminInline(admin.TabularInline):
    model = BookingLineItem


class BookingAdmin(admin.ModelAdmin):
    inlines = (BookingLineAdminInline, )


admin.site.register(Booking, BookingAdmin)
