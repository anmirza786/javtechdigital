from django.db import models
# Create your models here.


class Testimonial(models.Model):
    customer = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Customer`s Name")
    review = models.TextField(blank=False, null=False,
                              verbose_name="Customer`s Review")
    home_display = models.BooleanField(default=False)
    link = models.URLField()

    def __str__(self):
        return self.customer


class CompanyGrowth(models.Model):
    experience = models.IntegerField(blank=False, null=False,
                                     verbose_name="Years of Experience")
    cilents = models.IntegerField(
        blank=False, null=False, verbose_name="Global Happy Clients")
    projects = models.IntegerField(
        blank=False, null=False, verbose_name="Completed Projects")
    working = models.IntegerField(
        blank=False, null=False, verbose_name="Working Hours")
    days = models.IntegerField(
        blank=False, null=False, verbose_name="Working Days a week")
    ratting = models.DecimalField(
        blank=False, null=False, verbose_name="Custumer Rating", decimal_places=1, max_digits=4)

    def __str__(self) -> str:
        return str(self.id)


class OurTeam(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name="Name")
    picture = models.ImageField(
        upload_to='our-team', blank=False, null=False, verbose_name="Image")
    post = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name="Post in Company")
    intro = models.TextField(blank=False, null=False,
                             verbose_name="A Little Introduction")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Our Team"
        verbose_name_plural = "Our Team"


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name="Name")
    picture = models.ImageField(
        upload_to='our-products', blank=False, null=False, verbose_name="Product Icon")
    link = models.URLField(max_length=128, db_index=True, unique=True,
                           blank=True, verbose_name="Hyperlink to product")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Contact(models.Model):
    email = models.EmailField(blank=False, null=False,
                              verbose_name="Email Address")
    message = models.TextField(blank=False, null=False, verbose_name="Message")
    is_contacted = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
        
