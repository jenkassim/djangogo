from django.conf.urls import url

from .views import (
        ProductListView,
        # product_list_view,
        # ProductDetailView,
        # product_detail_view,
        # ProductFeaturedListView,
        # ProductFeaturedDetailView,
        ProductDetailSlugView,
        )

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]