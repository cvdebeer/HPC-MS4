from django.urls import path
from .views import EventsListView
from search.views import SearchView


urlpatterns = [
    path('', EventsListView.as_view(), name='events'),
    path('search_results/', SearchView.as_view(), name='search')
]
