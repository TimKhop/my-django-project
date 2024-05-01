# Generated by Django 4.2.11 on 2024-04-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_payment_id_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='В обработке', max_length=50, verbose_name='Статус заказа'),
        ),
    ]
