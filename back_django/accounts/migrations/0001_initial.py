# Generated by Django 3.0.5 on 2020-05-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('portal_id', models.CharField(max_length=10, null=True, unique=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('dept_major', models.CharField(max_length=50, null=True)),
                ('username', models.SlugField(max_length=30, null=True, unique=True)),
                ('reputation', models.IntegerField(default=0)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
