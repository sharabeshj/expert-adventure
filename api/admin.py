from django.contrib import admin
from api.models import Banks,Branches

# Register your models here.

class BankAdmin(admin.ModelAdmin):
	pass
admin.site.register(Banks)

class BranchesAdmin(admin.ModelAdmin):
	pass
admin.site.register(Branches)
