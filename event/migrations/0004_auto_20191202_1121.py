# Generated by Django 2.2.7 on 2019-12-02 11:21

from django.db import migrations, models
import event.models.event


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20191202_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(null=True, upload_to=event.models.event._content_file_name),
        ),
    ]