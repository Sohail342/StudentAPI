# Generated by Django 5.1.4 on 2024-12-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cgp',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
