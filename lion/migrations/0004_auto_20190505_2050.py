# Generated by Django 2.0.13 on 2019-05-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lion', '0003_lion_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=200)),
                ('password', models.IntegerField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='lion',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
    ]
