# Generated by Django 4.0 on 2021-12-30 13:57

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('facultad', models.CharField(choices=[(1, 'Facultad 1'), (2, 'Facultad 2'), (3, 'Facultad 3'), (4, 'Facultad 4'), (5, 'FTE'), (6, 'CITEC')], max_length=20)),
                ('grupo', models.CharField(choices=[(1, 'F1401'), (2, 'F1402'), (3, 'F1403'), (4, 'F1404'), (5, 'F1405')], max_length=20)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
