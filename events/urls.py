from django.urls import path

from search.views import SearchView

from .views import EventsListView

urlpatterns = [
    path('', EventsListView.as_view(), name='events'),
    path('search_results/', SearchView.as_view(), name='search')
]
