# Generated by Django 5.1.3 on 2024-11-22 17:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]