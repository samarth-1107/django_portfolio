from django.shortcuts import render, redirect
from .models import AboutSectionDetail, ServiceSectionDetail,ProjectSectionDetail,ContactSectionDetail,PersonalLinks,SkillsSectionDetails
from .forms import CreateContact

def index(request):

    personal_links = PersonalLinks.objects.all()
    about_section_details = AboutSectionDetail.objects.all()
    services_section_details = ServiceSectionDetail.objects.all()
    skills_section_details = SkillsSectionDetails.objects.all()
    project_section_details = ProjectSectionDetail.objects.all()
    contact_section_details = ContactSectionDetail.objects.all()

    contact_form = CreateContact()
    if request.method=="POST":
        contact_form = CreateContact(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('')

    context = {
        'personal_links':personal_links,
        'about_section_details':about_section_details,
        'services_section_details':services_section_details,
        'skills_section_details':skills_section_details,
        'project_section_details':project_section_details,
        'contact_section_details':contact_section_details,
        'contact_form':contact_form
        }
    return render(request, 'index.html', context=context)
