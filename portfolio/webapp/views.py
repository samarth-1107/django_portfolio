from django.shortcuts import render

def index(request):
    context = {'message':'Basic structure ready'}
    return render(request, 'index.html', context=context)

def about_section(request):
   
    # context = {'about_section_details':about_section_details}
    return render(request, 'index.html')

def services_section(request):
   
    # context = {'services_section_details':services_section_details}
    return render(request, 'index.html')