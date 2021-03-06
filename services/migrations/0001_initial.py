# Generated by Django 3.2.9 on 2021-11-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='Category')),
                ('aboutProduct', models.TextField(verbose_name='About Product')),
                ('link', models.URLField(verbose_name='Portfolio Link')),
            ],
            options={
                'verbose_name': 'Portfolio Product',
                'verbose_name_plural': 'Portfolio Products',
            },
        ),
        migrations.CreateModel(
            name='Portfolio_Showcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutProduct', models.TextField(verbose_name='About Product')),
                ('link', models.URLField(verbose_name='Portfolio Link')),
                ('picture', models.ImageField(upload_to='portfolio-showcase', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Portfolio Showcase',
                'verbose_name_plural': 'Portfolio Showcases',
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone Number')),
                ('request', models.TextField(verbose_name='Requested Proposal')),
            ],
            options={
                'verbose_name': 'Proposal',
                'verbose_name_plural': 'Proposals',
            },
        ),
    ]
