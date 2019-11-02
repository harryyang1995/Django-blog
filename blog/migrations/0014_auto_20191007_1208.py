# Generated by Django 2.2.6 on 2019-10-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191002_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-order', 'add_time'], 'verbose_name': '1-文章分类', 'verbose_name_plural': '1-文章分类'},
        ),
        migrations.AlterField(
            model_name='article',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, help_text='越大越前', verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, help_text='越大越前', verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='link',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, help_text='越大越前', verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, help_text='越大越前', verbose_name='排序'),
        ),
    ]