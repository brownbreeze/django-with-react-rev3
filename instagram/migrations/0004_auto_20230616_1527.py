# Generated by Django 3.0.14 on 2023-06-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_post_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
