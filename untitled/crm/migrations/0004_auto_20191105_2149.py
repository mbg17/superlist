# Generated by Django 2.2 on 2019-11-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20191105_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futhurdetail',
            name='status',
            field=models.IntegerField(choices=[(1, '正在跟进'), (2, '3天未跟进'), (3, '15天未成单'), (4, '放弃跟单')], default=1),
        ),
    ]
