# Generated by Django 4.1.3 on 2022-11-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_issue_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
