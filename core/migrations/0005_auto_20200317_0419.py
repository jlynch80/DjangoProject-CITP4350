# Generated by Django 2.2.10 on 2020-03-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image4',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image5',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('SE', 'Sedan'), ('TR', 'Truck'), ('SU', 'SUV')], max_length=2),
        ),
    ]
