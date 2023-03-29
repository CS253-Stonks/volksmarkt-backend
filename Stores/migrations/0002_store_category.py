# Generated by Django 4.1.1 on 2023-03-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Medical', 'Medical'), ('Stationary', 'Stationary'), ('Print', 'Print'), ('General Store', 'General Store'), ('grocery', 'grocery'), ('books', 'books'), ('food', 'food'), ('Others', 'Others')], max_length=20, null=True),
        ),
    ]