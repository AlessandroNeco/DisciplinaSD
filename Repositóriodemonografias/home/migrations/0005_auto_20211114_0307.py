# Generated by Django 3.2.9 on 2021-11-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_monografia_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='Area',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='Autor',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='Banca',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='Curso',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='Formato',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='Numero_de_Paginas',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='Orientador',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='Titulo',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='Universidade',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='Url',
            field=models.CharField(max_length=300),
        ),
    ]
