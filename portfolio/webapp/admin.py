from django.contrib import admin
from .models import AboutSectionDetail, ServiceSectionDetail,ProjectSectionDetail,ContactSectionDetail,ContactForm,PersonalLinks,SkillsSectionDetails

admin.site.register(AboutSectionDetail)
admin.site.register(ServiceSectionDetail)
admin.site.register(SkillsSectionDetails)
admin.site.register(ProjectSectionDetail)
admin.site.register(ContactSectionDetail)
admin.site.register(ContactForm)
admin.site.register(PersonalLinks)