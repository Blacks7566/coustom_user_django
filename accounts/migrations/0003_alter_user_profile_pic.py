# Generated by Django 4.1.3 on 2022-12-23 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='profiles/profile.png', upload_to='profiles'),
        ),
    ]
