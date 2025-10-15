from django.contrib import admin
from django.urls import path
from automata_theory.views import *
from border_control2.views import *
from border_control1.views import *
from django.views.generic.base import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MainPageView.as_view(), name="main"),
    path(
        "login/",
        ExtendedLoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("border-control/", BorderControlView.as_view(), name="border_control"),
    path("border-control2/", BorderControl2View.as_view(), name="border_control2"),
    path("border-control1/", BorderControl1View.as_view(), name="border_control1"),
    path("account/", AccountView.as_view(), name="account"),
    path("kr/<int:kr_number>/", KRDetailView.as_view(), name="kr_detail"),
    path(
        "admin-panel/",
        RedirectView.as_view(url="/admin/", permanent=True),
        name="admin-panel",
    ),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
