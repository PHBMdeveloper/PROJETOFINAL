# Generated by Django 2.1.5 on 2019-01-29 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca'),
        ),
    ]
