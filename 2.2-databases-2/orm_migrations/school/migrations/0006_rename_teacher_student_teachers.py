# Generated by Django 5.0.3 on 2024-04-09 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_student_options_alter_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]