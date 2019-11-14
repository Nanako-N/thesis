# Generated by Django 2.0.13 on 2019-10-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20191022_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='destination',
            field=models.BooleanField(choices=[(True, 'あり'), (False, 'なし')], default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='exitmark',
            field=models.IntegerField(choices=[(-1, '-------'), (300, '出口１')], default=0),
        ),
        migrations.AlterField(
            model_name='group',
            name='landmark',
            field=models.IntegerField(choices=[(-1, '-------'), (100, '都庁'), (200, '新宿ピカデリー')], default=0),
        ),
    ]