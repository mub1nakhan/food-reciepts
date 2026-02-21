from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("contact", views.contact_veiw, name="contacts"),
    path("meal/<int:pk>",views.meal_detail, name="meal_detail")
]
