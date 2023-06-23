from django.contrib import admin
from .models import Proposal, ProposalField

# Register your models here.


class ProposalFieldInline(admin.TabularInline):
    model = ProposalField
    extra = 0


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    inlines = [ProposalFieldInline]
