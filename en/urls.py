from django.urls import path
from . import views
from django.views.generic.base import RedirectView

app_name = 'en'
urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('<current_page>', RedirectView.as_view(url='%(current_page)s/'), name='language'),

    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('work/', views.work, name='work'),
    path('work/all/', views.work_all, name='work_all'),
    path('contact/', views.contact, name='contact'),
]

htmx_urlpatterns = [
    path('load_realworld/', views.get_realworld, name='load_realworld'),
    path('load_personal/', views.get_personal, name='load_personal'),
    path('load_challenge/', views.get_challenge, name='load_challenge'),
]

urlpatterns += htmx_urlpatterns