from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Client, Contact, Site
from .forms import ClientForm, ContactForm, SiteForm


# list views


def index(request): # list of clients
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'clients/index.html', context)


def contact_index(request): # list of contacts
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'clients/contact_index.html', context)


def site_index(request): # list of sites
    sites = Site.objects.all()
    context = {
        'sites': sites
    }
    return render(request, 'clients/site_index.html', context)


# create views


def create_client(request): # create a client
    if request.method == 'POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('clients-home'))
    else:
        form = ClientForm()
    return render(request, 'clients/create_client.html', {'form': form})


def create_contact(request): 
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('clients-home'))
    else:
        form = ContactForm()
    return render(request, 'clients/create_contact.html', {'form': form})


def create_site(request): # create a site
    if request.method == 'POST':
        form=SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('clients-home'))
    else:
        form = SiteForm()
    return render(request, 'clients/create_site.html', {'form': form})


# detail views


def client_detail(request, pk): # client detail
    clients = get_object_or_404(Client, pk=pk)
    sites = Site.objects.filter(client=clients)
    employees = Contact.objects.filter(company=clients)
    print(employees)
    context = {
        'clients': clients,
        'sites': sites,
        'employees': employees,
    }
    return render(request, 'clients/client_detail.html', context)


def contact_detail(request, pk): # contact detail
    contact = get_object_or_404(Contact, pk=pk)
    context = {
        'contact': contact
    }
    return render(request, 'clients/contact_detail.html', context)


def site_detail(request, pk): # site detail
    site = get_object_or_404(Site, pk=pk)
    context = {
        'site': site
    }
    return render(request, 'clients/site_detail.html', context)


# update views


def update_client(request, pk): # update a client
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect(reverse('clients-home'))
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/update_client.html', {'form': form})


def update_contact(request, pk): # update a contact
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(reverse('clients-home'))
    else:
        form = ContactForm(instance=contact)
    return render(request, 'clients/update_contact.html', {'form': form})


def update_site(request, pk): # update a site
    site = get_object_or_404(Site, pk=pk)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect(reverse('clients-home'))
    else:
        form = SiteForm(instance=site)
    return render(request, 'clients/update_site.html', {'form': form})


# delete views


def delete_client(request, pk): # delete a client
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect(reverse('clients-home'))
    return render(request, 'clients/delete_client.html', {'client': client})


def delete_contact(request, pk): # delete a contact
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(reverse('clients-home'))
    return render(request, 'clients/delete_contact.html', {'contact': contact}) 


def delete_site(request, pk): # delete a site
    site = get_object_or_404(Site, pk=pk)
    if request.method == 'POST':
        site.delete()
        return redirect(reverse('clients-home'))
    return render(request, 'clients/delete_site.html', {'site': site})