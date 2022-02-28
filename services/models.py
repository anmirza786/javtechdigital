from unicodedata import category
from django.db import models


class Proposal(models.Model):
    name = models.CharField(max_length=255, null=False,
                            blank=False, verbose_name="Name")
    email = models.EmailField(null=False, blank=False, verbose_name="Email")
    phone = models.CharField(max_length=255, blank=False,
                             verbose_name="Phone Number")
    proposalText = models.TextField(
        null=False, blank=False, verbose_name="Requested Proposal")

    def __str__(self):
        return self.name


class PortfolioProduct(models.Model):
    category = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Category", choices=(('Design', 'Design'), ('Development',
                                                                                                          'Development'), ('Design & Development', 'Design & Development'), ('Growth', 'Growth')))
    aboutProduct = models.TextField(
        null=False, blank=False, verbose_name="About Product")
    link = models.URLField(blank=False, null=False,
                           verbose_name="Portfolio Link")

    def __str__(self):
        return self.category


class PortfolioShowcase(models.Model):
    aboutProduct = models.TextField(
        null=False, blank=False, verbose_name="About Product")
    link = models.URLField(blank=False, null=False,
                           verbose_name="Portfolio Link")
    picture = models.ImageField(
        upload_to='portfolio-showcase', blank=False, null=False, verbose_name="Image")

    def __str__(self):
        return self.link


class Services(models.Model):
    category = models.CharField(max_length=256, choices=(('Design', 'Design'), ('Development',
                                                                                'Development'), ('Design & Development', 'Design & Development'), ('Growth', 'Growth')), null=False, blank=False)
    title = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
