# Generated by Django 4.0.2 on 2022-02-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20211126_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Design', 'Design'), ('Development', 'Development'), ('Design & Development', 'Design & Development'), ('Growth', 'Growth')], max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='portfolioproduct',
            name='category',
            field=models.CharField(choices=[('Design', 'Design'), ('Development', 'Development'), ('Design & Development', 'Design & Development'), ('Growth', 'Growth')], max_length=255, verbose_name='Category'),
        ),
    ]
