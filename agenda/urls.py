from rest_framework import routers
from .api import AgendamentoViewSet

router = routers.DefaultRouter()
router.register('api/agendamentoModel', AgendamentoViewSet, 'agendamentoModel')

urlpatterns = router.urls