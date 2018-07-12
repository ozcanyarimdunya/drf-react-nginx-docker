from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html')),
    path('', include('tasker.urls')),
    path('docs/', include_docs_urls(
        title="Project api", description="Tasker api Documentation (Development only)"
    )),
]
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
