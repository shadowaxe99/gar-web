
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ai_assistant/', include('ai_assistant.urls')),
    path('blockchain/', include('blockchain.urls')),
    path('nlp/', include('nlp.urls')),
]
