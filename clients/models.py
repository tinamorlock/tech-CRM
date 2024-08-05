from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    job_title = models.CharField(max_length=100, default='N/A')
    office_phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='company_account', null=True, blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name} with {self.company.company}'


class Client(models.Model):
    company = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='client_contact', null=True, blank=True)


    def __str__(self):
        return f'{self.company}'
    

class Site(models.Model):
    site_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='main_client', null=True, blank=True)


    def __str__(self):
        return f'{self.site_name} — {self.client.company}'