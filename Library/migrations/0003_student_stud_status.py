# Generated by Django 5.1 on 2024-08-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_alter_student_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stud_status',
            field=models.CharField(default='Active', max_length=255),
        ),
    ]