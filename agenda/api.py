from agenda.models import agendamentosModel
from rest_framework import viewsets, permissions
from .serializers import AgendamentoSerializer

# Agendamento Viewset
class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = agendamentosModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AgendamentoSerializer