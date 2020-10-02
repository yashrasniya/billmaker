# Generated by Django 3.1.1 on 2020-10-02 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_product', models.CharField(max_length=200)),
                ('quantity_of_product', models.IntegerField()),
                ('gst', models.IntegerField(default=18)),
                ('rate_of_product', models.IntegerField()),
            ],
        ),
    ]
