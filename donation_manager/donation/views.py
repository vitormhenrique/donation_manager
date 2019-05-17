from django.shortcuts import render


def create_donation(request):
    context = {}
    return render(request, 'donation/index.html', context=context)