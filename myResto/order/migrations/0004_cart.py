# Generated by Django 5.0.6 on 2024-06-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=255)),
                ('items', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=12)),
            ],
        ),
    ]
