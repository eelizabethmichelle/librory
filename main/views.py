from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'IPA 12 SMA',
        'amount': 10,
        'description': 'Non-fiction'
    }

    return render(request, "main.html", context)