# Generated by Django 2.0.13 on 2019-10-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20191022_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='exitmark',
            field=models.IntegerField(blank=True, choices=[(300, '出口１')], max_length=20),
        ),
        migrations.AlterField(
            model_name='group',
            name='landmark',
            field=models.IntegerField(blank=True, choices=[(100, '都庁'), (200, '新宿ピカデリー')], max_length=20),
        ),
        migrations.AlterField(
            model_name='route',
            name='route',
            field=models.CharField(choices=[(1, '小田急小田原線'), (2, '都営新宿線'), (3, '東京メトロ丸ノ内線'), (4, 'JR中央線'), (5, 'JR埼京線'), (6, 'JR総務線'), (7, 'JR山の手線(外回り)'), (8, 'JR山の手線(内回り)'), (9, 'JR湘南新宿ライン'), (10, '京王線'), (11, '京王新線'), (12, '西武新宿線')], max_length=20),
        ),
    ]
