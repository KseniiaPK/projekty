from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_pojmy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clanek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100)),
                ('nazev', models.CharField(max_length=100)),
                ('popis', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]