# Generated by Django 4.2.1 on 2023-06-16 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoria', '0006_familiares_dv_familiar_familiares_nacionalidad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=100)),
            ],
        ),
    ]
