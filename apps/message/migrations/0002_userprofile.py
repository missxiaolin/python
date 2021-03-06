# Generated by Django 2.0.1 on 2018-01-11 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('birday', models.DateField(default='', verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=5)),
                ('address', models.CharField(default='', max_length=100, verbose_name='地址')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True)),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'abstract': False,
            },
        ),
    ]
