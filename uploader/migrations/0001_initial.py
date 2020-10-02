# Generated by Django 3.1.2 on 2020-10-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('file_name', models.CharField(max_length=500)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('uploaded_at', models.DateTimeField()),
                ('expired_at', models.DateTimeField()),
            ],
        ),
    ]
