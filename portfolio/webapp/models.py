from django.db import models

class AboutSectionDetail(models.Model):
    first_paragraph = models.CharField(max_length=500)
    second_paragraph = models.CharField(max_length=500)
    about_image = models.ImageField(upload_to="images/", null=True, default=None)
    resume = models.FileField(upload_to ='uploads/', null=True, default=None)

class ServiceSectionDetail(models.Model):
    icon = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    descreption = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    
class ProjectSectionDetail(models.Model):
    project_name = models.CharField(max_length=100, default= None)
    project_image = models.ImageField(upload_to="images/", null=True, default=None)
    project_link = models.CharField(max_length=300)
    def __str__(self):
        return self.project_name
    
class ContactSectionDetail(models.Model):
    personal_info = models.CharField(max_length=25)
    info_icon = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.personal_info
    
class ContactForm(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_number =models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    def __str__(self):
        return self.full_name
    
class PersonalLinks(models.Model) : 
    link_name = models.CharField(max_length=15)
    personal_link_icon = models.CharField(max_length = 20)
    personal_links = models.CharField(max_length=50)
    def __str__(self):
        return self.link_name