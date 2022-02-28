from django.db import models

# Create your models here.


class CourseForm(models.Model):
    firstname = models.CharField(max_length=255, null=False,
                                 blank=False, verbose_name="First Name")
    lastname = models.CharField(max_length=255, null=False,
                                blank=False, verbose_name="Lastt Name")
    email = models.EmailField(null=False, blank=False, verbose_name="Email")
    phone = models.CharField(max_length=255, blank=False,
                             verbose_name="Phone Number")
    course = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Course Name")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Course Form"
        verbose_name_plural = "Course Forms"


class InternshipForm(models.Model):
    firstname = models.CharField(max_length=255, null=False,
                                 blank=False, verbose_name="First Name")
    lastname = models.CharField(max_length=255, null=False,
                                blank=False, verbose_name="Lastt Name")
    email = models.EmailField(null=False, blank=False, verbose_name="Email")
    phone = models.CharField(max_length=255, blank=False,
                             verbose_name="Phone Number")
    cv = models.FileField(upload_to='intership-form/',
                          blank=False, null=False, verbose_name="CV")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Internship Form"
        verbose_name_plural = "Internship Forms"
