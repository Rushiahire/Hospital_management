from django.urls import path
from . import views
from patient.views import New_patient,Details,Update_info,Book_appointment

urlpatterns =[
    path('',views.Home.as_view(),name='Home'),
    path('add_patient',New_patient.as_view(),name='patient'),
    path('login/',views.Login.as_view(),name="login"),
    path('logout',views.Logout.as_view(),name="logout"),
    path('details/',Details.as_view(),name='details'),
    path('update_form/',Update_info.as_view(),name='update_info'),
    path('book_appointment',Book_appointment.as_view(),name="book appointment"),
    path('view_appointment',views.Booked_appointment.as_view(),name='booked')
]