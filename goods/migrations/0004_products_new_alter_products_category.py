# Generated by Django 4.2.11 on 2024-04-15 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_categories_image_alter_products_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='new',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Навинки'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c', to='goods.categories', verbose_name='Категория'),
        ),
    ]
