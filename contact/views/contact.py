from django.shortcuts import render, get_object_or_404
from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True)

    context = {'contacts': contacts, 'title': 'Home'}

    return render(request, 'contact/index.html', context)


def contact(request, id):
    single_contact = get_object_or_404(Contact, pk=id, show=True)

    context = {
        'contact': single_contact,
        'title': f'{single_contact.first_name} {single_contact.last_name}',
    }

    return render(request, 'contact/contact.html', context)
