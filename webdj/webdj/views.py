from django.shortcuts import render
from about.models import about

def home(request):
    if request.path == '/':
        my_data = about.objects.all()
        data = {'my_data': my_data}
    else:
        print("error in loading")
      
   
    return render(request, 'index.html', data)