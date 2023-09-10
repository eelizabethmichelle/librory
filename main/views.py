from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'app_name': 'librory',
        'name': 'Michelle Elizabeth Amanda Hutasoit',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)