# Generated by Django 3.2.3 on 2021-05-31 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tindog_app', '0003_auto_20210531_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentsforkar', models.ManyToManyField(to='tindog_app.ContentsForKar')),
            ],
        ),
    ]
