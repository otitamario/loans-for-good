from django.db import models


# Create your models here.
class Proposal(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("DENIED", "Denied"),
    )

    # Campos do modelo de proposta
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="PENDING"
    )
    # Adicione campos de relacionamento, se necessário

    def __str__(self):
        return self.name


class ProposalField(models.Model):
    proposal = models.ForeignKey(
        Proposal, on_delete=models.CASCADE, related_name="fields"
    )
    field_name = models.CharField(max_length=100)
    field_value = models.CharField(max_length=255)

    def __str__(self):
        return self.field_name
