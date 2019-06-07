# Generated by Django 2.2.1 on 2019-06-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='image_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='issue',
            name='issue_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='issue',
            name='image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue',
            field=models.FileField(blank=True, upload_to='issues/'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='soundcloud',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='issue',
            name='youtube',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
