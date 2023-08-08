from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItPojem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zkratka', models.SlugField(max_length=100)),
                ('nazev', models.CharField(max_length=100)),
                ('popis', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]