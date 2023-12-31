from django.db import models

class AboutSectionDetail(models.Model):
    first_paragraph = models.CharField(max_length=500)
    second_paragraph = models.CharField(max_length=500)
    about_image = models.ImageField(upload_to="images")

class ServiceSectionDetail(models.Model):
    icon = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    descreption = models.CharField(max_length=500)

    def __str__(self):
        return self.title