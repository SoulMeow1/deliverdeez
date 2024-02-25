from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("staff-home/", views.staffHome, name = "staffHome"),
    path("part-time-home/", views.partTimeHome, name = "partTimeHome"),
    path("part-time-profile/<str:pk>/", views.partTimeProfile, name = "partTimeProfile"),
    path("accept-delivery/<str:pk>/", views.acceptDelivery, name = "acceptDelivery"),
    path("complete-delivery/<str:pk>/", views.completeDelivery, name = "completeDelivery"),
    path("create-delivery/", views.createDelivery, name = "createDelivery"),
    path("update-delivery/<str:pk>/", views.updateDelivery, name = "updateDelivery"),
    path("delete-delivery/<str:pk>/", views.deleteDelivery, name = "deleteDelivery"),
    path("login/", views.userLogin, name = "login"),
    path("register/", views.register, name = "register"),
    path("logout/", views.logoutUser, name = "logoutUser"),
]
