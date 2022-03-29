# Generated by Django 4.0.3 on 2022-03-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_rename_aboutproduct_portfolioproduct_about_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Design', 'Design'), ('Development', 'Development'), ('Design & Development', 'Design & Development'), ('Growth', 'Growth')], max_length=256)),
                ('category_description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='services',
            name='category',
        ),
        migrations.RemoveField(
            model_name='services',
            name='slug',
        ),
        migrations.DeleteModel(
            name='SubServices',
        ),
        migrations.AddField(
            model_name='category',
            name='services',
            field=models.ManyToManyField(to='services.services'),
        ),
    ]
