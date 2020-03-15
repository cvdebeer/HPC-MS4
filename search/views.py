from itertools import chain
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from events.models import Event, EventType

'''
The entire Search app was copied and adjusted for this project from a tutorial by codingforentrepeneurs.com - https://www.codingforentrepreneurs.com/blog/a-multiple-model-django-search-engine/

An issue creating an "Related Field has invalid lookup: icontains" was resolved with the help of stack overflow- https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains
'''


class SearchView(ListView):
    template_name = 'events/search_results.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            event_results = Event.objects.search(query)
            type_results = EventType.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                event_results,
                type_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Event.objects.none()  # just an empty queryset as default
