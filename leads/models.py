from django.db import models


class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    source = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name} with {self.company}'
    

class LeadNote(models.Model):
    note = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='lead_contact', null=True, blank=True)


    def __str__(self):
        return f'{self.note} — {self.lead.first_name} {self.lead.last_name} with {self.lead.company}'
    