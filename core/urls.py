from django.urls import path
from .views import (
    ItemDetailView,
    # CheckoutView,
    HomeView,
    # OrderSummaryView,
    # add_to_cart,
    # remove_from_cart,
    # remove_single_item_from_cart,
    # PaymentView,
    # AddCouponView,
    # RequestRefundView
)

app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
]
