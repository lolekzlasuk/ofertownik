from django.urls import path
from . import views
app_name = 'ofertownik'
urlpatterns = [
    path('add',views.create_offer,name="createoffer"),
    path('<slug:slug>/',views.OfferDetailView.as_view(),name="viewoffer"),
    path('<slug:slug>/edit',views.edit_offer,name="editoffer"),
    path('offers',views.OfferListView.as_view(),name="offerlist"),
    path('addproduct',views.addproduct,name='addproduct'),
    path('deleteproduct',views.deleteproduct,name='deleteproduct'),
    path('editproduct',views.editproduct,name='editproduct'),
    path('deleteimage/<int:pk>',views.deleteimage,name='deleteimage'),
    path('product/<int:pk>/addimage',views.addimage,name='addimage'),
    path('send_email',views.send_email,name='sendmail'),


]
