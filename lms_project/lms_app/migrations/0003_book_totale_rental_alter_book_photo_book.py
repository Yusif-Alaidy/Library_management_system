# Generated by Django 5.0 on 2023-12-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_book_photo_author_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='totale_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo_book',
            field=models.ImageField(upload_to='photos'),
        ),
    ]