# Generated by Django 5.0.2 on 2024-02-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(verbose_name='Salary'),
        ),
    ]