# Generated by Django 4.0.6 on 2022-07-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=45, null=True, verbose_name='User id')),
                ('username', models.CharField(max_length=45, null=True, verbose_name='Username')),
                ('name', models.CharField(max_length=45, null=True, verbose_name='Name')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user/avatar/', verbose_name='Avatar')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Custom User',
                'verbose_name_plural': 'Custom Users',
                'ordering': ['name'],
            },
        ),
    ]
