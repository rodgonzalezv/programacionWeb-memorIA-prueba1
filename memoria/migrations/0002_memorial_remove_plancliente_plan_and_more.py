# Generated by Django 4.2.1 on 2023-06-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memorial',
            fields=[
                ('id_memorial', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='plancliente',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='plancliente',
            name='user',
        ),
        migrations.DeleteModel(
            name='Familiar',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
        migrations.DeleteModel(
            name='PlanCliente',
        ),
    ]
