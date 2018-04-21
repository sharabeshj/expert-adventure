from rest_framework import serializers
from api.models import Branches,Banks

class BankSerializer(serializers.ModelSerializer):
	class Meta:
		model = Banks
		fields = ('name','id')

class BranchesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Branches
		fields =  ('ifsc','bank','branch','address','city','district','state')