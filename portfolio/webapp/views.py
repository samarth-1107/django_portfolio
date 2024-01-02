from django.shortcuts import render
from .models import AboutSectionDetail, ServiceSectionDetail,ProjectSectionDetail,ContactSectionDetail

def index(request):
    about_section_details = AboutSectionDetail.objects.all()
    services_section_details = ServiceSectionDetail.objects.all()
    project_section_details = ProjectSectionDetail.objects.all()
    contact_section_details = ContactSectionDetail.objects.all()
    context = {
        'message':'Basic structure ready',
        'about_section_details':about_section_details,
        'services_section_details':services_section_details,
        'project_section_details':project_section_details,
        'contact_section_details':contact_section_details,
        }
    return render(request, 'index.html', context=context)