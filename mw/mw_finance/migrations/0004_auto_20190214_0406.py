# Generated by Django 2.1.5 on 2019-02-14 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mw_finance', '0003_auto_20190211_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency_info',
            old_name='등락률',
            new_name='change',
        ),
        migrations.RenameField(
            model_name='currency_info',
            old_name='전일대비',
            new_name='comparing_yesterday',
        ),
        migrations.RenameField(
            model_name='currency_info',
            old_name='현재가',
            new_name='current_price',
        ),
        migrations.RenameField(
            model_name='currency_info',
            old_name='심볼',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='currency_info',
            old_name='통화명',
            new_name='symbol',
        ),
        migrations.AlterField(
            model_name='currency_info',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
