# Generated by Django 3.2.4 on 2021-06-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='admin@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]