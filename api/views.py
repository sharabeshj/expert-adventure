from django.shortcuts import render
from rest_framework import viewsets
from api.models import Banks,Branches
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from api.serializers import BankSerializer,BranchesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class BankViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Banks.objects.all()
	serializer_class = BankSerializer

class BranchViewSet(viewsets.ModelViewSet):
	queryset = Branches.objects.all()
	serializer_class = BranchesSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
							IsOwnerOrReadOnly,)	

	@action(detail = False)
	def branch_list(self,request):
		branch_list = Branches.objects.filter(bank__name__iexact = request.GET.get('bank')).filter(city__iexact = request.GET.get('city'))
		serializer = self.get_serializer_class()(branch_list,many = True)
		return Response(serializer.data)
