# Generated by Django 4.2.1 on 2023-06-15 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoria', '0002_memorial_remove_plancliente_plan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id_plan', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Planes',
                'verbose_name_plural': 'Planess',
            },
        ),
        migrations.AlterModelOptions(
            name='memorial',
            options={'verbose_name': 'Memorial', 'verbose_name_plural': 'Memorials'},
        ),
        migrations.AlterField(
            model_name='memorial',
            name='id_memorial',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]