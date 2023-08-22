
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nlp/', include('apps.nlp.urls')),
    path('blockchain/', include('apps.blockchain.urls')),
    path('agents/', include('apps.agents.urls')),
    path('federated_learning/', include('apps.federated_learning.urls')),
    path('ai_planning/', include('apps.ai_planning.urls')),
    path('inlp/', include('apps.inlp.urls')),
    path('smart_healthcare/', include('apps.smart_healthcare.urls')),
]
