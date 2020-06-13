from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from .views import *

app_name='site_manager'

urlpatterns = [
    path('unsubscribe/<uidb64>/<uidb64cat>/<token>/', Unsubscribe.as_view(), name='unsubscribe'),
    path('sendmail/', staff_member_required(SendMassiveEmail.as_view()), name='send_mass_mail'),

]
