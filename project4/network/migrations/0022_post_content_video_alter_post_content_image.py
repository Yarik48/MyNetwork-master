# Generated by Django 4.1.7 on 2023-03-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0021_alter_post_content_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_image',
            field=models.ImageField(blank=True, upload_to='posts/'),
        ),
    ]
