from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from base.forms import AuthenticationForm

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('meeting_list')), name="homepage"),
    url(r'^meetings/', include('meeting.urls')),
    url(r'^login/$',
        views.LoginView.as_view(
            form_class=AuthenticationForm,
            template_name='login.jinja2'
        ),
        name='login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name='logout.jinja2'), name='logout'),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
