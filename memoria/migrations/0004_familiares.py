# Generated by Django 4.2.1 on 2023-06-16 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoria', '0003_planes_alter_memorial_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id_familiar', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_familiar', models.CharField(max_length=100)),
                ('apellidos_familiar', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_deceso', models.DateField()),
            ],
        ),
    ]
