# Generated by Django 3.1.7 on 2021-03-17 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210317_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='/static/img/single_blog_1.png', upload_to='images/'),
            preserve_default=False,
        ),
    ]
