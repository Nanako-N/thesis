# Generated by Django 2.0.13 on 2019-12-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20191023_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='exitmark',
            field=models.IntegerField(choices=[[-1, '--------'], [26, '西口'], [28, '中央西口'], [25, '中央東口'], [43, '東口'], [30, '東南口'], [543, '南口'], [33, '新南口'], [32, 'ミライナタワー口'], [31, '甲州街道口'], [603, '2番出口'], [604, '3番出口'], [648, '4番出口'], [607, '5番出口'], [611, '6番出口'], [609, '7番出口'], [612, '8番出口'], [247, 'A1出口'], [219, 'A2出口'], [215, 'A4出口'], [212, 'A5出口'], [205, 'A6出口'], [203, 'A7出口'], [303, 'A8出口'], [317, 'A9出口'], [401, 'A10出口'], [441, 'A11出口'], [444, 'A12出口'], [440, 'A13/A14出口'], [417, 'A15出口'], [420, 'A16出口'], [423, 'A17出口'], [422, 'A18出口'], [224, 'B2出口'], [221, 'B3出口'], [217, 'B4出口'], [214, 'B5出口'], [210, 'B6出口'], [208, 'B7出口'], [206, 'B9出口'], [201, 'B10出口'], [301, 'B11出口'], [319, 'B12a出口'], [320, 'B12b出口'], [322, 'B13出口'], [402, 'B14出口'], [403, 'B15出口'], [407, 'B16出口'], [406, 'B17出口'], [419, 'B18出口'], [409, 'D1出口'], [411, 'D2出口'], [413, 'D3出口'], [415, 'D4出口'], [416, 'D5出口'], [313, 'M出口'], [501, '地上出口1'], [505, '地上出口2'], [511, '地上出口3'], [514, '地上出口4'], [528, '地上出口5'], [525, '地上出口6'], [522, '地上出口7'], [518, '地上出口8'], [516, '地上出口9'], [436, '地上出口11'], [435, '地上出口12'], [434, '地上出口13'], [433, '地上出口14'], [429, '地上出口15'], [428, '地上出口16'], [427, '地上出口17'], [426, '地上出口18'], [430, '地上出口19'], [425, '地上出口20'], [604, '京王モールA出口'], [537, '京王モールB出口'], [536, '京王モールC出口'], [533, '京王モールD出口'], [526, '京王モールE出口'], [529, '京王モールF出口'], [534, '京王モールG出口'], [538, '京王モールH出口'], [101, 'サブナード1番出口'], [103, 'サブナード2番出口'], [108, 'サブナード3番出口'], [106, 'サブナード4番出口'], [113, 'サブナード5番出口'], [111, 'サブナード6番出口'], [114, 'サブナード7番出口'], [116, 'サブナード8番出口'], [119, 'サブナード9番出口'], [117, 'サブナード10番出口'], [122, 'サブナード11番出口'], [125, 'サブナード12番出口'], [123, 'サブナード13番出口'], [126, 'サブナード14番出口'], [129, 'サブナード15番出口'], [130, 'サブナード15B出口'], [131, 'サブナード16番出口'], [134, 'サブナード17番出口'], [133, 'サブナード18番出口'], [137, 'サブナード19番出口'], [136, 'サブナード20番出口'], [139, 'サブナード21番出口'], [138, 'サブナード22番出口'], [237, 'C1出口'], [233, 'C2出口'], [235, 'C3出口'], [239, 'C4出口'], [241, 'C5出口'], [242, 'C6出口'], [244, 'C7出口'], [245, 'C8出口'], [231, 'E1出口'], [230, 'E2出口'], [228, 'E3出口'], [226, 'E4出口'], [254, 'E5出口'], [256, 'E6出口'], [258, 'E7出口'], [259, 'E8出口'], [250, 'E9出口'], [252, 'E10出口'], [631, 'N1出口'], [633, 'N2出口'], [635, 'N3出口'], [637, 'N4出口'], [639, 'N5出口'], [641, 'N6出口'], [615, 'O1出口'], [617, 'O2出口'], [644, 'S2出口'], [646, 'S3出口'], [622, 'シーズンロードS1出口'], [624, 'シーズンロードS2出口'], [626, 'シーズンロードS3出口'], [628, 'シーズンロードS4出口'], [620, 'ワンデーストリート新宿ワシントンホテル出口'], [619, 'ワンデーストリート東京都庁出口']], default=0),
        ),
        migrations.AlterField(
            model_name='group',
            name='landmark',
            field=models.IntegerField(choices=[[-1, '--------'], [33, '新宿サザンテラス'], [32, '高島屋'], [522, '京王プラザホテル'], [619, '東京都庁'], [620, '新宿ワシントンホテル'], [543, '小田急サザンタワー'], [254, '新宿御苑'], [261, '高島屋タイムズスクエア'], [212, 'ビックロ'], [43, 'ルミネエスト'], [35, '小田急百貨店本館'], [28, '京王百貨店'], [539, 'ルミネ１'], [29, 'ルミネ２'], [425, '新宿エルタワー'], [208, '紀伊国屋ビル'], [230, '花園神社'], [322, 'スタジオアルタ'], [407, '小田急ハルク'], [206, '新宿ピカデリー'], [214, '伊勢丹'], [108, 'TOHOシネマズ新宿'], [237, '新宿バルト９'], [215, '新宿マルイ本館']], default=0),
        ),
        migrations.AlterField(
            model_name='route',
            name='number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='route',
            name='route',
            field=models.IntegerField(choices=[[7, '小田急小田原線'], [2, '都営新宿線\u3000新宿三丁目駅'], [4, '東京メトロ丸ノ内線\u3000新宿駅'], [6, 'JR線'], [8, '京王線'], [11, '京王新線'], [9, '都営大江戸線\u3000新宿駅'], [0, '西武新宿線'], [1, '東京メトロ丸ノ内線\u3000新宿三丁目駅'], [5, '都営大江戸線\u3000新宿西口駅'], [3, '副都心線\u3000新宿三丁目駅'], [10, '都営新宿線\u3000新宿駅']]),
        ),
    ]
