# Generated by Django 4.2.5 on 2023-10-21 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popular',
            name='image',
            field=models.FileField(upload_to='popular', verbose_name='Film Afişi'),
        ),
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('text', models.TextField(default='', verbose_name='Açıklama')),
                ('image', models.FileField(upload_to='netflix', verbose_name='Film Afişi')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMy.category', verbose_name='Kategori')),
            ],
        ),
    ]
