# Generated by Django 3.0.5 on 2023-03-20 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop8', '0003_auto_20230320_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='shop8.Category'),
        ),
    ]
