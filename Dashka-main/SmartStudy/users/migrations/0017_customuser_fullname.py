# Generated by Django 4.2.5 on 2023-11-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_group_alter_customuser_middlename_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Полное имя'),
        ),
    ]