# Generated by Django 3.2.9 on 2021-12-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_monografia_formato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='Formato',
            field=models.CharField(choices=[('PDF', 'PDF'), ('WORD', 'WORD'), ('ZIP', 'ZIP')], max_length=100),
        ),
    ]
