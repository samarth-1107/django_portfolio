from django.contrib import admin
from .models import AboutSectionDetail, ServiceSectionDetail,ProjectSectionDetail,ContactSectionDetail,ContactForm

admin.site.register(AboutSectionDetail)
admin.site.register(ServiceSectionDetail)
admin.site.register(ProjectSectionDetail)
admin.site.register(ContactSectionDetail)
admin.site.register(ContactForm)