# Generated by Django 4.1.7 on 2023-03-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_alter_post_content_image_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_image',
            field=models.ImageField(blank=True, upload_to='posts/'),
        ),
    ]
